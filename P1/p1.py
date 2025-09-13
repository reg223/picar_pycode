#P1.PY
# Created by Kuangyi "Sam" Hu (samhu2) for CS437 at UIUC
# Inspired by examples keyboard.py and obstacle_avoidance.py from the official Sunfounder picar-x repo

from picarx import Picarx
import time

from robot_hat import Music

#constants
MOVE = 50 #amount moved per step
SAFE = 15 #ignores anything closer than this (cm)


px = Picarx()
music = Music()

def main():
    px.set_dir_servo_angle(0) #straighten the servo
    
    while True:
        dist = px.get_distance()
        if dist < SAFE:
            px.stop()
            music.sound_play_threading('../sounds/car-double-horn.wav')
            time.sleep(1)
            px.set_dir_servo_angle(20)
            px.backward(MOVE)
            px.set_dir_servo_angle(0)
            px.backward(MOVE)
            px.set_dir_servo_angle(-20)
            px.backward(MOVE)
            px.set_dir_servo_angle(20)
            px.forward(MOVE)
            px.set_dir_servo_angle(0)
            px.forward(MOVE)
            px.set_dir_servo_angle(-20)
            px.forward(MOVE)
            px.set_dir_servo_angle(0)

        else:
            px.forward(MOVE)


