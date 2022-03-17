#! /usr/bin/env python

#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    my_response = BB8CustomServiceMessageResponse()
    sides = request.side
    reps = request.repetitions
    moveBB8(reps, sides)
    my_response.success = True
    return my_response.success

def straight(sides):
    wait_time = float(sides/2)
    move.linear.x = 0.5
    pub.publish(move)
    rospy.sleep(wait_time)
    move.linear.x = 0.0
    pub.publish(move)
    rospy.sleep(wait_time)

def rotate():
    move.angular.z = 0.195
    pub.publish(move)
    rospy.sleep(8)
    move.angular.z = 0
    pub.publish(move)
    rospy.sleep(1)

def moveBB8(reps, sides):
    i = 0
    j = 1
    while i < reps:    
        while j < 4:
            straight(sides)
            rotate()
            j+=1
        i+=1
        j=0

    while i == reps:    
        while j < 4:
            straight(sides)
            straight(sides)
            rotate()
            j+=1
        i+=1
        j=0

rospy.init_node('bb8_square') 

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
move = Twist()
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) 
rospy.wait_for_service('/move_bb8_in_square_custom')

rate = rospy.Rate(10)

rospy.spin()
