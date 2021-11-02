import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D

rng = np.random.default_rng()

a, b, c = (rng.integers(5, size=(3, 3, 2)))
print (a)
print ("")
print (b)
print ("")
print (c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(a,b, c= 'red')
plt.show()