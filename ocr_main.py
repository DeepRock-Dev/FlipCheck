import cv2
import pytesseract
import streamlit as st
from PIL import Image
import numpy as np

# Expanded product list with descriptions
product_list = {
    "OTC items": "Health supplements, skin care, and personal hygiene items.",
    "Personal care items": "Deodorants, lipstick, face creams, shampoo, etc.",
    "Household items": "Cooking oil, toiletries, package food items.",
    "Electronic items": "Smartphones, chargers, headphones, etc.",
    "Food items": "Beverages, snacks, and packaged foods.",
    "Stationery items": "Pens, notebooks, staplers, and office supplies.",
    "Toiletries": "Toilet cleaner, soaps, shampoos, detergents, etc.",
    "Cosmetics": "Face cream, makeup, perfumes, and personal grooming items.",
    "Beverages": "Soft drinks, juices, bottled water, tea, and coffee.",
    "Snacks": "Chips, cookies, biscuits, candies, and packaged snacks.",
    "Packaged food": "Canned food, ready-to-eat meals, and instant noodles.",
    "Pharmaceuticals": "Medicines, vitamins, and health supplements.",
    "Kitchen items": "Spices, cooking oils, condiments, and sauces."
}

# Function to handle OCR with Tesseract
def ocr_with_tesseract(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(gray, config='--psm 6')
    return text

# Streamlit interface to handle webcam capture or file upload
st.title("Product Scanner")

# Option to upload an image
uploaded_file = st.file_uploader("Upload an image of the product")

# Button to capture image from webcam
if st.button("Capture Image"):
    cap = cv2.VideoCapture(0)
    
    # Capture a frame from the webcam
    ret, frame = cap.read()
    cap.release()  # Release the webcam after capturing the image
    
    if ret:
        st.image(frame, channels="BGR", caption="Captured Image", use_column_width=True)
        
        # Perform OCR on the captured image
        ocr_text = ocr_with_tesseract(frame)
        st.write("### Detected Text:")
        st.write(ocr_text)
        
        # Perform case-insensitive matching with the product list
        ocr_text_lower = ocr_text.lower()  # Convert OCR text to lowercase
        
        product_info = {}
        for product, description in product_list.items():
            if product.lower() in ocr_text_lower:  # Case-insensitive comparison
                product_info["Product Description"] = description
                product_info["Product Name"] = product
        
        # Display the extracted product information
        if product_info:
            st.write("### Detected Product Information")
            st.table({
                "Field": ["Product Name", "Product Description"],
                "Detected Value": [
                    product_info.get("Product Name", "Not detected"),
                    product_info.get("Product Description", "Not detected")
                ]
            })
        else:
            st.write("No matching products detected.")
    else:
        st.write("Failed to capture image.")

# Process uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Display uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Perform OCR on the uploaded image
    ocr_text = ocr_with_tesseract(image_cv)
    st.write("### Detected Text:")
    st.write(ocr_text)
    
    # Perform case-insensitive matching with the product list
    ocr_text_lower = ocr_text.lower()  # Convert OCR text to lowercase
    
    product_info = {}
    for product, description in product_list.items():
        if product.lower() in ocr_text_lower:  # Case-insensitive comparison
            product_info["Product Description"] = description
            product_info["Product Name"] = product
    
    # Display the extracted product information
    if product_info:
        st.write("### Detected Product Information")
        st.table({
            "Field": ["Product Name", "Product Description"],
            "Detected Value": [
                product_info.get("Product Name", "Not detected"),
                product_info.get("Product Description", "Not detected")
            ]
        })
    else:
        st.write("No matching products detected.")
