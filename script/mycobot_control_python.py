#!/usr/bin/env python

import rospy  
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import random


def publisher_control():
    rospy.init_node('mycobot_control_python_node')
    control_publisher = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    
    while not rospy.is_shutdown():
        msg = JointTrajectory()   
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names =['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        
        point = JointTrajectoryPoint()
        j1 = random.random()
        j2 = random.random()
        j3 = random.random()
        j4 = random.random()
        j5 = random.random()
        j6 = random.random()
        point.positions = [j1, j2, j3, j4, j5, j6]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)
        
        msg.points.append(point)
        
        control_publisher.publish(msg)
        
        rospy.loginfo(msg)

    



if __name__ == '__main__':
    publisher_control()        

