#!/usr/bin/env python
import rospy 
import rospkg
from math import pi
from geometry_msgs.msg import Pose, Quaternion
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
from tf.transformations import quaternion_from_euler

def main():
    rospy.init_node('set_pose')

    state_msg = ModelState()
    state_msg.model_name = 'jetbot'
    state_msg.pose.position.x = 0
    state_msg.pose.position.y = 0
    state_msg.pose.position.z = 0
    state_msg.pose.orientation = Quaternion(*quaternion_from_euler(0.0, 0.0, 90*pi/180))
    state_msg.twist.linear.x = 0 
    state_msg.twist.linear.y = 0
    state_msg.twist.linear.z = 0
    state_msg.twist.angular.x = 0
    state_msg.twist.angular.y = 0
    state_msg.twist.angular.z = 0
    state_msg.reference_frame = 'world'
    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass