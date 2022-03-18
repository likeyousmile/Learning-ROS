cmake_minimum_required(VERSION 2.8.3)
project(actions_quiz)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib_msgs
)

add_action_files(
  DIRECTORY action
  FILES 
  CustomActionMsg.action
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES actions_quiz
 CATKIN_DEPENDS rospy actionlib_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)