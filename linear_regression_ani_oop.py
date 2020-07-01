############################################################
### Linear Regression animation with gradient descent  #####
### regression line is rotated using a rotation matrix #####
### (angle is in radians)                              #####
############################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style, gridspec
from math import degrees

class RegressAni:

    def __init__(self):
        # initialize values
        self.n = 50
        self.angle = 0
        self.direction = 1
        self.angleinc = 0.05
        self.limit = 150

        # generate random test sample
        self.x_values = np.random.rand(self.n)*5+1
        self.y_values = self.x_values*1.2+3.5 + np.random.randn(self.n)*1.2

        # initial regression line parameters (horizontal line through mean of y-values)
        # [slope, y-intercept]
        self.linreg = [0, np.mean(self.y_values)]

        # calculate initial points of the line corresponding to the min and max x-values
        self.pmax = np.array([[max(self.x_values)], [max(self.x_values)*self.linreg[0]+self.linreg[1]]])
        self.pmin = np.array([[min(self.x_values)], [min(self.x_values)*self.linreg[0]+self.linreg[1]]])

        # linear regression line always goes through (mean(x), mean(y))
        # and is therefore center of rotation
        self.pmean = np.array([[np.mean(self.x_values)], [np.mean(self.y_values)]])

        # rotation matrix
        self.rotmatrix = np.array([[np.cos(self.angle),-np.sin(self.angle)], [np.sin(self.angle), np.cos(self.angle)]])
        self.residuals = [[],[]]

        # initialize figure
        self.fig = plt.figure()
        self.fig.suptitle('Linear regression', fontsize=20)
        self.fig.set_size_inches(5*2.54, 2.5*2.54)
        self.gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
        plt.subplots_adjust(wspace = 0.3)
        self.ax1 = self.fig.add_subplot(self.gs[0])
        self.ax2 = self.fig.add_subplot(self.gs[1])
        self.fig.patch.set_facecolor('#e2e2e2')
        self.ax1.set_facecolor('#bebebe')
        self.ax2.set_facecolor('#bebebe')

        # setup animation
        self.anim = animation.FuncAnimation(self.fig, self.update, interval=5)

        # setup the animation control
        self.anim_running = True

    def calculate(self):
        #compute new rotation matrix
        self.rotmatrix = np.array([[np.cos(self.angle),-np.sin(self.angle)], [np.sin(self.angle), np.cos(self.angle)]])
        # compute new dot-matrix products
        self.pmax_new = np.dot(self.rotmatrix, (self.pmax-self.pmean))+self.pmean
        self.pmin_new = np.dot(self.rotmatrix, (self.pmin-self.pmean))+self.pmean
        #compute regress line from this
        self.linreg = np.polyfit([self.pmax_new[0][0], self.pmin_new[0][0]], [self.pmax_new[1][0], self.pmin_new[1][0]], 1)

    def update(self, frame):
        self.calculate()

        # plot x and y values
        self.ax1.clear()
        self.ax1.set_ylim(min(self.y_values)-1,max(self.y_values)+1)
        self.ax1.set_xlim(0,7)
        self.ax1.plot(self.x_values, self.y_values,'o')

        # plot regress line
        self.ax1.plot(self.x_values, self.x_values*self.linreg[0]+self.linreg[1], 'r')
        self.ax1.set_title(f"y = {self.linreg[0]:.2f}*x + {self.linreg[1]:.2f}", fontsize=17)
        self.ax1.set_xlabel("x", fontsize=17)
        self.ax1.set_ylabel("y", rotation=0, fontsize=17)

        # plot residuals in ax2
        # calculate current residualsquares
        self.residualsquares = 0
        for i in range(self.n):
            self.ax1.plot([self.x_values[i], self.x_values[i]], [self.y_values[i], self.x_values[i]*self.linreg[0]+self.linreg[1]], 'g')
            self.residualsquares += (self.y_values[i] - (self.x_values[i]*self.linreg[0]+self.linreg[1]))**2

        self.residuals[0] += [self.angle]
        self.residuals[1] += [self.residualsquares]

        self.ax2.clear()
        self.ax2.set_title("$R^2$", fontsize=17)
        self.ax2.set_ylim(0,max(self.residuals[1]))
        self.ax2.set_xlabel("angle °", fontsize=17)
        self.ax2.set_ylabel("$R^2$", fontsize=17, rotation=0)
        self.ax2.yaxis.set_label_coords(-0.3, 0.5)
        self.ax2.plot([degrees(x) for x in self.residuals[0]],self.residuals[1])
        self.ax2.plot(degrees(self.residuals[0][-1]),self.residuals[1][-1], "ro")

        # calculate turning criteria
        if (len(self.residuals[1])>1) and (self.residuals[1][-1] > self.residuals[1][-2]) and (self.residuals[1][-1] > self.limit):
            self.direction *=-1
            self.angle += self.angleinc*self.direction
            self.angleinc *= 0.8
            self.limit = min(self.residuals[1])+(self.residuals[1][-1]-min(self.residuals[1]))/2
        else:
            self.angle += self.angleinc*self.direction

        # plot tangent to residual function by plotting through the last two points
        # starting from at least two points radians is converted to degrees
        if (len(self.residuals[1])>1) and (abs(self.residuals[1][-1]-self.residuals[1][-2]) > 0.00001):
            self.regresstangente = np.polyfit([self.residuals[0][-1], self.residuals[0][-2]], [self.residuals[1][-1], self.residuals[1][-2]], 1)
            self.ax2.plot([degrees(min(self.residuals[0])), degrees(max(self.residuals[0]))], [x *self.regresstangente[0]+self.regresstangente[1] for x in [min(self.residuals[0]), max(self.residuals[0])]])
        elif (len(self.residuals[1])>1):
            print("done")
            self.anim.event_source.stop()
            self.anim_running = False

    def animate(self):
        plt.show()

ani = RegressAni()
ani.animate()
