#!/usr/bin/env python

import rospy
from gurdy_behaviour import GurdyBehaviour

#Two scipts that start different behaviours. 
#One jumps when its upright and flips when gurdy has fallen. And the second just detects that it has fallen and gets upright again.
def start_jump_behaviour_behaviour():
    # We Start Here
    rospy.init_node('jump_behaviour_node')
    gurdy_bhv = GurdyBehaviour()
    gurdy_bhv.start_behaviour(behaviour="jump")


if __name__ == "__main__":
    start_jump_behaviour_behaviour()