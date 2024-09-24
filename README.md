# Face and Eye Detector

This software is a face and eye detection tool using **OpenCV** and **Haar Cascade Classifiers**. It loads an image, locates human faces and eyes within the image, and draws rectangles around the detected faces and eyes. The image is then displayed with the detection results. This project displays mastery of basic coding techniques, visual data, and image manipulation.

## Features

- Detects faces using the `haarcascade_frontalface_default.xml` classifier.
- Detects eyes within the facial regions using the `haarcascade_eye.xml` classifier.
- Draws rectangles around detected faces and eyes for visual representation.
- Displays the final image with a scaled-down view for better visibility on different resolutions.

## Requirements

- Python 3.x
- OpenCV (`cv2` module)

## Installation

1. **Clone the repository** (or download the project files):
   ```bash
   git clone https://github.com/your-username/face-eye-detection-opencv.git
   cd face-eye-detection-opencv
2. **Install the required dependencies** (Ensure you have OpenCV installed. If not, you can install it using pip):
    ```bash
    pip install opencv-python

## Usage

1. **Run the script:**
    After you've installed the dependencies and placed the necessary Haar Cascade files in the directory, you can run the script as follows:

    ```bash
    python face_detection.py

2. **How it works:**
    - The script will read the image, convert it to grayscale, and detect faces using the haarcascade_frontalface_default.xml.
    - Once a face is detected, it looks for eyes within the facial region using the haarcascade_eye.xml.
    - Rectangles are drawn around the detected faces (in yellow) and eyes (in orange).
    - The resulting image is displayed in a scaled-down window for better visualization.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.