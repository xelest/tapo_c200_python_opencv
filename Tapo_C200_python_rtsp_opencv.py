#Using Tapo C200 TP Link Camera for Open CV 
#Connect using RTSP Link
#This is still in discovery phase and has a working script
#Mark Anthony V. Hernandez
#May 31, 2023

import cv2

# Set up camera connection details
ip_address = '192.168.0.XX' # Replace with the IP address of your camera
port = '554'          # Replace with the port number for your camera
username = 'admin'    # Replace with the username for your camera
password = 'password' # Replace with the password for your camera

# Construct the RTSP stream URLs using variables
url_640x480 = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"

# Set up RTSP stream URL
rtsp_url = url_640x480

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Check if the RTSP stream is opened successfully
if not cap.isOpened():
    print("Failed to open RTSP stream")
    exit()

while True:
    # Read a frame from the RTSP stream
    ret, frame = cap.read()

    # Check if the frame is read correctly
    if not ret:
        print("Failed to read frame")
        break

    # Display the frame
    cv2.imshow("RTSP Stream", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the RTSP stream and close the window
cap.release()
cv2.destroyAllWindows()
