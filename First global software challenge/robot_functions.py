#!/usr/bin/env python3

from ev3dev2.button import Button
# Import the necessary libraries
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *
from ev3dev2.sound import Sound

from robot_variables import *
from class_square import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()

color_sensor_in1 = ColorSensor(INPUT_1)

# middle sensor
ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)

# left sensor
ultrasonic_sensor_in3 = UltrasonicSensor(INPUT_3)

# right sensor
ultrasonic_sensor_in4 = UltrasonicSensor(INPUT_4)

gyro_sensor_in5 = GyroSensor(INPUT_5)

motorC = LargeMotor(OUTPUT_C)  # Magnet


# nice would also be a function which allowes me to just input the distance i want to travel converts it into
# degrees and just moves that distance
def initial_position():
    speed = -20
    while ultrasonic_sensor_in2.distance_centimeters < middle_sens_to_w:
        tank_drive.on(speed, speed)
    else:
        tank_drive.off(brake=True)


# creates grip upon which will the robot move
def createsquares():
    for x in range(8):
        for y in range(8):
            # adding this cell to the list of cells
            square = Square(x, y)
            if x == 0 and y == 0:
                square.clean = True
            if y == 7 and x == 0:
                square.redfinish = True
                square.clean = True
                print("red finish:", square.redfinish)
            if x == 7 and y == 0:
                square.bluefinish = True
                square.clean = True
                print("blue finish:", square.bluefinish)
            info_square.append(square)
    print(info_square)


# motorA.off(brake=True)
# tank_drive.on(100, 100)
# tank_drive.on_for_rotations(20, 20, 1)
# gyro_sensor_in5.angle
# motorA.position in degrees
# ultrasonic_sensor_in4.distance_centimeters
# color_sensor_in1.rgb[1] and color_sensor_in1.rgb[0]

# scan for possible moves
def scan():
    # variables
    red = color_sensor_in1.rgb[0]
    blue = color_sensor_in1.rgb[2]
    middle_sensor = ultrasonic_sensor_in2.distance_centimeters
    left_sensor = ultrasonic_sensor_in3.distance_centimeters
    right_sensor = ultrasonic_sensor_in4.distance_centimeters

    # check for additional possible paths
    if middle_sensor:
        pass

    # checks whether bot is standing above a puck
    if red == 255:
        return_red_puck()
    elif blue == 255:
        return_blue_puck()

    print(info_square[0].grid_location())
    print(info_square[0].write_possible_moves())

    # function to move from set square into another square upfront, back


def front_move():
    pass


def back_move():
    pass


# functions to move from set square into another square left, right
def right_move():
    pass


def left_move():
    pass


def magnet():
    pass


def return_blue_puck():
    pass


def return_red_puck():
    pass
