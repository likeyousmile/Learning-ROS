#! /usr/bin/env python

import rospy                               # Import the Python library for ROS
from geometry_msgs.msg import Twist             # Import the Int32 message from the std_msgs package

rospy.init_node('topics_quiz_node')         # Initiate a Node named 'topic_publisher'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    
                                           # Create a Publisher object, that will publish on the /counter topic
                                           # messages of type Int32

rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
msg = Twist()
msg.linear.x = 1.0
msg.linear.y = 0.0
msg.linear.z = 0.0
msg.angular.x = 0.0
msg.angular.y = 0.0
msg.angular.z = 0.0                                                                                 

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
  pub.publish(msg)                       # Publish the message within the 'count' variable
  rate.sleep()                             # Make sure the publish rate maintains at 2 Hz