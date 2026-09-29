from matplotlib import pyplot as plt


def Bresenham(X1, X2, Y1, Y2):

    dX = X2 - X1
    dY = Y2 - Y1

    # Initial decision parameter
    P = 2 * dY - dX

    # Initialize value of X and Y
    X = X1
    Y = Y1

    # Store points for plotting
    x_coordinates = []
    y_coordinates = []

    # Repeat until we reach the end point
    while X <= X2:

        x_coordinates.append(X)
        y_coordinates.append(Y)

        # Case I
        if P < 0:
            X = X + 1
            Y = Y
            P = P + 2 * dY

        # Case II
        else:
            X = X + 1
            Y = Y + 1
            P = P + 2 * dY - 2 * dX

    # Show coordinates of the points
    print("Coordinates of the points:")

    for i in range(len(x_coordinates)):
        print(f"Point {i + 1}: ({x_coordinates[i]}, {y_coordinates[i]})")

    # Plotting the points
    plt.plot(x_coordinates, y_coordinates, marker='.')
    plt.show()


#Example usage

#User inputs for the coordinates of the two points
print("Enter the coordinates of the first point (X1, Y1):")
X1 = int(input("X1: "))
Y1 = int(input("Y1: "))

print("Enter the coordinates of the second point (X2, Y2):")
X2 = int(input("X2: "))
Y2 = int(input("Y2: "))

Bresenham(X1, X2, Y1, Y2)