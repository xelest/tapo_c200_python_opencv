# Using Tapo C200 TP Link Camera OpenCV Script Documentation
#### Introduction

This documentation provides a guide on how to use the Tapo C200 TP Link camera with OpenCV. The script connects to the camera using an RTSP link and captures video frames for further processing or display.

#### Prerequisites

To use this script, ensure that you have the following:

+ Tapo C200 TP Link camera
+ Python 3 installed
+ OpenCV library installed (pip install opencv-python)

#### Usage
1. Set up camera connection details:
```
ip_address = '192.168.0.XX'  # Replace with the IP address of your camera
port = '554'                # Replace with the port number for your camera
username = 'admin'          # Replace with the username for your camera
password = 'password'       # Replace with the password for your camera
```
2. Construct the RTSP stream URLs:
```
url_640x480 = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"
```

3. Set the desired RTSP stream URL:
```
rtsp_url = url_640x480  # Set it to either `url_640x480` or `url_1080p` based on the desired resolution
```

4. Run the script and observe the video stream

#### Example Configuration:
```
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

````

#### Conclusion
This script provides a basic implementation to connect to a Tapo C200 TP Link camera using an RTSP link and utilize the video feed with OpenCV. Feel free to modify the configuration and adapt it to your specific use case.

Please note that this script assumes a working network connection to the Tapo C200 camera and proper configuration of the camera's IP address, port, username, and password.

#### Resources & References
https://www.tp-link.com/us/support/faq/2680/

https://www.ispyconnect.com/

https://www.ispyconnect.com/camera/tp-link

https://programtalk.com/vs4/python/JurajNyiri/pytapo/


#### How to Setup Tapo Smart Home WiFi Camera C200
"https://www.youtube.com/watch?v=ozBOifbkqGk"
