#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

#create and init a pthon node called cylinder_input
rospy.init_node("cylinder_input")

#create a publisher that publishes on the "radius" topic and store it in radius_pub variable
#the message type is a float64 from the standard msg library with a queue size of 10
radius_pub 	= rospy.Publisher("/radius", Float64, queue_size=10)
#create a publisher that publishes on the "height" topic and store it in height_pub variable
#the message type is a float64 from the standard msg library with a queue size of 10
height_pub 	= rospy.Publisher("/height", Float64, queue_size=10)
#create a publisher that publishes on the "density" topic and store it in density_pub variable
#the message type is a float64 from the standard msg library with a queue size of 10
density_pub = rospy.Publisher("/density", Float64, queue_size=10)


#get the radius and height from the user
radius 	= float(input("Enter radius: "))
height 	= float(input("Enter height: "))
density = float(input("Enter density: "))


#publish height, radius, and density as long as the ros master is open and running
#it is published at a rate of 10Hz as teh rospy.sleep command causes the loop to pause for .1 seconds.
while not rospy.is_shutdown():
	radius_pub.publish(radius)
	height_pub.publish(height)
	density_pub.publish(density)
	rospy.sleep(0.1)
