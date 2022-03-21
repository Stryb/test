#!/usr/bin/env python3

import rospy
from time import sleep
from geometry_msgs.msg import Twist
import sys
 
 
def turtle_circle(radius,time):
    rospy.init_node('turtlesim', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',
                          Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
   # time = 1
    for i in range(0, int(time*10)): 
   # while not rospy.is_shutdown():
        vel.linear.x = radius
       # vel.linear.y = 0
        #vel.linear.z = 0
       # vel.angular.x = 0
       # vel.angular.y = 0
        vel.angular.z = 1.0
        rospy.loginfo("Radius = %f",
                      radius)
        pub.publish(vel)
        rospy.sleep(0.1)       
       #rate.sleep()
 
 
if __name__ == '__main__':
    try:
        turtle_circle(float(sys.argv[1]),float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass
