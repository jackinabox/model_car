#!/usr/bin/env python
# assignment 2

import math
import rospy
from std_msgs.msg import Float32, String

def callback(yaw_msg):
	deg = round(math.degrees(yaw_msg),1)
	publisher.publish(output % (yaw_msg, deg))

# Initialize node
rospy.init_node("echo_yaw_node")

# output format
output = "I heard: %f (~%.1f°)"

# Initialize publisher and subscriber
publisher = rospy.Publisher("/assignment1_publisher_subscriber", String)
rospy.Subscriber("/yaw", Float32, callback)

# spin() keeps python from exiting until this node is stopped
rospy.spin()
