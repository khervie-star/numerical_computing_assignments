import time

def lagrange_interpolation():
    i = 1
    sm = 0
    n = eval(input("Enter number of tabulated points 'n': "))
    X = eval(input("Enter point of interpolation: "))

    print("Enter coordinates (x, y): ")

    x_coordinates = []
    y_coordinates = []

    for i in range(1, n+1):
        x_coordinates.append(float(input( 'x['+str(i)+']=')))
        y_coordinates.append(float(input( 'y['+str(i)+']=')))



    for i in range(1, n+1):
        pr = 1
        for j in range(1, n+1):
            if (i != j):
                pr = pr * ((X - x_coordinates[j-1]) / (x_coordinates[i-1] - x_coordinates[j-1]))
                print('pr: ' + str(pr))
                time.sleep(.5)
                print("*******************")
            time.sleep(.35)
        sm = sm + y_coordinates[i-1] * pr
    
    print("The Interpolated value of y at X(" +str(X)+ ") is now: " + str(sm))
    

if __name__ == "__main__":
    lagrange_interpolation()
