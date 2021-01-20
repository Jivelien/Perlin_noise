import math
import numpy as np
from matplotlib import pyplot as plt
import random

height = 100
width = 200
canva = np.empty([height,width])

canva[:,:]= 0
canva[10:20,100:110]= 254

for y in range(height):
    for x in range(width):
        canva[y,x] = x + (math.sin(x) + math.sin(y) + 2) * 254/4

plt.imshow(canva)

class perlin:
    def __init__(self, size, frequency):
        self.size = size
        self.frequency = frequency
        self.noise = [0]*size
        pass
    