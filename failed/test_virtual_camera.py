
#Open the camera and read the frames

import cv2
import pyfakewebcam

import numpy as np

gray = pyfakewebcam.FakeWebcam('/dev/video0', 640, 480)

while(True):
    # Capture frame-by-frame

    print('Type of gray ->', type(gray))
    gray = cv2.resize(gray, (500, 300))
    
    
    cv2.imshow("Pyfakewebcam", gray)

    key = cv2.waitKey(1)
    if key == 27:
        break

gray.release()
cv2.destroyAllWindows()
