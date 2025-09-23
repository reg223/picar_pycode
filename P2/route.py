import numpy as np
import map
import move
from collections import deque

debug = True


class IE():
  
  def __init__(self):
    self.location = [0,0]
    self.orientation = 0
    #offset from current map scan, not necessarily origin
    self.offset_x = 0
    self.offset_y = 0
    self.queue = deque()
    self.grid = map.scan()
    self.target = False
    self.target_loc = None
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

  #TODO: call route upon reset 
  def update(self,x = 0, y = 0):
    if debug: print("Updating position.")
    self.offset_x += x
    self.offset_x += y
    
    if(abs(self.offset_x)+abs(self.offset_y) >= 50):
      self.map_reset()
      self.queue = None
      self.route()
      return
      
  def map_reset(self):
    if debug: print("Resetting map.")
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
    while self.queue:
      direction, amount  = self.queue.pop()
      if debug: print("Now executing command d=",direction,", a =",amount)
      diff = int(direction) - self.orientation
      # 3 - 4
      if diff:
        move.rTurn() if (diff < 0) else move.lTurn()
        self.orientation = int(direction)
      move.forward(amount)
      off_x , off_y = self.orient(0,amount)
      self.location[0] += off_x
      self.location[1] += off_y
      if (sum(self.offset_x,off_x,self.offset_y,off_y)>= 50): break
      self.update(off_x,off_y)
      if (self.location == self.target_loc):
        self.goal()
    
    # trigger reset
    self.update(off_x,off_y)
       
    return
  
  def goal(self):
    self.target = False
    self.location = None

  def route(self,x = 0,y = 0):
    if debug: print("Setting Route for destination: X = ",x,", y = ",y)
    if (not self.target):
      if debug: print("Setting final destination: X = ",x,", y = ",y)
      self.target_loc = [x,y]    
    else:
      x = self.target_loc[0] - self.location[0]
      y = self.target_loc[1] - self.location[1]
    if x >= map.MAPSIZE:
      x = map.MAPSIZE
    if y >= map.MAPSIZE:
      y = map.MAPSIZE
    
    route = self.path(x,y)
    for step in route:
      self.queue.append(step)
      
    return
  
def path(self,x,y):
  if debug: print("Looking for optimal path to: X = ",x,", y = ",y)
  dirs = {
      '0': (0, 1),
      '2': (0, -1),
      '1': (1, 0),
      '3': (-1, 0)
  }
  def in_bounds(x, y):
    return 0 <= x < cols and 0 <= y < rows
  def direction(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    if dx == 1:  return '1'
    if dx == -1: return '3'
    if dy == 1:  return '0'
    if dy == -1: return '2'
  start = (self.location[0],self.location[1])
  goal = (x,y)
  q = deque([start])
  came_from = {start: None}
  while q:
    x, y = q.popleft()
    if (x, y) == goal:
        break
    for d, (dx, dy) in dirs.items():
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and self.grid[ny, nx] == 0 and (nx, ny) not in came_from:
            came_from[(nx, ny)] = (x, y)
            q.append((nx, ny))
  if goal not in came_from:
    if debug: print("Error: no path found for",x,", y = ",y)
    return [] # No path found
    
  path = []
  cur = goal
  while cur != start:
      path.append(cur)
      cur = came_from[cur]
  path.append(start)
  path.reverse()
  segments = []
  if len(path) < 2:
      return segments
  
  current_dir = direction(path[0], path[1])
  dist = 1

  for i in range(1, len(path) - 1):
      d = direction(path[i], path[i + 1])
      if d == current_dir:
          dist += 1
      else:
          segments.append((current_dir, dist))
          current_dir = d
          dist = 1
  segments.append((current_dir, dist))
  return segments
