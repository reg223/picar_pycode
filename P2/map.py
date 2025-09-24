import numpy as np
import math
import time
import move

px = move.px

MAPSIZE = 10

def scan():

    grid = np.zeros((MAPSIZE, MAPSIZE), dtype=np.uint8)
    origin_x = MAPSIZE/2    
    origin_y = 0     
    
    for angle in range(-60, 60, 5):   
        px.set_cam_pan_angle(angle)
        time.sleep(0.1)  # small pause for servo to settle

        dist_dm = round(px.ultrasonic.read()/10, 2)

        if dist_dm <= 0 or dist_dm > MAPSIZE:
            continue  


        rad = math.radians(angle)
        dx = dist_dm * math.sin(rad)
        dy = dist_dm * math.cos(rad)


        grid_x = int(round(origin_x + dx))
        grid_y = int(round(origin_y + dy))


        if 0 <= grid_x < MAPSIZE and 0 <= grid_y < MAPSIZE:
            grid[grid_y, grid_x] = 1

    px.set_cam_pan_angle(0)
    return grid
  
from numpy.lib.stride_tricks import sliding_window_view
def pad(grid):
    windows = sliding_window_view(grid, (3,3))
    out = np.zeros_like(grid)
    # If any cell in the 3x3 window is 1, center becomes 1
    mask = (windows.sum(axis=(2,3)) > 0)
    out[1:-1, 1:-1] = mask
    return out

def print_grid(grid):
  
 for row in reversed(grid):
        line = ''.join('#' if cell else '.' for cell in row)
        print(line)
