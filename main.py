from math import *
import numpy as np
import random

import Plot

random.seed()

Plot.set_DrawingArea()

x = [50] * 100
y = [50] * 100

#a = numpy.array((xa,ya,za))
#b = numpy.array((xb,yb,zb))
#position = [[x, y]] * 100

for times in range(1000):
    Draw_Frequency = 100
    for i in range(len(x)):
        theta = random.random() * 2 * pi
        x[i] = x[i] + 2 * cos(theta)
        y[i] = y[i] + 2 * sin(theta)
    if times % Draw_Frequency ==0 : Plot.Draw(x, y)
    


#dist = numpy.linalg.norm(a-b)





if __name__ == '__main__':
    pass