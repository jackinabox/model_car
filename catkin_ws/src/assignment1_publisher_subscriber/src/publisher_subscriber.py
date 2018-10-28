#!/usr/bin/env python
# -*- coding: utf-8 -*-

# assignment 2

import math
import rospy
from std_msgs.msg import Float32, String

def callback(yaw_msg):
	deg = round(math.degrees(float(yaw_msg.data)),2)
	publisher.publish(String(output % (yaw_msg.data, deg)))

# Initialize node
rospy.init_node("echo_yaw_node")

# output format
output = "I heard: %f (%.2f deg)"

# Initialize publisher and subscriber
publisher = rospy.Publisher("/assignment1_publisher_subscriber", String, queue_size=10)
rospy.Subscriber("/yaw", Float32, callback)

# spin() keeps python from exiting until this node is stopped
rospy.spin()
