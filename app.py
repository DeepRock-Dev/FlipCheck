import streamlit as st

# 1. Create the main navigation and layout
st.set_page_config(page_title="Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Freshness Index Detection", "OCR", "Barcode Detection", "Image-based Counting"])

# 2. Home Page
if page == "Home":
    st.title("Welcome to the Multi-feature Dashboard")
    st.write("""
    This dashboard provides multiple functionalities, including:
    - **Freshness Index Detection**: Detects freshness using live webcam and Roboflow inference.
    - **OCR (Optical Character Recognition)**: Scans product images to extract text and match them with known product descriptions.
    - **Barcode Detection**: Live barcode scanning using a webcam.
    - **Image-based Counting**: Count objects in live webcam feed using the YOLO model.
    Navigate through the sidebar to explore each feature.
    """)
    
    
    
    # Copyright Statement
    st.write("© Copyright 2024, All Rights Reserved | TEAM ROCKS")

# 3. About Page
elif page == "About":
    st.title("About This Dashboard")
    st.write("""
    ### Overview
    This dashboard integrates four functionalities using OpenCV, YOLO, Roboflow, and Tesseract:
    1. **Freshness Index Detection**: Utilizes a pre-trained Roboflow model to detect object freshness from a webcam feed.
    2. **OCR (Optical Character Recognition)**: Extracts text from images and matches it against a predefined list of product types.
    3. **Barcode Detection**: Scans barcodes using a live video feed and decodes them for display.
    4. **Image-based Object Counting**: Uses the YOLO object detection model to count items in a live video feed.
    
    ### Dataset Information
    The image-based counting model (YOLO) was trained on a large dataset of over 19,000 images.

    ### Installation and Setup Instructions:
    You will need the following libraries and dependencies:
    - **Python 3.11.0**
    - **Streamlit**
    - **OpenCV**: `pip install opencv-python`
    - **PyZbar** (for barcode detection): `pip install pyzbar`
    - **Tesseract** (for OCR): Install Tesseract separately and add it to the system path.
    - **Roboflow SDK** (for Freshness Index Detection): `pip install roboflow`

    ### Running the Dashboard:
    1. Clone the repository and navigate to the project directory.
    2. Install all required dependencies using `pip install -r requirements.txt`.
    3. Run the Streamlit app: `streamlit run app.py`.
    """)

    # Team Members Section
    st.subheader("Meet Our Team")
    team_members = [
        {"name": "Yash Pathak", "github": "https://github.com/vindicta07", "linkedin": "https://www.linkedin.com/in/vindicta07/"},
        {"name": "Tanish Palkar", "github": "https://github.com/Tanishpalkar", "linkedin": "https://www.linkedin.com/in/tanish-palkar-5b70492b7/"},
        {"name": "Mangesh Tiwari", "github": "https://github.com/MANGESHti04", "linkedin": "https://www.linkedin.com/in/mangesh-tiwari-3804a8273/"},
        {"name": "Krunal Waghela", "github": "https://github.com/Kru938", "linkedin": "https://www.linkedin.com/in/krunal-waghela-8436ba154/"},
        {"name": "Omkar More", "github": "https://github.com/Omkarmore2003", "linkedin": "https://www.linkedin.com/in/omkarmore5/"},
    ]

    for member in team_members:
        st.write(f"{member['name']} | [GitHub]({member['github']}) | [LinkedIn]({member['linkedin']})")

    # Copyright Statement
    st.write("© Copyright 2024, All Rights Reserved | TEAM ROCKS")


# 4. Freshness Index Detection Page
elif page == "Freshness Index Detection":
    st.title("Freshness Index Detection")
    st.write("Running Freshness Index Detection...")

    # Import or run the freshness detection script
    with open('freshness_index.py') as f:
        exec(f.read())  # This will execute the code from 'freshness.py'
        
        
    # Copyright Statement
    st.write("© Copyright 2024, All Rights Reserved | TEAM ROCKS")

# 5. OCR Detection Page
elif page == "OCR":
    st.title("OCR - Product Scanner")
    st.write("Running OCR Detection...")

    # Import or run the OCR detection script
    with open('ocr_main.py') as f:
        exec(f.read())
        
        
    # Copyright Statement
    st.write("© Copyright 2024, All Rights Reserved | TEAM ROCKS")

# 6. Barcode Detection Page
elif page == "Barcode Detection":
    st.title("Barcode Detection")
    st.write("Running Barcode Detection...")

    # Import or run the barcode detection script
    with open('barcode.py') as f:
        exec(f.read())
        
        
    # Copyright Statement
    st.write("© Copyright 2024, All Rights Reserved | TEAM ROCKS")

# 7. Image-based Object Counting Page
elif page == "Image-based Counting":
    st.title("Object Counting with YOLO")
    st.write("Running Object Counting...")

    # Import or run the image counting script
    with open('Image_based_counting.py') as f:
        exec(f.read())
        
        
    # Copyright Statement
    st.write("© Copyright 2024, All Rights Reserved | TEAM ROCKS")
