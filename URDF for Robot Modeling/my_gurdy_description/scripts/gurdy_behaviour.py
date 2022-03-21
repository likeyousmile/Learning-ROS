#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
from gurdy_mover import gurdyJointMover
from imu_data_processor import GurdyImuDataProcessor

#It will decide the behaviour based on the IMU data, so that when gurdy falls it gets up again detecting that it has fallen. 
#This is NOT implemented in the cmd_vel behaviour.
class GurdyBehaviour(object):

    def __init__(self):
        self.flip_time = rospy.get_time()
        self.imu_data_processor = GurdyImuDataProcessor()
        self.gurdy_mover = gurdyJointMover()


    def choose_behaviour(self, behaviour):
        detected_upsidedown = self.imu_data_processor.is_upasidedown()
        # Do something based on detect_upsidedown
        self.now_time = rospy.get_time()
        delta_time_since_flip = self.now_time - self.flip_time
        if delta_time_since_flip > 2.0:

            if detected_upsidedown:
                movement = "flip"
                self.flip_time = rospy.get_time()
            else:
                movement = behaviour        

            rospy.logwarn(str(movement))
            self.gurdy_mover.execute_movement_gurdy(movement)

    def start_behaviour(self, behaviour):

        while not rospy.is_shutdown():
            self.choose_behaviour(behaviour)