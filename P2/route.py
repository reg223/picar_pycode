import numpy as np
import map
import move
from collections import deque



class IE():
  
  def __init__(self):
    self.location = [0,0]
    self.orientation = 0
    #offset from current map scan, not necessarily origin
    self.offset_x = 0
    self.offset_y = 0
    self.queue = deque()
    self.grid = map.scan()
    pass
  
  # direction = orientation * 90 right (clockwise)
  def orient(self,x,y):
    self.orientation %= 4
    match(self.orientation):
      case 0:
        return x,y
      case 1:
        return y,x
      case 2:
        return -x,-y
      case 3:
        return -y,-x

  
  def update(self,x = 0, y = 0):
    self.offset_x += x
    self.offset_x += y
    
    if(abs(self.offset_x)+abs(self.offset_y) >= 50):
      self.map_reset()
      return
      
  def map_reset(self):
    self.offset_x = 0
    self.offset_y = 0
    o = self.orientation
    while(self.orientation):
      move.rTurn()
      self.orientation = (self.orientation+1)%4
    self.grid = map.scan()
    while(self.orientation != o):
      move.rTurn()
      self.orientation = (self.orientation+1)%4
  
  #TODO iterate off queue, call map reset when necessary
  #TODO implement obstacle detection
  def go(self):
    return
    
  #TODO: update queue with go strings
  def route(self,x = 0,y = 0):
    return
  

