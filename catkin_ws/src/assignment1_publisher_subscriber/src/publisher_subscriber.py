#!/usr/bin/env python
# assignment 2

import rospy
import numpy as np
from std_msgs.msg import Float32, String

def callback(yaw_msg):
	deg = round(rad2deg(yaw_msg),1)
	publisher.publish(output % (yaw_msg, deg))

def rad2deg(rad):
	return rad * 180 / np.pi

# Initialize node
rospy.init_node("echo_yaw_node")

# output format
output = "I heard: %f (~%.1f°)"

# Initialize publisher and subscriber
publisher = rospy.Publisher("/assignment1_publisher_subscriber", String)
rospy.Subscriber("/yaw", Float32, callback)

# spin() keeps python from exiting until this node is stopped
rospy.spin()
	
	
