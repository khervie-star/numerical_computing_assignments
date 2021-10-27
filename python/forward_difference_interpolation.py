import math
import time
import numpy as np

i = 1
sm = 0
n = eval(input("Enter number of tabulated points 'n': "))
X = eval(input("Enter point of interpolation: "))

print("Enter coordinates (x, y): ")

x_coordinates = []
y_coordinates = []


for val in range(1, n+1):
    x_coordinates.append(eval(input("Enter x("+str(val)+"): ")))
    print(x_coordinates)
for i in range(3):
    print("************************************************************************************")

for val in range(1, n+1):
    y_coordinates.append(eval(input("Enter y("+str(val)+"): ")))
    print(y_coordinates)
    
print("x coordinates from x(1) to x(" + str(n) + ") :", x_coordinates)
print("y coordinates from y(1) to y(" + str(n) + ") :", y_coordinates)

i = 1
# while (X > x_coordinates[i-1]):
#     i = i + 1
#     k = i - 1
#     print(k)

z = (X - x_coordinates[i-1]) / (x_coordinates[i] - x_coordinates[i-1])
print(z)



# for i in range(1,n+1):
#     for j in range(0,n-i):
#         y_coordinates[j][i] = y_coordinates[j+1][i-1] - y_coordinates[j][i-1]

# print(y_coordinates)

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

