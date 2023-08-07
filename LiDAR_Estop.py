#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class sub_LiDAR:
    def __init__(self):
        rospy.init_node('mayu')
        rospy.Subscriber("/scan",LaserScan,callback=self.callback)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.cmd_vel = Twist()
        rospy.spin()

    def callback(self, msg):
        num = 0

        

        self.cmd_vel_pub.publish(self.cmd_vel)
        self.cmd_vel.linear.x = 0.2
        # if msg.range_max < :
        #     self.cmd_vel.linear.x = 0
        
        # else:
        #     self.cmd_vel.linear.x = 0.5

        # print(msg)
        # print("msg.range_min: ", msg.range_min)
        # print("msg.range_max: ", msg.range_max)
        # print(len(msg.ranges))
        print(len(msg.intensities))

if __name__ == '__main__':
    sub_LiDAR()
    rospy.spin()
