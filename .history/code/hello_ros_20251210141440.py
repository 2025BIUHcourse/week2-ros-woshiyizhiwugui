
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

