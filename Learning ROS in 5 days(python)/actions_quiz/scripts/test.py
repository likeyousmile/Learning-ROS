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
    
    def takeoff(self):
        rospy.loginfo("Taking off...")
        publish_once(self.pub_takeoff, self._takeoff_msg)
    
    def land(self):
        rospy.loginfo("Landing...")
        publish_once(self.pub_land, self._land_msg)

    def callback(self, goal):
        self.pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self._takeoff_msg = Empty()
        self.pub_land = rospy.Publisher('drone/land', Empty, queue_size=1)
        self._land_msg = Empty()

        if goal.goal=='TAKEOFF':
            self.takeoff()
            self._feedback.feedback = 'Taking off...'
            self.action_server.publish_feedback(self._feedback)
            rospy.sleep(1)
        elif goal.goal=='LAND':
            self.land()
            self._feedback.feedback = 'landing off...'
            self.action_server.publish_feedback(self._feedback)
            rospy.sleep(1)
        
    def start(self):
        self.action_server.start()
        rospy.spin()

if __name__=='__main__':
    custom_action_server = CustomActionServer()
    custom_action_server.start() 