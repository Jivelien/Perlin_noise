import math
import numpy as np
from matplotlib import pyplot as plt
from random import random

height = 1000
width = 2000
canva = np.empty([height,width])

class Perlin:
    def __init__(self, size, frequency):
        self.size = size
        self.frequency = frequency
        self.point = [random() for _ in range(self.frequency)]
        self.noise = [0]*self.size

        for i in range(self.size):
            weights = []
            for j in range(self.frequency):
                p_pos = self.size // self.frequency * j
                dist = min(abs(p_pos - i), abs((self.size + p_pos - i) % self.size))
                w = ((self.size - dist)/self.size )**10
                weights.append(w)
            self.noise[i] = sum([weights[k]*self.point[k] for k in range(self.frequency)]) / sum(weights)

p_row = Perlin(height, 500)
p_col = Perlin(width, 1000)

for r in range(height):
    for c in range(width):
        canva[r,c] = p_row.noise[r] + p_col.noise[c]

plt.imshow(canva)
plt.show()

plt.plot(p_row.noise)
