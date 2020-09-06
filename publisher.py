#!/usr/bin/env python
import rospy
import std_msgs


def publisher():

    # INITIALIZATION
    pub = rospy.Publisher('/albert', std_msgs.msg.UInt32, queue_size=10) # topic being published to and type
    rospy.init_node('publisher',anonymous=True) # name of the node is "publisher", anonymus set to True so that 'publisher' name is unique
    rate = rospy.Rate(1) # used to sleep for a certain time (20Hz)
    
    k = 1
    n = 4

    # COMPUTATION 
    while not rospy.is_shutdown():
        k += n
        message = std_msgs.msg.UInt32(k) # Create the message
        pub.publish(message) # Publish the message
        rate.sleep() # Wait a bit to send the next message
        

if __name__ == '__main__': # if this node is being run directly, and not being used for being imported
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass