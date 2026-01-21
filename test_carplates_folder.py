import cv2
import os
from ultralytics import YOLO

model = YOLO("models/yolo_plate.pt")

IMG_DIR = "datasets/Car_Plates/images"

for img_name in os.listdir(IMG_DIR):
    if not img_name.lower().endswith((".jpg", ".png")):
        continue

    img = cv2.imread(os.path.join(IMG_DIR, img_name))
    results = model(img)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(
                img,
                f"Plate {conf:.2f}",
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

    cv2.imshow("Car_Plates Dataset Test", img)
    key = cv2.waitKey(0)
    
    if key == 27:
        break

cv2.destroyAllWindows()
