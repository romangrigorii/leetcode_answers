# https://en.m.wikipedia.org/w/index.php?title=Bresenham%27s_line_algorithm&wprov=rarw1


# Develop an algorithm that will take a line's starting and ending corrdinates, and
# draw the line on a 2D raster.

import numpy as np
import matplotlib.pyplot as plt 

def bresenham(start,end,px):
    # start and end represent pair of nums corresponding to starting and ending positions
    # px represnts the pixel size in units of x. 

    sy = int(abs(start[1] - end[1])/px)
    sx = int(abs(start[0] - end[0])/px)

    map = np.zeros((sy,sx))

    st = (0,0)
    map[0,0] = 1
    ysum = 0
    y = 0
    for x in range(sx):
       ysum+=sx
       while ysum>sx:
           y+=1
           ysum -= sx
           map[y,x] = 1
    
    plt.imshow(map)
    plt.show()
    

bresenham((0,0),(20,5), 1)