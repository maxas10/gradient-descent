def gradient_descent_iteration(dydx, x, rate=0.5):
    #detect if left or right
    gradient = rate*dydx #x_n = x_(n-1)+alpha*∇x, for 1 input, ∇x = dy/dx
    new_x = x-gradient
    return new_x