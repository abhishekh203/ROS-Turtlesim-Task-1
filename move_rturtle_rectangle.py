#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time


def move_turtle_rectangle():
    rospy.init_node("move_turtle_rectangle_node", anonymous=True)
    velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)

    vel_msg = Twist()
    linear_speed = 1.0  # Speed for straight movement
    angular_speed = 1.57  # Approximate speed for a 90-degree turn (1.57 radians)

    # Rectangle dimensions (length and width)
    length_time = 2.0  # Time in seconds for moving along the length
    width_time = 1.0  # Time in seconds for moving along the width

    rospy.loginfo("Moving the turtle in a rectangle...")

    while not rospy.is_shutdown():
        # Move forward along the length
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        time.sleep(length_time)

        # Turn 90 degrees
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = angular_speed
        velocity_publisher.publish(vel_msg)
        time.sleep(1.0)  # Time to turn approximately 90 degrees

        # Move forward along the width
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        time.sleep(width_time)

        # Turn 90 degrees again
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = angular_speed
        velocity_publisher.publish(vel_msg)
        time.sleep(1.0)  # Time to turn approximately 90 degrees


if __name__ == "__main__":
    try:
        move_turtle_rectangle()
    except rospy.ROSInterruptException:
        pass
