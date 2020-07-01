############################################################
### Linear Regression animation with gradient descent  ####
### regression line is rotated using a rotation matrix ####
### (angle is in radians)

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
        self.x_values = np.random.rand(n)*5+1
        self.y_values = x_values*1.2+3.5 + np.random.randn(n)*1.2

        # initial regression line parameters (horizontal line through mean of y-values)
        # [slope, y-intercept]
        self.linreg = [0, np.mean(y_values)]

        # calculate points of the line corresponding to the min and max x-values
        self.pmax = np.array([[max(x_values)], [max(x_values)*linreg[0]+linreg[1]]])
        self.pmin = np.array([[min(x_values)], [min(x_values)*linreg[0]+linreg[1]]])

        # linear regression line always goes through (mean(x), mean(y))
        self.pmean = np.array([[np.mean(x_values)], [np.mean(y_values)]])

        # rotation matrix
        self.rotmatrix = np.array([[np.cos(angle),-np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        residuals = [[],[]]

    def calculate(self):

    def animate(self):
        self.bla =0
