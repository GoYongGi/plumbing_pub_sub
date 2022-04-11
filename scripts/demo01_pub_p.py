#! /usr/bin/env/python

from itertools import count
import rospy
from std_msgs.msg import String

"""
    使用 python 实现消息发布：
    1.导包：
    2.初始化 ros 节点；
    3.创建发布者对象；
    4.编写发布逻辑并发布数据
"""


if __name__ == "__main__":

    # 2.初始化 ros 节点；
    rospy.init_node("fabuzhe_py")
    # 3.创建发布者对象；
    pub = rospy.Publisher("AMR",String,queue_size=10)
    # 4.编写发布逻辑并发布数据
    #创建数据
    msg = String()
    #指定发布频率
    rate = rospy.Rate(1)
    #设置计数器
    count = 0
    #使用循环发布数据
    rospy.sleep(3)
    while not rospy.is_shutdown():
        count += 1
        msg.data = "hello" + str(count)
        #发布数据
        pub.publish(msg)
        rospy.loginfo("发布的数据：%s",msg.data)
        rate.sleep()
        




