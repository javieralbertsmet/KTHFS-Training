#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32

def callback(data):
    q = 0.15
    print(data.data/q) # data.data accesses the value of the integer in the message

def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('/albert', UInt32,callback) # Callback function is executed when data is received
    rospy.spin()

def publisher():
    rospy.init_node('Result_publisher',anonymoys=True)
    rospy.Publisher('/kthfs/result',UInt32)

if __name__ == '__main__':
    subscriber()
