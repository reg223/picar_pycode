import cv2
import time
from picamera2 import Picamera2
import libcamera
from ultralytics import YOLO

# ---------- Custom interaction ----------
def on_stop_sign_detected(confidence: float):
    """
    This function is called every time a stop sign is detected
    with confidence >= DETECTION_THRESHOLD.
    Replace the body with whatever custom action you need:
      - trigger a GPIO pin
      - send a network message
      - stop a robot, etc.
    """
    print(f"STOP SIGN DETECTED! confidence={confidence:.2f}")
    # Example: GPIO.output(17, GPIO.HIGH)

# ---------- Settings ----------
MODEL_PATH = "/path/to/stop_sign_tiny.pt"   # your YOLO model
DETECTION_THRESHOLD = 0.5                   # adjust to taste

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

framecount, fps = 0, 0.0
start_time = time.time()

print("Starting detection loop. Press Ctrl+C to stop.")
while True:
    img = picam2.capture_array()

    # YOLO inference (no drawing)
    results = model.predict(img, verbose=False)

    # Each result can have multiple boxes
    if results and len(results[0].boxes) > 0:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            conf   = float(box.conf[0])
            # If your dataset has only 'stop sign' as class 0:
            if cls_id == 0 and conf >= DETECTION_THRESHOLD:
                on_stop_sign_detected(conf)


