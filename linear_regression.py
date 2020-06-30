import numpy as np
import matplotlib.pyplot as plt

n = 20

x_values = np.random.rand(n)*5
y_values = x_values*2+3.5
y_values = y_values + np.random.randn(n)*2

winkel=3.14/2
rotmatrix = np.array([[np.cos(winkel),-np.sin(winkel)], [np.sin(winkel), np.cos(winkel)]])

#plt.axis('equal')
plt.plot(x_values, y_values,'o')

regression = np.polyfit(x_values, y_values, 1)
plt.plot(x_values, x_values*regresion[0]+regresion[1], 'r')

regression = [0, np.mean(y_values)]

for i in range(n):
    plt.plot(x_values, x_values*regresion[0]+regresion[1], 'r')
    plt.plot([x_values[i], x_values[i]], [y_values[i], x_values[i]*regresion[0]+regresion[1]], 'g')


plt.plot(np.mean(x_values), np.mean(y_values), "bv", markersize =10)

# Drehung
pmax = np.array([[max(x_values)], [max(x_values)*regresion[0]+regresion[1]]])
pmin = np.array([[min(x_values)], [min(x_values)*regresion[0]+regresion[1]]])
pmean = np.array([[np.mean(x_values)], [np.mean(y_values)]])

#drehmatrix

#rotmatrix = np.array([[-np.sin(winkel), np.cos(winkel)], [np.cos(winkel), np.sin(winkel)]])

# https://www.youtube.com/watch?v=ZbbLMDX-s-0 hier mus noch pmean rein
pmax_new = np.dot(rotmatrix, (pmax-pmean))+pmean
pmin_new = np.dot(rotmatrix, (pmin-pmean))+pmean

plt.plot([pmax_new[0], pmin_new[0]], [pmax_new[1], pmin_new[1]], "r")
#plt.plot([pmax[0], pmin[0]], [pmax[1], pmin[1]], "g")

plt.show()
