from matplotlib import pyplot as plt

def DDA(X1, X2, Y1, Y2):
    dX = abs(X2 - X1)
    dY = abs(Y2 - Y1)

    # Step size
    steps = max(dX, dY)


    # Calculate increment in X and Y
    Xinc = dX / steps
    Yinc = dY / steps

    # Initialize value of X and Y
    X = float(X1)
    Y = float(Y1)

    # Store points for plotting
    x_coordinates = []
    y_coordinates = []

    for i in range(steps):
        x_coordinates.append(round(X))
        y_coordinates.append(round(Y))
        X += Xinc
        Y += Yinc


    # show coordinates of the points
    print("Coordinates of the points:")
    for i in range(steps):
        print(f"Point {i + 1}: ({x_coordinates[i]}, {y_coordinates[i]})")

    # Plotting the points
    plt.plot(x_coordinates, y_coordinates, marker='.')
    plt.show()



# Example usage
# user inputs for the coordinates of the two points
print("Enter the coordinates of the first point (X1, Y1):")
X1 = int(input("X1: "))
Y1 = int(input("Y1: "))

print("Enter the coordinates of the second point (X2, Y2):")
X2 = int(input("X2: "))
Y2 = int(input("Y2: "))

DDA(X1, X2, Y1, Y2)
