import streamlit as st
import cv2
import numpy as np
import time
from inference_sdk import InferenceHTTPClient

# Set up the Inference HTTP Client
CLIENT = InferenceHTTPClient(
    api_url="https://classify.roboflow.com",
    api_key="your_api_key"  # Replace with your actual API Key
)

# Streamlit UI setup
st.title("Live Object Detection with Roboflow")
st.sidebar.title("Options")

# Option to start webcam
run_webcam = st.checkbox("Start Webcam", value=False)

if run_webcam:
    video_stream = cv2.VideoCapture(0)
    stframe = st.empty()
    
    last_capture_time = time.time()  # Track the last capture time
    capture_interval = 1.0  # Capture interval in seconds
    detection_display = st.empty()  # Placeholder for detection display

    while run_webcam:
        ret, frame = video_stream.read()
        if not ret:
            st.warning("Failed to capture video.")
            break

        # Display the current frame
        stframe.image(frame, channels="BGR", use_column_width=True)

        # Check if it's time to capture an image
        current_time = time.time()
        if current_time - last_capture_time >= capture_interval:
            # Update last capture time
            last_capture_time = current_time
            
            # Save the frame temporarily to predict
            cv2.imwrite("temp_image.jpg", frame)

            # Infer on the saved image using the Roboflow inference client
            result = CLIENT.infer("temp_image.jpg", model_id="prp-s1udm/1")

            # Debugging: Print the result to understand its structure
            print("Inference Result:", result)

            # Check if result is a string, try to convert it to JSON
            if isinstance(result, str):
                try:
                    import json
                    result = json.loads(result)  # Attempt to parse string as JSON
                except json.JSONDecodeError:
                    st.error("Failed to decode JSON from the response.")
                    print("Received a non-JSON response:", result)
                    continue

            # Check if result is a dictionary and contains predictions
            if isinstance(result, dict) and "predictions" in result:
                predictions = result["predictions"]
                
                # Find the highest confidence prediction
                highest_confidence = 0
                highest_label = None
                
                for label, pred in predictions.items():
                    if isinstance(pred, dict):
                        confidence = pred["confidence"]
                        
                        # Update highest prediction if confidence is higher
                        if confidence > highest_confidence:
                            highest_confidence = confidence
                            highest_label = label
                
                # Update the detection display
                if highest_label and highest_confidence > 0.01:  # Only display if confidence is above threshold
                    detection_display.text(f"Detected: {highest_label} ({highest_confidence:.2f})")
                    
                    # Draw the label on the frame (optional)
                    cv2.putText(
                        frame,
                        f"{highest_label} ({highest_confidence:.2f})",
                        (10, 30),  # Display at top left
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2,
                    )
                else:
                    detection_display.text("No detections.")
            else:
                st.error("Error in inference result. Check the structure.")
                print("Unexpected result format:", result)

            # Display the frame with predictions
            stframe.image(frame, channels="BGR", use_column_width=True)

    # Release the webcam when done
    video_stream.release()

else:
    st.write("Click the checkbox to start the webcam.")
