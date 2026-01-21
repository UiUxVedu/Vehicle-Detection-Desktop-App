from ultralytics import YOLO

model = YOLO("runs/detect/alpr_plate4/weights/best.pt")
model.export(format="torchscript")
