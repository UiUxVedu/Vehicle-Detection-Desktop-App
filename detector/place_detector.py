from ultralytics import YOLO

class PlateDetector:
    def __init__(self, model_path, conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        """
        Detect license plates in a frame.
        Returns list of bounding boxes: [x1, y1, x2, y2]
        """
        results = self.model(frame, verbose=False)
        boxes = []

        for result in results:
            for box in result.boxes:
                conf = float(box.conf[0])
                if conf >= self.conf_threshold:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    boxes.append((x1, y1, x2, y2))

        return boxes
