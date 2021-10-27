import math
import numpy as np


def forward_difference_interpolation():
    i = 1
    sm = 0
    n = eval(input("Enter number of tabulated points 'n': "))
    X = eval(input("Enter point of interpolation: "))

    print("Enter coordinates (x, y): ")

    x_coordinates = np.zeros((n))
    y_coordinates = np.zeros((n))

    print('Enter data for x and y: ')
    for i in range(n):
        x_coordinates[i] = float(input( 'x['+str(i+1)+']='))
        y_coordinates[i] = float(input( 'y['+str(i+1)+']='))
        
    print("x coordinates from x(1) to x(" + str(n) + ") :", x_coordinates)
    print("y coordinates from y(1) to y(" + str(n) + ") :", y_coordinates)

    i = 1
    # while (X > x_coordinates[i-1]):
    #     i = i + 1
    #     k = i - 1
    #     print(k)

    z = (X - x_coordinates[i-1]) / (x_coordinates[i] - x_coordinates[i-1])
    print(z)


    fd = np.zeros((n,n))

    for j in range(1, n):
        for i in range(0, n-j):
            if ( j == 1):
                fd[i][j-1] = y_coordinates[i+1] - y_coordinates[i]
            else:
                fd[i][j-1] = fd[i+1][j-2] - fd[i][j-2]
    print("The forward difference table is: ")
    print(fd)


    sm = y_coordinates[0]

    print(sm)

    for i in range(1, n):
        product = 1
        for j in range(i):
            product *= (z - j)
        m = math.factorial(i)
        sm += fd[0][i-1] * (product / m)
    print(sm)

    print('Interpolated value of X('+str(X)+') is: ' + str(sm))
    


if __name__ == "__main__":
    forward_difference_interpolation()