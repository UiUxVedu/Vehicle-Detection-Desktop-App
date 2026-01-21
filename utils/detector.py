from ultralytics import YOLO

class VehicleDetector:
    def __init__(self):
        # Pretrained YOLOv8 model (vehicle detection)
        self.model = YOLO("yolov8n.pt")

        # COCO class IDs for vehicles
        self.vehicle_classes = [2, 3, 5, 7]
        # 2 = car, 3 = motorcycle, 5 = bus, 7 = truck

    def detect(self, frame, conf=0.25):
        results = self.model(frame, conf=conf, verbose=False)
        detections = []

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                cls = int(box.cls[0])
                if cls in self.vehicle_classes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confidence = float(box.conf[0])
                    detections.append((x1, y1, x2, y2, confidence))

        return detections
