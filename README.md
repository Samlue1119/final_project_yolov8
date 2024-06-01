# Traffic Light Control and Person Detection System

This project implements a traffic light control system with person detection using the YOLOv8 model. The system displays traffic light states and predicts the number of people in an image, triggering alerts if the count exceeds a specified threshold.

## Features

- Detect the number of persons in an image using the YOLOv8 model.
- Display a countdown for traffic light states (red and green).
- Change the duration of the green light if the detected number of persons exceeds 5.
- Show alert images if the person count is greater than 5.

## Prerequisites

- Python 3.x
- Tkinter
- PIL (Pillow)
- Ultralytics YOLOv8

## File Structure

project  
│  
├── main.py # The main script for the traffic light control and person detection system  
├── Seven Segment.ttf # The font used for displaying the countdown  
├── yolov8/  
│ ├── runs/  
│ │ ├── detect/  
│ │ │ ├── predict1/  
│ │ │ │ └── malu1.jpg # Example image for person detection  
│ │ │ └── train2/  
│ │ │ └── weights/  
│ │ │ └── best.pt # Trained YOLOv8 model weights  
│ └── photo/  
│ ├── button.jpg # Button image for triggering person detection  
│ ├── rd light_1.png # Red light image  
│ ├── rd light_2.png # Green light image  
│ ├── y light_1.png # Yellow alert light image (state 1)  
│ ├── y light_2.png # Yellow alert light image (state 2)  
└── README.md # This README file  

## Usage

1. Navigate to the project directory.

2. Run the main script:
    ```sh
    python main.py
    ```

3. The GUI will open displaying the initial state with a traffic light and a button. Click the button to predict the number of persons in the image.

4. If the person count exceeds 5, the system will:
   - Change the green light duration to 6 seconds.
   - Show alert images.

## Code Explanation

### Main Functions

- `predict(i)`: Loads and displays the image for person detection.
- `get_person()`: Returns the detected number of persons as a string.
- `get_second(state, green_duration=3)`: Returns the countdown time based on the traffic light state.
- `add()`: Disables the button and starts the countdown.
- `show_page(frame)`: Raises the specified frame to the top of the window.
- `update_image_with_countdown(i, state, green_duration=3)`: Updates the traffic light image with a countdown timer.
- `alert_sys()`: Shows alert images if the person count exceeds 5 and changes the green light duration.
- `show_alert_image(repetitions)`: Alternates between two alert images for a flashing effect.

### Event Flow

1. Click the button to trigger `add()`.
2. `add()` calls `update_image_with_countdown()`.
3. `update_image_with_countdown()` updates the countdown and calls itself every second.
4. When the countdown reaches zero, the light state changes, and if the state is red, `alert_sys()` is called.
5. `alert_sys()` updates the green light duration and triggers the alert images if the person count exceeds 5.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
