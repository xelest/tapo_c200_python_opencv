# Tapo C200 & C211 TP Link Camera OpenCV Script Documentation

## Introduction

This documentation provides a guide on how to use Tapo C200 and C211 TP Link cameras with OpenCV. The script connects to the camera using RTSP and captures video frames for processing or display.

### Supported Cameras
- **Tapo C200** (original)
- **Tapo C211** (verified working with local account setup)

### YouTube Reference
https://www.youtube.com/watch?v=-kcVOxRNR9M

## Prerequisites

To use this script, ensure you have:

- Tapo C200/C211 TP Link camera
- Python 3 installed
- OpenCV library installed: `pip install opencv-python`
- Network access to camera (same subnet recommended)

## Camera Setup: Create Local Account

Before connecting via RTSP, you must create a **local camera account** (separate from Tapo cloud account).

### Step-by-Step Setup Guide

**For detailed visual instructions with screenshots, see the official TP-Link guide:**
👉 **[How to Create a Camera Account in the Tapo App](https://www.tp-link.com/us/support/faq/2680/)**

#### Quick Steps:

1. **Open Tapo App** → Select your camera
2. **Tap Settings** (⚙️ gear icon, top right)
3. **Go to Device Settings** → **Advanced Settings**
4. **Tap Camera Account** → **Create Account**
5. **Agree to the notice** and enter:
   - **Username** (example: `admin`, `myCamera`, etc.)
   - **Password** (6-32 characters, strong password recommended)
6. **Save** - RTSP is now enabled! ✅

---

### ⚠️ Important Notes:

- This creates a **local camera account** (separate from Tapo cloud)
- Use a **strong, unique password** (different from Tapo cloud password)
- RTSP is automatically enabled on **port 554** after account creation
- For security: only enable this account when needed for third-party access
- See [TP-Link FAQ #2680](https://www.tp-link.com/us/support/faq/2680/) for full visual walkthrough

---

### RTSP Stream URLs

Once the local account is created, use these URLs:

```
rtsp://username:password@camera_ip:554/stream1      # High resolution (1080p+)
rtsp://username:password@camera_ip:554/stream2      # Low resolution (640x480)
```

**Example for C211 at 192.168.0.226:**
```
rtsp://admin:MySecurePass@192.168.0.226:554/stream1
```

### Quick Checklist

- [ ] Open Tapo app
- [ ] Navigate to camera device
- [ ] Tap ⚙️ Settings icon (top right)
- [ ] Scroll to **Advanced Settings**
- [ ] Tap **Camera Account**
- [ ] Create username and password
- [ ] Save changes
- [ ] **RTSP is now enabled!** (port 554)

## Usage

### 1. Find Your Camera's IP Address
```bash
# Option A: Check router's connected devices
# Option B: Open Tapo app → Camera → Settings → Device Info → IP Address
# Option C: Use network scanner (Angry IP Scanner, etc.)
```

### 2. Set Up Connection Details
```python
ip_address = '192.168.1.XX'    # Replace with your camera's IP
port = '554'                    # RTSP port (default)
username = 'your_username'      # Username from local account setup
password = 'your_password'      # Password from local account setup
```

### 3. Construct RTSP Stream URLs
```python
# Stream options:
url_640x480 = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"  # 640x480
url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"    # 1080p or higher
url_2k = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"       # C211: 2304x1296
```

### 4. Choose Stream Resolution
```python
# Select the resolution you want
rtsp_url = url_1080p  # or url_640x480, or url_2k for C211
```

### 5. Run the Script
```bash
python Tapo_C200_python_rtsp_opencv.py
```

## Example Configuration

### Complete Python Example
```python
import cv2

# Camera connection details
ip_address = '192.168.1.100'      # Your camera IP
port = '554'                       # RTSP port
username = 'mycamera'              # Local account username
password = 'SecurePassword123'     # Local account password

# Construct RTSP URLs
url_640x480 = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"

# Select stream (use url_1080p for C211)
rtsp_url = url_1080p

# Open video stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Cannot open camera stream")
    exit()

# Get stream properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Stream resolution: {width}x{height}")

# Capture frames
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Display frame
    cv2.imshow('Tapo Camera Feed', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Tapo C211 Specific Configuration
```python
# Tapo C211 settings (verified working)
ip_address = '192.168.0.226'
port = '554'
username = 'admin'
password = 'your_local_password'

# C211 supports 2304x1296 (2K) resolution
rtsp_url = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"
```

## Troubleshooting

### Camera Connection Fails
- **Issue:** "Cannot open camera stream"
- **Solutions:**
  1. Verify local account is created in Tapo app settings
  2. Check camera IP address (use `ipconfig /all` or Tapo app)
  3. Ensure camera and PC are on same network
  4. Verify firewall allows port 554 (RTSP)
  5. Try port 8800 if port 554 doesn't work

### RTSP Port Not Found
- **Issue:** Port 554 is closed
- **Solutions:**
  1. Create a local camera account (see Camera Setup section)
  2. Restart camera after creating account
  3. Check if ISP/firewall blocks port 554
  4. Try alternative ports: 8800, 28800

### Wrong Credentials
- **Issue:** "401 Unauthorized" or connection timeout
- **Solutions:**
  1. Verify you're using **local account** (not Tapo cloud account)
  2. Double-check username/password in Tapo app
  3. Ensure no special characters issues in password
  4. Reset camera and recreate local account if issues persist

## Conclusion

This script provides a practical implementation to connect Tapo C200/C211 cameras using RTSP and OpenCV. Key requirements:
- A local camera account (separate from Tapo cloud)
- Correct IP, port, username, and password
- Network connectivity to camera

Feel free to modify for your specific use case and requirements.

## Resources & References

### Official TP Link Documentation
- [TP Link Tapo Support FAQ](https://www.tp-link.com/us/support/faq/2680/)
- [TP Link Tapo C200 Manual](https://www.tp-link.com/us/support/download/tapo-c200/)
- [TP Link Tapo C211 Specs](https://www.tp-link.com/us/product/tapo-c211/)

### RTSP and Streaming Guides
- [RTSP Protocol Overview](https://helpdesk.cctvdiscover.com/network/rtsp_stream.html)
- [iSpyConnect - Camera Guide](https://www.ispyconnect.com/)
- [iSpyConnect - TP Link Cameras](https://www.ispyconnect.com/camera/tp-link)

### Python Libraries
- [pytapo - Python Tapo Library](https://github.com/JurajNyiri/pytapo/)
- [OpenCV Python Documentation](https://docs.opencv.org/master/)

### Video Tutorials
- [Setup Tapo C200 - YouTube](https://www.youtube.com/watch?v=ozBOifbkqGk)
- [Python RTSP Stream - YouTube](https://www.youtube.com/watch?v=-kcVOxRNR9M)

## Camera Models Tested
- **C200** - Original implementation (working)
- **C211** - Enhanced with 2K resolution (verified working with local account)
