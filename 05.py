'''
Created by Roman Beya
Created on 6-nov-2017
Created for ICS3U
This program calculates the volume of a cylinder!
'''

# Declaring Constants
PI = 3.1415926535897932384626433832

def calculate_volume_of_cylinder(radius, height):
	# this calculates the volume of a cylinder given the radius and height, inputted into the console
	
	# Use volume formula 2 * PI * radius ^ 2 * height
	volume_of_cylinder = 2 * PI * radius ** 2 * height
	
	# return result to user
	return volume_of_cylinder
	
radius_of_cylinder = input("Enter the radius: ")
height_of_cylinder = input("Enter the height: ")
volume = calculate_volume_of_cylinder(radius_of_cylinder, height_of_cylinder)
print volume
