# import map
import move
from picarx import Picarx
# import numpy as np




# px = Picarx()


def main():
  # grid = map.scan()

  print(px.ultrasonic.read())
  move.forward()
  print(px.ultrasonic.read())
  

if __name__ == "__main__":
  main()