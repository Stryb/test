#!/usr/bin/env python3
# поворот и линия
import rospy
from time import sleep
from geometry_msgs.msg import Twist
import sys

def turtle_circle(radius,time,time1):
	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',
	Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	# time = 1
	while not rospy.is_shutdown():
		for i in range(0, int(time*10)):
	#while not rospy.is_shutdown():
			vel.linear.x = 0.3
			vel.angular.z = 1.0
			pub.publish(vel)
			rospy.sleep(0.1)

#	vel = Twist()
		for j in range(0, int(time1*10)):
			vel.linear.x = radius
			vel.angular.z = 0
			rospy.loginfo("Radius = %f", radius)
			pub.publish(vel)
			rospy.sleep(0.1)
#rate.slep()

if __name__ == '__main__':
	try:
		turtle_circle(float(sys.argv[1]),float(sys.argv[1]),float(sys.argv[1]))
	except rospy.ROSInterruptException:
		pass
