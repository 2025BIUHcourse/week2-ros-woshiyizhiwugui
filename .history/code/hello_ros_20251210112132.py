#!/usr/bin/env python3
"""hello_ros.py

ROS 示例节点：在话题 `hello_topic` 上以 1Hz 发布字符串消息。
在已配置 ROS 环境的 Ubuntu 上运行。
"""

import rospy
from std_msgs.msg import String


def talker():
	rospy.init_node('hello_ros_node')
	pub = rospy.Publisher('hello_topic', String, queue_size=10)
	rate = rospy.Rate(1)
	count = 0
	while not rospy.is_shutdown():
		msg = f'Hello from hello_ros.py #{count}'
		pub.publish(msg)
		rospy.loginfo(msg)
		count += 1
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

