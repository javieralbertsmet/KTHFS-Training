#!/usr/bin/env python

import rospy
import numpy as np
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
import matplotlib.pyplot as plt

N = 1500 # Number of datapoints to plot
STD_MULTIPLIER = 0.01 # This multiplier is used in the display of uncertainty (red lines) in the plot. An STD_MULTIPLIER of 0.01 means we take +-0.1*std's to represent the uncertainty
# x,y, x_std and y_std hold the data to be plotted
x = []
y = []
x_std = []
y_std = []

def odom_filtered_callback(data):
    x.append(data.pose.pose.position.x)
    y.append(data.pose.pose.position.y)

    x_std.append(STD_MULTIPLIER*np.sqrt(data.pose.covariance[0]))
    y_std.append(STD_MULTIPLIER*np.sqrt(data.pose.covariance[7]))

    if len(x) % N == N-1: # Every N iterations we plot
        plt.figure()
        plt.title("(X,Y) position, for " + str(len(x)) + " datapoints")
        plt.plot(x,y)
        plt.plot(np.array(x)+np.array(x_std),np.array(y)+np.array(y_std),'r')
        plt.plot(np.array(x)-np.array(x_std),np.array(y)-np.array(y_std),'r')
        plt.show()

if __name__ == '__main__':
    print("Running")

    rospy.init_node('slam', anonymous=True) # Only one node per process

    rospy.Subscriber('/odometry/filtered', Odometry, odom_filtered_callback) 

    rospy.spin()
