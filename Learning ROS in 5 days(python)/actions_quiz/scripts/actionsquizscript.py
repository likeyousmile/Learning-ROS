#! /usr/bin/python

import rospy
import time
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import *


def publish_once(pub, msg):
    r = rospy.Rate(1)
    while True:
        connections = pub.get_num_connections()
        if connections > 0:
            pub.publish(msg)
            rospy.loginfo("Publishing msg")
            break
        else:
            r.sleep()

class CustomActionServer:
    _feedback = CustomActionMsgFeedback()

    def __init__(self):
        rospy.init_node('action_custom_msg_as', log_level=rospy.DEBUG)
        self.action_server = actionlib.SimpleActionServer('action_custom_msg_as', CustomActionMsgAction, self.callback, auto_start=False)
        self.rate = rospy.Rate(10)
        self.ctrl_c = False


    def callback(self, goal):
        self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self._takeoff_msg = Empty()
        self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self._land_msg = Empty()

        if goal.goal=='TAKEOFF':
            while not self.ctrl_c:
                i=0
                while not i == 3:
                    self._pub_takeoff.publish(self._takeoff_msg)
                    self.action_server.publish_feedback(self._feedback)
                    rospy.loginfo('Taking off...')
                    time.sleep(1)
                    i += 1
            
        elif goal.goal=='LAND':
            while not self.ctrl_c:
                i=0
                while not i == 3:
                    self._pub_land.publish(self._land_msg)
                    self.action_server.publish_feedback(self._feedback)
                    rospy.loginfo('LANDING')
                    time.sleep(1)
                    i += 1

    def start(self):
        self.action_server.start()
        rospy.spin()

if __name__=='__main__':
    custom_action_server = CustomActionServer()
    custom_action_server.start() 