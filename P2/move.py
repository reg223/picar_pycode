from picarx import Picarx
import time

px = Picarx()

# TODO: experiment for turns to find out 90 Deg req
# TODO: experiment to find out move constant

orientation = 0

def forward(amount = 1):
  px.set_dir_servo_angle(0)
  px.forward(amount*50)
  time.sleep(0.385)
  px.forward(0)
  
def backward(amount = 1):
  px.set_dir_servo_angle(0)
  px.backward(amount*50)
  time.sleep(0.385)
  px.backward(0)
  
def rTurn(fixpos = True):
  orientation += 1
  if fixpos:
    px.set_dir_servo_angle(45)
    px.forward(30)
    time.sleep(0.3)
    px.set_dir_servo_angle(-45)
    px.back(30)
    time.sleep(0.3)
    px.backward(0)
    px.set_dir_servo_angle(0)
  else:
    px.set_dir_servo_angle(45)
    px.forward(30)
    time.sleep(1)
    px.backward(0)