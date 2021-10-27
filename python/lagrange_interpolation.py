import math
import time

def main():
    i = 1
    sm = 0
    n = eval(input("Enter number of tabulated points 'n': "))
    X = eval(input("Enter point of interpolation: "))

    print("Enter coordinates (x, y): ")

    x_coordinates = []
    y_coordinates = []

#Takes our input values of both x and y coordinates
    for val in range(1, n+1):
        x_coordinates.append(eval(input("Enter x("+str(val)+"): ")))
        print(x_coordinates)
        time.sleep(.3)
    for i in range(3):
        print("************************************************************************************")
        time.sleep(.3)

    for val in range(1, n+1):
        y_coordinates.append(eval(input("Enter y("+str(val)+"): ")))
        print(y_coordinates)
        time.sleep(.3)
    print("x coordinates from x(1) to x(" + str(n) + ") :", x_coordinates)
    print("y coordinates from y(1) to y(" + str(n) + ") :", y_coordinates)

    print('')
    time.sleep(.5)


#Interpolation code according to algorithm given

    print("******************STARTING ITERATION/ INTERPOLATION ********************")
    for i in range(2):
        print("************************************************************************************")
        time.sleep(.4)
    print('')

    
    for i in range(1, n+1):
        pr = 1
        for j in range(1, n+1):
            if (i != j):
                pr = pr * ((X - x_coordinates[j-1]) / (x_coordinates[i-1] - x_coordinates[j-1]))
                print("product = ", pr)
                time.sleep(.25)
            time.sleep(.5)
        sm = sm + y_coordinates[i-1] * pr
        print("sum = ", sm)

        for i in range(2):
            print("************************************************************************************")
            time.sleep(.4)

#This outputs our final answer
    print("The Interpolated value of y at X(" +str(X)+ ") is now: " + str(sm))
    

if __name__ == "__main__":
    main()
