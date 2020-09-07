#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32
from stf_msgs.msg import Float32

def callback(data):
    q = 0.15
    pub = rospy.Publisher('/kthfs/result',Float32,queue_size=10) # may be a more efficient way
    rate = rospy.Rate(1) # Same rate as the publisher of the publisher.py script (in this case set to 1 Hz)
    msg = Float32(data.data/q)
    pub.publish(msg)
    rospy.loginfo(data.data/q) # data.data accesses the value of the integer in the message
    rate.sleep()

def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('/albert', UInt32,callback) # Callback function is executed when data is received
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Result_publisher',anonymoys=True)
    subscriber()
