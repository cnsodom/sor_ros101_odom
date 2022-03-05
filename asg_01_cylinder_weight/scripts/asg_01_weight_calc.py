#!/usr/bin/env python
import rospy
from std_msgs.msg 		import Float64
from asg_01_cylinder_weight.msg 	import Cylinder

volume 			= 0
density			= 0

density_found   = False
volume_found	= False

def density_callback(data):
	global density
	global density_found
	density			= data.data
	density_found 	= True

def cylinder_callback(data):
	global volume
	global volume_found
	volume 			= data.volume
	volume_found 	= True

def calculate():
	if density_found and volume_found:
		weight = 9.807 * density * volume
		density_pub.publish(weight)

rospy.init_node("weight_calc")
rospy.Subscriber("/density",Float64,density_callback)
rospy.Subscriber("/cylinder",Cylinder,cylinder_callback)

density_pub = rospy.Publisher("/weight",Float64,queue_size=10)

while not rospy.is_shutdown():
	calculate()
	rospy.sleep(0.1)
