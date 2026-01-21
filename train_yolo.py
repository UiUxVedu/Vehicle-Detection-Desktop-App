from ultralytics import YOLO
import os
print("CURRENT WORKING DIRECTORY:")
print(os.getcwd())


def train_model():
    model = YOLO("yolov8n.pt")
    # Start training
    model.train(
    data="datasets/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="alpr_plate"
)
if __name__ == "__main__":
    train_model()
