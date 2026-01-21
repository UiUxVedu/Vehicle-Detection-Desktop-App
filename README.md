#  Real-Time Vehicle Detection Desktop App

A desktop-based vehicle detection system built using **YOLOv8**, **Python**, **OpenCV**, and **Tkinter**.  
The application allows users to log in, select a video file, detect vehicles in real time, and store detection data in CSV format.

---

##  Features

- Login authentication (Tkinter GUI)
- Background image–based UI
- Vehicle detection using YOLOv8 (cars, buses, trucks, motorcycles)
- Video file selection
- Real-time bounding boxes
- CSV logging for post-analysis
- Modular and clean project structure

---

##  Tech Stack

- Python 3.9+
- YOLOv8 (Ultralytics)
- OpenCV
- Tkinter
- Pillow
- CSV

---

##  Project Structure

ALPR_OD/
├── main.py
├── gui/
│ ├── login.py
│ └── dashboard.py
├── utils/
│ └── detector.py
├── assets/
│ ├── bg_login.jpg
│ └── bg_dashboard.jpgs
├── output/
├── requirements.txt
└── README.md



##  How to Run

```bash
pip install -r requirements.txt
python main.py---