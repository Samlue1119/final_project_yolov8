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

## Usage

1. Navigate to the project directory.

2. Run the main script:
    ```sh
    python main.py
    ```

3. The GUI will open displaying the initial state with a traffic light and a button. Click the button to predict the number of persons in the image.

4. If the person count exceeds 5, the system will:
   - Change the green light duration to max(6, (person_count - 3) * 0.2 + 5) seconds, capped at 10 seconds.  
   - Show alert images.
     
5.Ensure you have the best.pt file (trained YOLOv8 model weights) in the yolov8/runs/detect/train2/weights/ directory.  
If not, you can train your own model or download pre-trained weights from the Ultralytics YOLOv8 repository.  

## Code Explanation

### Main Functions

- `predict(i)`: Loads and displays the image for person detection.
- `get_person()`: Returns the detected number of persons as a string.
- `get_second(state, green_duration)`: Returns the countdown time based on the traffic light state.
- `add()`: Disables the button and starts the countdown.
- `show_page(frame)`: Raises the specified frame to the top of the window.
- `update_image_with_countdown(i, state, green_duration)`: Updates the traffic light image with a countdown timer.
- `alert_sys()`: Shows alert images if the person count exceeds 5 and changes the green light duration.
- `show_alert_image(repetitions)`: Alternates between two alert images for a flashing effect.

### Event Flow

1. Click the button to trigger `add()`.
2. `add()` calls `update_image_with_countdown()`.
3. `update_image_with_countdown()` updates the countdown and calls itself every second.
4. When the countdown reaches zero, the light state changes, and if the state is red, `alert_sys()` is called.
5. `alert_sys()` updates the green light duration and triggers the alert images if the person count exceeds 5.

## License

This project is licensed under the Taiwan License - License Owner [@01057050andrea](https://github.com/01057050andrea), [@Samlue1119](https://github.com/Samlue1119), [@90w09](https://github.com/90w09), [@Bryan9103](https://github.com/Bryan9103), [@Fangyil](https://github.com/Fangyil).
