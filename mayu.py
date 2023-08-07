#!/usr/bin/env python3

import rospy 
from std_msgs.msg import String 


class pub(): 
    def __init__(self): 
        rospy.init_node('mayu') 
        self.pub = rospy.Publisher("/mayu/talking", String, queue_size=10) 
        rospy.Subscriber("/jesok_h/taking",String,callback=self.CB)
        self.msg = String()

    def CB(self,msg):
        print(msg)
    def main(self):
        self.msg.data = input("input here: ")
        self.pub.publish(self.msg)

if __name__ == '__main__':
    aub = pub()
    while not rospy.is_shutdown():
        aub.main()