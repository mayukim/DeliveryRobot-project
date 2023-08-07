#!/usr/bin/env python3
#해쉬뱅

import rospy #로스를 사용하기 위해서 로스 라이브러리를 불러옴
import random
from geometry_msgs.msg import Twist #터틀심 패키지 안에 있는 메세지 폴더에서 포즈라는 메세지 타입을 가져옴
from turtlesim.msg import Pose #지오메트리메세지 폴더 안에 있는 메세지 폴더에서 트위스트라는 메세지 타입을 가져옴


class Subscribe_test: #섭스크라이브 테스트라는 이름으로 클래스를 선언함
    def __init__(self): #클래스를 생성했으니 클래스가 생성될 때 실행되는 함수인 생성자 함수를 만듦
        rospy.init_node('wego_node') #로스 마스터에 노드의 이름을 등록 해 주는 init_node 함수를 로스파이 라이브러리 안에서 가져옴
        self.turtle_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=3) #로스파이 라이브러리 안에서 퍼블리셔 객체를 가쳐온 뒤 인스턴스화 시킴
        rospy.Subscriber("/turtle1/pose", Pose, self.callback) #로스 라이브러리 안에서 섭스크라이버 객체를 가져옴(콜백함수에게 현재 토픽에서 받는 정보를 전달)

    def callback(self, msg): #섭스크라이버에서 호출하는 (콜백)함수를 선언해줌(이름은 상관없음)
        cmd_msg = Twist() #트위스트라는 객체를 인스턴스화해서 cmd_msg로 생성합니다. (트위스트 객체는 선속도 각속도에 대한 정보를 가지고 있는 객체)
        # cmd_msg.linear.x = 1 #cmd_msg is Twist(cmd_msg는 Twist) Twist객체 안에 있던 linear.x 속성을 cmd_msg 또한 가지고 있음
        #cmd_msg.angular.z = 1 #cmd_msg is Twist(cmd_msg는 Twist) Twist객체 안에 있던 angular.z 속성을 cmd_msg 또한 가지고 있음
        if 

        


        self.turtle_pub.publish(cmd_msg) # 퍼블리셔 객체의 인스턴스인 self.turtle_pub에서 퍼블리시 함수를 가져와서 (cmd_msg)를 퍼블리시

def main():
    subscribe_test = Subscribe_test()
    rospy.spin()

if __name__ == '__main__':
    main()
