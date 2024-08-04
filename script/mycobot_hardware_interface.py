#!/usr/bin/env python

import time
import math
import rospy
from sensor_msgs.msg import JointState
from pymycobot.mycobot import MyCobot

mc = None

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "%s", data.position)
    
    data_list =[]
    for index, value in enumerate(data.position):
        radians_to_angles = round(math.degrees(value), 2)
        data_list.append(radians_to_angles)
        
    rospy.loginfo(rospy.get_caller_id() + "%s", data_list)
    mc.send_angles(data_list, 25)
    
def listener():
    global mc
    rospy.init_node("myCobot_hardware_interface", anonymous=True)
    
    rospy.Subscriber("joint_states", JointState, callback)
    port = rospy.get_param("~port", "/dev/ttyUSB0")
    baud = rospy.get_param("~baud", 115200)
    print(port, baud)
    mc = MyCobot(port, baud)
    time.sleep(0.05)
    mc.set_fresh_mode(1)
    time.sleep(0.05)
    
    print("spin ...")
    rospy.spin()
    
if __name__ == "__main__":
    listener()