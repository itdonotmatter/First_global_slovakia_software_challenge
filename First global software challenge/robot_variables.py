# check where is the point at which the robot turns in contrast to the position of the sensors
distance_to_middle_of_square = 22.5

# distance front, side sensors must read in order for the center of rotation to be above the middle of the square
middle_sens_to_w = distance_to_middle_of_square - 3
right_sens_to_w = distance_to_middle_of_square - 7
left_sens_to_w = distance_to_middle_of_square - 7
blue_pucks = 3
red_pucks = 3
var_up = 1.1
var_down = 0.9
current_square = 0
angle_down_uncertainty = -9
angle_up_uncertainty = 9
# squares storing their informations in one list
info_square = []
