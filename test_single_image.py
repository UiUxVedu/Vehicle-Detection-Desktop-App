import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("models/yolo_plate.pt")

# Load test image
img = cv2.imread("test_plate.jpg")

if img is None:
    print("ERROR: test_plate.jpg not found")
    exit()

img = cv2.resize(img, (640, 640))

# Run detection
results = model(img, conf=0.15)

detected = False

for r in results:
    if r.boxes is None:
        continue

    for box in r.boxes:
        detected = True
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])

        print("Detected plate with confidence:", conf)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

if not detected:
    print(" NO PLATE DETECTED ")

cv2.imshow("Test Image Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
