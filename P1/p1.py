# P1.PY
# Created by Kuangyi "Sam" Hu (samhu2) for CS437 at UIUC
# Inspired by examples 3.tts_example.py and 4.avoiding_obstacles.py
# from the official Sunfounder picar-x repo

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
    try: 
        while True:
            dist = round(px.ultrasonic.read(), 2)
            if dist < SAFE:
                px.forward(0)
                time.sleep(1)
                music.sound_play_threading('car-double-horn.wav')
                px.set_dir_servo_angle(30)
                px.backward(MOVE)
                time.sleep(0.3)
                px.set_dir_servo_angle(0)
                time.sleep(1)
                px.set_dir_servo_angle(-30)
                time.sleep(0.3)
                
                px.set_dir_servo_angle(30)
                px.forward(MOVE)
                time.sleep(0.3)
                px.set_dir_servo_angle(0)
                time.sleep(1)
                px.set_dir_servo_angle(-30)
                time.sleep(0.3)
                px.set_dir_servo_angle(0)
                px.forward(0)

            else:
                px.forward(MOVE)
                time.sleep(0.1)
    finally:
        px.forward(0)


if __name__ == "__main__":
    main()
