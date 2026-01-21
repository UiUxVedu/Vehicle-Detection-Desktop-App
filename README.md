## Real-Time Vehicle Detection Desktop Application[Build in 13 jan to 21 jan] 

A desktop-based computer vision application developed using YOLOv8, Python, OpenCV, and Tkinter that performs real-time vehicle detection from video files and logs detection results into a CSV file for further analysis.

The application features a login system, a graphical user interface, video selection from the local system, real-time bounding box visualization, and automated data recording.

## Project Overview

This project demonstrates the complete pipeline of a real-world computer vision system, including:

Desktop GUI development

Deep learning–based object detection

Video processing

Data logging

Modular software design

Version control using Git and GitHub

The system is designed to be scalable, allowing future integration of license plate detection and OCR.

# Key Features

# Login Authentication

Username and password–based access using Tkinter GUI

# Modern Desktop Interface

Background image–based UI for both login and dashboard pages

# Video File Selection

Users can select any video file from their local system

## Real-Time Vehicle Detection

Detects:

Cars

Buses

Trucks

Motorcycles

Powered by YOLOv8 pretrained model

# Bounding Box Visualization

Vehicles are highlighted with bounding boxes during playback

# CSV Data Logging

Detection details are automatically saved to a CSV file

Useful for post-analysis and reporting

# Modular Project Structure

Clean separation of GUI, detection logic, and utilities

# Tech Stack

Programming Language: Python 3.9+

Deep Learning Model: YOLOv8 (Ultralytics)

Computer Vision: OpenCV

GUI Framework: Tkinter

Image Handling: Pillow (PIL)

Data Storage: CSV

Version Control: Git & GitHub

## Project Structure
ALPR_OD/
│
├── main.py                  # Application entry point
│
├── gui/
│   ├── login.py             # Login screen GUI
│   └── dashboard.py         # Main dashboard & detection UI
│
├── utils/
│   └── detector.py          # YOLOv8 vehicle detection logic
│
├── assets/
│   ├── bg_login.jpg         # Login page background image
│   └── bg_dashboard.jpg     # Dashboard background image
│
├── output/
│   └── vehicles.csv         # Auto-generated detection results
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

# How to Run the Project
# Clone the Repository
git clone https://github.com/<your-username>/Vehicle-Detection-Desktop-App.git
cd Vehicle-Detection-Desktop-App

#Create & Activate Environment (Optional but Recommended)
conda create -n alpr_env python=3.9
conda activate alpr_env

# Install Dependencies
pip install -r requirements.txt

# Run the Application
python main.py

# Login Credentials
(Credentials can be modified inside gui/login.py)

## Video Input

The application allows users to select video files from any location on their system.

Test videos are not included in the repository to keep it lightweight and reusable.

Supported Formats:

.mp4

.avi

.mov

## Output Details

Detection results are saved automatically in:

output/vehicles.csv


CSV columns include:

Frame number

Timestamp

Detection confidence


## Final Note

This project reflects real-world software engineering practices, combining deep learning, desktop application development, and clean code architecture.
