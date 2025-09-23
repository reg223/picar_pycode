import numpy as np
import math
import time
import move

px = move.px

MAPSIZE = 100

def scan():

    grid = np.zeros((MAPSIZE, MAPSIZE), dtype=np.uint8)
    origin_x = 50    
    origin_y = 0     
    
    for angle in range(-45, 45, 5):   
        px.set_cam_pan_angle(angle)
        time.sleep(0.05)  # small pause for servo to settle

        dist_cm = round(px.ultrasonic.read(), 2)

        if dist_cm <= 0 or dist_cm > 100:
            continue  


        rad = math.radians(angle)
        dx = dist_cm * math.sin(rad)
        dy = dist_cm * math.cos(rad)


        grid_x = int(round(origin_x + dx))
        grid_y = int(round(origin_y + dy))


        if 0 <= grid_x < 100 and 0 <= grid_y < 100:
            grid[grid_y, grid_x] = 1

    px.set_cam_pan_angle(0)
    return pad(grid)
  
def pad(grid, pad_width=1):

  return np.pad(grid, pad_width, mode="constant", constant_values=0)

def print_grid(grid):
  
 for row in reversed(grid):
        line = ''.join('#' if cell else '.' for cell in row)
        print(line)