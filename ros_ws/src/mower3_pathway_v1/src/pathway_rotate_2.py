#!/usr/bin/env python3
# поворот и линия
import rospy
from time import sleep
from geometry_msgs.msg import Twist
import sys
rot = 1
def turtle_circle(radius = 2.3, time = 0.8):
	global rot
	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',
	Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
    # time = 1

	while not rospy.is_shutdown():
		rot = (-1) * rot
		b = input()
		b1 = input()		#	vel.linear.x = 0.3
		n=b/b1
		for a in range(0, n):
			print('итерация:', a)
	#		pub.publish(vel)
	#		rospy.sleep(0.1)
			for j in range(0, int(time*10)):
				vel.linear.x = 2.3
				vel.angular.z = 0
#			rospy.loginfo("Dlina zony = %f", b)
#			rospy.loginfo("Iteraciy = %f", b/b1)
				pub.publish(vel)
				rospy.sleep(0.1)
			for i in range(0, int(10.998)):
                        	vel.linear.x = 0.4
                        	vel.angular.z = 3.1*rot
                        	pub.publish(vel)
                        	rospy.sleep(0.1)


if __name__ == '__main__':
	try:
		turtle_circle(float(sys.argv[1]), float(sys.argv[1]))
	except rospy.ROSInterruptException:
		pass



