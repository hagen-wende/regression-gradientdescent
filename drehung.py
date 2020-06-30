import numpy as np
import matplotlib.pyplot as plt

winkel = 0.1

p1 = np.array([[1],[1]])
p2 = np.array([[0],[0]])

rotmatrix = np.array([[np.cos(winkel),-np.sin(winkel)], [np.sin(winkel), np.cos(winkel)]])

plt.plot(p1.reshape(-1)[0], p1.reshape(-1)[1], "ro")
plt.plot(p2.reshape(-1)[0], p2.reshape(-1)[1], "o")
plt.axis('equal')

for i in np.arange(0, 2*np.pi, 0.1):
    p1_new = np.dot(rotmatrix,p1_new)
    plt.plot(p1_new.reshape(-1)[0], p1_new.reshape(-1)[1], "go")
