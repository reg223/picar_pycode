# import map
import move
import map
import route
import vision 
# import numpy as np




px = move.px


def main():
  # grid = map.scan()
  ie = route.IE()
  while True:
    x,y = input("please provide target coordinates: ").split()
    
    ie.route(int(x),int(y))
  

if __name__ == "__main__":
  main()
