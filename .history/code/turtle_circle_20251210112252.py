#!/usr/bin/env python3
"""turtle_circle.py

ROS 节点：让 turtlesim 中的 /turtle1 以固定线速度和角速度画圆。
"""

import rospy
from geometry_msgs.msg import Twist


def turtle_circle(linear_speed=0.5, angular_speed=0.5):
	rospy.init_node('turtle_circle_node', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel_msg = Twist()

	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0

	while not rospy.is_shutdown():
		vel_msg.linear.x = linear_speed
		vel_msg.angular.z = angular_speed
		pub.publish(vel_msg)
		rate.sleep()


if __name__ == '__main__':
	try:
		turtle_circle()
	except rospy.ROSInterruptException:
		pass

