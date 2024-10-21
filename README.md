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
