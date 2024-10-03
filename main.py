# Programmers: Cody and Laure
# Course: CS151
# Due Date: 10/2/2024
# Lab Assignment: Lab 3
# Problem Statement: What type of speed does a jumper need to achieve on the ramp to make good distance on their jump
# Data In: hill type, jumper speed
# Data Out: points, distance traveled
# Credits:This code is based on the example we were given on github
import math

#the purpose of this lab is to use if, elif, and else statements to solve formulas with different variables

#Create the variables and set each current value to zero
height = 0
par = 0
points_per_meter = 0

#Ask user to input the hill type
hill_type = input('Is the hill type normal or large?')
if hill_type == 'normal':
    height = 46
    par = 90
    points_per_meter = 2
elif hill_type == 'large':
    height = 70
    par = 120
    points_per_meter = 1.8
else:
    print('Invalid hill type')

#Ask user to input the jumper's speed at the end of the ramp
jumper_speed = float(input('What is the jumper''s speed at the end of the ramp in meters per second?'))

#Calculate the time in the air
time_in_air = float(math.sqrt((2 * height) / 9.8))

#Calculate the distance traveled
distance = float(jumper_speed * time_in_air)

#Calculate the total points earned
total_points = float(60 + (distance - par) * points_per_meter)

#output response to user
if total_points >= 61:
    print( "Great job for doing better than par!")
elif total_points < 10:
    print("What happened??")
else:
    print("Sorry, you didn't go far")

#Output distance and total points to user

print('Distance:' + str(distance))
print('Total points:' + str(total_points))

