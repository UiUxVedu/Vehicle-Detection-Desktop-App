import cv2
import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from utils.detector import VehicleDetector

class DetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Detection")
        self.root.geometry("400x200")

        self.detector = VehicleDetector()
        self.video_path = None

        tk.Button(root, text="Select Video",
                  width=25, command=self.select_video).pack(pady=10)

        tk.Button(root, text="Start Detection",
                  width=25, command=self.start_detection).pack(pady=10)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
        )
        if self.video_path:
            messagebox.showinfo("Selected", "Video selected successfully")

    def start_detection(self):
        if not self.video_path:
            messagebox.showerror("Error", "Please select a video first")
            return

        os.makedirs("output", exist_ok=True)
        csv_path = "output/vehicles.csv"

        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            messagebox.showerror("Error", "Could not open video")
            return

        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Frame", "Time", "Confidence"])

            frame_id = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    print(" Video ended. ")
                    break

                frame = cv2.resize(frame, (960, 540))

                detections = self.detector.detect(frame)

                print(f"Frame {frame_id} → Vehicles: {len(detections)}")

                for x1, y1, x2, y2, conf in detections:
                    cv2.rectangle(frame, (x1, y1), (x2, y2),
                                  (0, 255, 0), 2)

                    writer.writerow([
                        frame_id,
                        datetime.now().strftime("%H:%M:%S"),
                        round(conf, 3)
                    ])

                cv2.imshow("Vehicle Detection (Press Q to Stop)", frame)
                frame_id += 1

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print(" Stopped by user. ")
                    break

        cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo(
            "Completed",
            f"Detection finished.\nCSV saved at:\n{csv_path}"
        )
