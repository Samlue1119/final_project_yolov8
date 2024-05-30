from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")  # load an official model
    results = model.train(data="C:\C++\yolov8\data.yaml", epochs=3)
    # Validate the model
    model = YOLO("path/to/best.pt")
    results = model.predict(source="C:\C++\yolov8\malu1.jpg", save=True)
