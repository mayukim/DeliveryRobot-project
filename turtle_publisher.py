#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def turtle_speed_publisher():
    rospy.init_node('turtle_speed_publisher', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        speed = Twist()
        speed.linear.x = 2.0
        speed.angular.z = 1.0
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_speed_publisher()
    except rospy.ROSInterruptException:
        pass