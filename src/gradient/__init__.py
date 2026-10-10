import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x): #f(x)=x^2
    return x**2

x_values = np.linspace(-10, 10, 100)
y_values = f(x_values)

start_x_point = -5
start_y_point = f(start_x_point)

learning_rate=

def main() -> None:
    figure, axis = plt.subplots()

    dydx = np.gradient(y_values) # when i have one variable, i only need differentiation instead of partial differentiation
    # gradient.gradient_descent_iteration()

    #--plot graph--
    axis.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gradient Descent Visualization")
    #--------------

    #--plot point modeled by gradient descent--

    point, = axis.plot([start_x_point],[start_y_point], marker="*", markersize=15, color="red")

    x_point = start_x_point

    def update(frame):
        nonlocal x_point

        for _ in range(5): #its too slow 😂
            x_point = gradient_descent_iteration(np.interp(x_point,x_values,dydx), x_point)
            y_point = f(x_point)
        point.set_data([x_point],[y_point])

        return point,

    ani = FuncAnimation(
        figure,
        update,
        interval=0.1,
        blit=True
    )

    #------------------------------------------

    plt.show()

def gradient_descent_iteration(dydx, x, learning_rate=1e-3):
    #detect if left or right
    gradient = x-learning_rate*dydx #x_n = x_(n-1)+alpha*∇y, for 1 input, ∇x = dy/dx
    return gradient

main()