import cv2
from ultralytics import YOLO
import os
import random
model = YOLO("models/yolo_plate.pt")

img_path = "datasets/Car_Plates/images"
img_name = random.choice(os.listdir(img_path))

img = cv2.imread(os.path.join(img_path, img_name))
img = cv2.resize(img, (640, 640))

results = model(img, conf=0.05)  # VERY LOW THRESHOLD

print("Number of detections:", len(results[0].boxes))

for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    conf = float(box.conf[0])

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(
        img,
        f"{conf:.2f}",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

cv2.imshow("DEBUG TEST", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
