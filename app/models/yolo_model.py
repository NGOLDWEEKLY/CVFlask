from ultralytics import YOLO
import os
from config import Config
import time
import cv2

yolo_model = YOLO('../model/tuned_yolov8.pt')

# Function to perform ship detections
def defect_detect(img_path):
    
    # Read the image
    img = cv2.imread(img_path)

    # Pass the image through the detection model and get the result
    detect_result = yolo_model(img)
    # Plot the detections
    detect_img = detect_result[0].plot()
    
    # Convert the image to RGB format
    # detect_img = cv2.cvtColor(detect_img, cv2.COLOR_BGR2RGB)
    # Save the image
    new_file_name = str(hash(time.time())) + ".jpg"
    file_path = os.path.join(Config.USER_FOLDER, new_file_name)
    cv2.imwrite(file_path, detect_img)
    url_path = f"files/{new_file_name}"
    
    # Return the filepath
    return url_path

