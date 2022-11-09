def calculate_area(side_length= 10):
    print("Side length: "+ str(side_length) + " units")
    print("Area: " +  str(side_length ** 2) + " units square")

side_length = int(input("Enter side length: "))
if side_length > 0:
    calculate_area(side_length)
    area = side_length ** 2
    print("The area of a square with sides of length " + str(side_length) + " is " +str(area) +".")
else:
    calculate_area(10)
    print("The area of a square with sides of length 10 is 100.")