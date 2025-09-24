import cv2
import time
from picamera2 import Picamera2
import libcamera
from ultralytics import YOLO

# ---------- Custom interaction ----------
# def on_stop_sign_detected(confidence: float):

#     print(f"STOP SIGN DETECTED! confidence={confidence:.2f}")


# ---------- Settings ----------
MODEL_PATH = "best.pt"   # your YOLO model
DETECTION_THRESHOLD = 0.25                   # adjust to taste

# ---------- Load YOLO model ----------
model = YOLO(MODEL_PATH)

# ---------- Setup PiCamera ----------



picam2 = Picamera2()
config = picam2.create_preview_configuration(
    main={"size": (640, 480), "format": "RGB888"},
    transform=libcamera.Transform(hflip=True, vflip=True)
)
picam2.configure(config)
picam2.start()




print("Starting detection loop. Press Ctrl+C to stop.")
def detection():
    img = picam2.capture_array()

    results = model.predict(img, verbose=False,conf=DETECTION_THRESHOLD)

    if results:
      return True
    else:
      return False


