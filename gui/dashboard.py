import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import cv2
import csv
import os
from datetime import datetime
from utils.detector import VehicleDetector

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Detection")
        self.root.geometry("960x540")
        self.root.resizable(False, False)

        # LOAD BACKGROUND IMAGE 
        bg_path = "assets/bg_dashboard.jpg"

        if not os.path.exists(bg_path):
            messagebox.showerror("Error", "Background image not found")
            return

        bg_image = Image.open(bg_path)
        bg_image = bg_image.resize((960, 540))
        self.bg_img = ImageTk.PhotoImage(bg_image)  # IMPORTANT

        # CANVAS 
        self.canvas = tk.Canvas(root, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        # DETECTOR 
        self.detector = VehicleDetector()
        self.video_path = None

        # BUTTONS 
        self.select_btn = tk.Button(
            root, text="Select Video", width=20, font=("Arial", 12),
            command=self.select_video
        )
        self.start_btn = tk.Button(
            root, text="Start Detection", width=20, font=("Arial", 12),
            command=self.start_detection
        )

        # Place buttons ON CANVAS
        self.canvas.create_window(480, 200, window=self.select_btn)
        self.canvas.create_window(480, 260, window=self.start_btn)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
        )
        if self.video_path:
            messagebox.showinfo("Video Selected", "Video selected successfully")

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
                    break

                frame = cv2.resize(frame, (960, 540))
                detections = self.detector.detect(frame)

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
                    break

        cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo(
            "Completed",
            "Detection completed.\nCSV saved in output folder."
        )
