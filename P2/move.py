from picarx import Picarx
import time
import vision

px = Picarx()

# TODO: experiment for turns to find out 90 Deg req


orientation = 0
safeDist = 15

def forward(amount = 1):
  px.set_dir_servo_angle(0)
  for i in range(amount):
    px.forward(50)
    time.sleep(0.385)
    detection()
  px.forward(0)
  
def backward(amount = 1):
  px.set_dir_servo_angle(0)
  px.backward(50)
  time.sleep(0.385*amount)
  px.backward(0)
  
def rTurn(fixpos = True):
  orientation += 1
  if fixpos:
    for i in range(4):
      px.set_dir_servo_angle(45)
      px.forward(30)
      time.sleep(0.3)
      px.set_dir_servo_angle(-45)
      px.backward(30)
      time.sleep(0.3)
      px.backward(0)
      px.set_dir_servo_angle(0)
  else:
    px.set_dir_servo_angle(45)
    px.forward(30)
    time.sleep(1.5)
    px.forward(0)
    
def lTurn(fixpos = True):
  if fixpos:
    for i in range(4):
      px.set_dir_servo_angle(-45)
      px.forward(30)
      time.sleep(0.3)
      px.set_dir_servo_angle(45)
      px.backward(30)
      time.sleep(0.3)
      px.backward(0)
      px.set_dir_servo_angle(0)
  else:
    px.set_dir_servo_angle(-45)
    px.forward(30)
    time.sleep(1.5)
    px.forward(0)
    
def detection():
  if px.ultrasonic.read() <= safeDist: 
    while px.ultrasonic.read() <= safeDist:
      px.forward(0)
  
  if vision.detection():
    px.forward(0)
    time.sleep(1)
    return