# Multi-feature Dashboard

Welcome to the **Multi-feature Dashboard**, an all-in-one platform that integrates multiple computer vision and image-processing functionalities using Streamlit, OpenCV, YOLO, Roboflow, Tesseract, and more. This dashboard allows you to perform various tasks including Freshness Index Detection, OCR (Optical Character Recognition), Barcode Detection, and Image-based Object Counting, all within a user-friendly interface.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Team](#team)
- [License](#license)

---

## Features

1. **Freshness Index Detection**
   - Uses a pre-trained model from Roboflow to detect the freshness of objects from a live webcam feed.
   
2. **OCR (Optical Character Recognition)**
   - Extracts and matches text from product images using Tesseract to predefined product types.

3. **Barcode Detection**
   - Scans and decodes barcodes in real-time via the webcam using PyZbar.

4. **Image-based Object Counting**
   - Utilizes the YOLO (You Only Look Once) model for counting objects in a live video feed.

## Installation

### Prerequisites
- **Python 3.11.0**
- **Streamlit**
- **OpenCV**: Install via `pip install opencv-python`
- **PyZbar**: Install via `pip install pyzbar`
- **Tesseract**: Install Tesseract separately and add it to your system's path. [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)
- **Roboflow SDK**: Install via `pip install roboflow`
  
### Setup Instructions
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/multi-feature-dashboard.git

## Usage

Once the dashboard is up and running, use the sidebar for navigation. The main features include:

- **Home**: Provides an overview of the dashboard and its features.
- **Freshness Index Detection**: Launches the Freshness Index Detection tool, which processes real-time video from the webcam to assess object freshness.
- **OCR (Optical Character Recognition)**: Runs the OCR tool that scans and extracts text from product images.
- **Barcode Detection**: Enables real-time barcode detection using your webcam to scan and decode barcodes.
- **Image-based Object Counting**: Utilizes the YOLO model to count objects in the live video feed.

Each page provides a brief description of the process and runs the respective functionality.

---

## Dataset Information

- The **Image-based Object Counting** feature utilizes the YOLO (You Only Look Once) object detection model, which was trained on a dataset of over 19,000 images to recognize and count various items.
- For **Freshness Index Detection**, a pre-trained Roboflow model is used to evaluate the freshness of objects based on visual data.

---

## Team

This project was created by **TEAM ROCKS**:

- [**Yash Pathak**](https://www.linkedin.com/in/vindicta07/)
- [**Tanish Palkar**](https://www.linkedin.com/in/tanish-palkar-5b70492b7/)
- [**Mangesh Tiwari**](https://www.linkedin.com/in/mangesh-tiwari-3804a8273/)
- [**Krunal Waghela**](https://www.linkedin.com/in/krunal-waghela-8436ba154/)
- [**Omkar More**](https://www.linkedin.com/in/omkarmore5/)

---

## License

© 2024 DeepRock-Dev. All Rights Reserved.

