import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style, gridspec
from math import degrees

def animate(i):
    global angle
    global direction
    global angleinc
    global limit

    #compute new rotation matrix
    rotmatrix = np.array([[np.cos(angle),-np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    # compute new dot-matrix products
    pmax_new = np.dot(rotmatrix, (pmax-pmean))+pmean
    pmin_new = np.dot(rotmatrix, (pmin-pmean))+pmean
    #compute regress line from this
    linreg = np.polyfit([pmax_new[0][0], pmin_new[0][0]], [pmax_new[1][0], pmin_new[1][0]], 1)
    # regresscalc = np.polyfit(x_values, y_values, 1)
    # plot x and y values
    ax1.clear()
    ax1.set_ylim(min(y_values)-1,max(y_values)+1)
    ax1.set_xlim(0,7)
    ax1.plot(x_values, y_values,'o')
    # plot regress line
    ax1.plot(x_values, x_values*linreg[0]+linreg[1], 'r')
    ax1.set_title(f"y = {linreg[0]:.2f}*x + {linreg[1]:.2f}", fontsize=17)
    ax1.set_xlabel("x", fontsize=17)
    ax1.set_ylabel("y", rotation=0, fontsize=17)

    #plot residuals
    residualsquares = 0
    for i in range(n):
        ax1.plot([x_values[i], x_values[i]], [y_values[i], x_values[i]*linreg[0]+linreg[1]], 'g')
        residualsquares += (y_values[i] - (x_values[i]*linreg[0]+linreg[1]))**2

    residuals[0] += [angle]
    residuals[1] += [residualsquares]

    ax2.clear()
    ax2.set_title("$R^2$", fontsize=17)
    ax2.set_ylim(0,max(residuals[1]))
    ax2.set_xlabel("angle °", fontsize=17)
    ax2.set_ylabel("$R^2$", fontsize=17, rotation=0)
    ax2.yaxis.set_label_coords(-0.3, 0.5)
    ax2.plot([degrees(x) for x in residuals[0]],residuals[1])
    ax2.plot(degrees(residuals[0][-1]),residuals[1][-1], "ro")

    if (len(residuals[1])>1) and (residuals[1][-1] > residuals[1][-2]) and (residuals[1][-1] > limit):
        direction *=-1
        angle += angleinc*direction
        angleinc *= 0.8
        limit = min(residuals[1])+(residuals[1][-1]-min(residuals[1]))/2
    else:
        angle += angleinc*direction

    # plot tangent to residual function by plotting through the last two points
    # starting from at least two points radians is converted to degrees
    if (len(residuals[1])>1) and (abs(residuals[1][-1]-residuals[1][-2]) > 0.00001):
        regresstangente = np.polyfit([residuals[0][-1], residuals[0][-2]], [residuals[1][-1], residuals[1][-2]], 1)
        ax2.plot([degrees(min(residuals[0])), degrees(max(residuals[0]))], [x *regresstangente[0]+regresstangente[1] for x in [min(residuals[0]), max(residuals[0])]])
    elif (len(residuals[1])>1):
        ax2.plot([degrees(min(residuals[0])), degrees(max(residuals[0]))], [x *regresstangente[0]+regresstangente[1] for x in [min(residuals[0]), max(residuals[0])]])
        print("done")


n = 50
angle = 0
direction = 1
angleinc = 0.05
limit = 150

x_values = np.random.rand(n)*5+1
y_values = x_values*1.2+3.5 + np.random.randn(n)*1.2

# initial regress
linreg = [0, np.mean(y_values)]

# rotation matrix
pmax = np.array([[max(x_values)], [max(x_values)*linreg[0]+linreg[1]]])
pmin = np.array([[min(x_values)], [min(x_values)*linreg[0]+linreg[1]]])
pmean = np.array([[np.mean(x_values)], [np.mean(y_values)]])
rotmatrix = np.array([[np.cos(angle),-np.sin(angle)], [np.sin(angle), np.cos(angle)]])
residuals = [[],[]]


# initialize figure
fig = plt.figure()
fig.suptitle('Linear regression', fontsize=20)
fig.set_size_inches(5*2.54, 2.5*2.54)
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplots_adjust(wspace = 0.3)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
fig.patch.set_facecolor('#e2e2e2')
ax1.set_facecolor('#bebebe')
ax2.set_facecolor('#bebebe')


ani = animation.FuncAnimation(fig, animate, interval=5)
plt.show()