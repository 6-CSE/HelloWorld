import random
import matplotlib.pyplot as plt
import numpy as np
for i in range(0,4000):
	x1 = random.random()
	y = x1 + 10 + random.random()/10
	plt.plot(x1, y, marker='o', markersize=1, color="blue")