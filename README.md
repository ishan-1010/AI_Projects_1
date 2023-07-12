# Hand Detection using Mediapipe

This code demonstrates hand detection using the `cv2` and `mediapipe` libraries. It captures video from the webcam and detects and tracks the landmarks of the hand.

## Requirements

- Python 3.x
- OpenCV (`cv2`) library
- Mediapipe (`mediapipe`) library

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/ishan-1010/Hand-Detection-Using-Mediapipe.git
   ```

2. Install the required libraries using pip:

   ```
   pip install opencv-python mediapipe
   ```

## Usage

1. Run the script:

   ```
   python hand_detection.py
   ```

2. A window will open displaying the webcam feed with hand landmarks and a frames-per-second (FPS) counter.

## Description

This script utilizes the `cv2` library to capture video from the webcam (`0` for the default webcam, or `1` for an external camera). It also uses the `mediapipe` library for hand detection and tracking.

The script starts a loop to continuously read frames from the video feed. For each frame, it converts the color space to RGB and processes it using the `mediapipe.Hands()` class. The detected hand landmarks are then displayed on the frame.

The script also prints the coordinates of each landmark and draws circles at the center of each landmark on the frame. The landmarks are identified by their index (`id`). The FPS is calculated and displayed in the top left corner of the frame.

Press `q` to quit the application.

## Contributing

Contributions are welcome! If you find any issues or want to enhance this project, feel free to open a pull request.
