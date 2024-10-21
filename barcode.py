import streamlit as st
import cv2
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time

# Initialize the Streamlit app
st.title("Live Barcode Scanner")
st.write("Press 'Capture' to log the detected barcode.")

# Start the video stream
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Initialize variables for found barcodes
found = set()
detected_barcodes = []

# Variable to hold the last detected barcode
last_detected = None

# Create a container for displaying the most recent detected barcode
last_detected_display = st.empty()

# Create a placeholder for the video frame
frame_placeholder = st.empty()

# Button to capture barcode
capture_button = st.button("Capture Barcode")

# Streamlit loop to display video frames
try:
    while True:
        # Grab the frame from the video stream and resize it
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        # Find the barcodes in the frame and decode each barcode
        barcodes = pyzbar.decode(frame)

        # Loop over the detected barcodes
        for barcode in barcodes:
            # Extract the bounding box location and draw the box on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Decode barcode data and type
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            # Draw the barcode data and type on the image
            text = f"{barcodeData} ({barcodeType})"
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # If the barcode text is not in our set, log it and update the set
            if barcodeData not in found:
                found.add(barcodeData)
                last_detected = barcodeData  # Update last detected barcode

        # Convert the frame to RGB and display it in Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")

        # Display the most recently detected barcode
        if last_detected:
            last_detected_display.text(f"Last Detected Barcode: {last_detected}")

        # Capture the barcode when the button is pressed
        if capture_button:
            if found:  # Check if there are any detected barcodes
                captured_barcodes = list(found)
                for barcode in captured_barcodes:
                    st.success(f"Captured Barcode: {barcode}")
            else:
                st.warning("No barcodes detected to capture.")

        # Break the loop if Streamlit is stopped
        if not frame_placeholder:
            break

except Exception as e:
    st.write("An error occurred: ", str(e))

finally:
    # Cleanup
    print("[INFO] cleaning up...")
    vs.stop()
