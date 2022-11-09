# Add your own tests here
import math

# fill in this function to return the distance between the two points!
def distance(first_point, second_point):
    # point_1= (8, 9)
    # point_2= (5, 4)
    number_x = second_point[0] - first_point[0]
    number_y = second_point[1] - first_point[1]
    square_x = pow(number_x,2)
    square_y = pow(number_y,2)
    result = square_x + square_y
    answer = math.sqrt(result)
    return answer

print(distance((4, 7),(3, 6)))