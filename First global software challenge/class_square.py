# creating class for each individual square
from robot_variables import var_up, var_down, angle_down_uncertainty,angle_up_uncertainty
class Square:

    def __init__(self, location_x, location_y):
        # addresing from for loops to individual cells
        self.x = str(location_x)
        self.y = str(location_y)
        # creating boolean values for each cell
        self.true_up = False
        self.true_down = False
        self.true_left = False
        self.true_right = False
        self.puck = False
        self.clean = False
        self.bluefinish = False
        self.redfinish = False

    def grid_location(self):
        print(self.x, self.y)
        return self.x, self.y

    def write_possible_moves(self, angle, up, left, right, back):
        if angle_down_uncertainty < angle < angle_up_uncertainty:
            self.true_up = up
            self.true_left = left
            self.true_right = right



    def check_if_clean(self):
        return self.clean

    def is_clean(self, clean):
        self.clean = clean
        print(f"is clean: {self.clean}, grid: {self.x} {self.y}")

    def read_possible_moves(self):
        return self.true_up, self.true_down, self.true_left, self.true_right


    # changing representation
    def __repr__(self):
        return f"""Square positions: {self.x} , {self.y} 
        up:{self.true_up}, down:{self.true_down}, left:{self.true_left},
        right:{self.true_right}, clean: {self.clean}
        red-finish {self.redfinish}, blue-finish {self.bluefinish} 
        
        
        """
