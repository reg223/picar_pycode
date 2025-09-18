# import map
import move

# import numpy as np




px = move.px


def main():
  # grid = map.scan()

  print(px.ultrasonic.read())
  move.forward()
  print(px.ultrasonic.read())
  

if __name__ == "__main__":
  main()