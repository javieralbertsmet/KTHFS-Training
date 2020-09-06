#!/usr/bin/env python

import rospy
import std_msgs

def callback(data):
    q = 0.15
    print(data.data/q) # data.data accesses the value of the integer in the message

def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('/albert', std_msgs.msg.UInt32,callback) # Callback function is executed when data is received
    rospy.spin()

if __name__ == '__main__':
    subscriber()