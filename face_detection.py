import cv2

# Load Haar Cascades
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load and process image if able
image = cv2.imread('example.jpg')
if image is None:
    print("Error loading image")
else:
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detects faces
    faces = face_classifier.detectMultiScale(image_grey, 1.1, 35)

    for (x,y,w,h) in faces:
        # Creates a rectangle around the face
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 0), 2)
        
        # Narrows computational focus to facial region
        face_grey = image_grey[y:y+h, x:x+w]
        face_color = image[y:y+h, x:x+w]

        # Finds eyes within facial region
        eyes = eye_classifier.detectMultiScale(face_grey, 1.1, 20)
        for (ex, ey, ew, eh) in eyes:
            # Creates a rectangle around the eyes
            cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)

    
    scale_percent = 30
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Displays result
    cv2.imshow('img', resized_image)
    cv2.waitKey()
    cv2.destroyAllWindows()