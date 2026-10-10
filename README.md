### The gradient descent function for a single variable is defined by the formula:

$$
x_{n}=x_{n-1}-{\alpha}f'(x_{n-1})
$$

### Where:
- $n$ is the current frame
- $x_{n-1}$ is the last value of the input variable x;
- $x_{n}$ is the updated or new value of the input variable x, iterating $n$ by 1
- $\alpha$ (optional) is the rate at the which the gradient changes x; used to find the relative minimum of loss functions in ML
- $f'(x_{n-1})$ is the derivative of the function f(x) at $x_{n-1}$. This represents the slope at that point.

### How It Works:
- We want $x_{n}$ to reach the relative minimum, so we want each iteration of n to make the y value fall towards that minimum.
- ${\alpha}f'(x_{n-1})$, or the slope multiplied by a small number, is subtracted from $x_{n-1}$; if we added it, then the x value would go away instead of towards the midpoint, and the y value would go up instead of down.

### The whole process can be described in Python as
```python
x_point = x_point - learning_rate * np.gradient(y_values)
```

### Then we could bring that into a loop.
### Using matplotlib:
```python
from matplotlib.animation import FuncAnimation

figure, axis = plt.subplots() # figure is the container of the elements on the page. axis has all the data. Use axis if putting data into the graph.

ani = FuncAnimation(
  figure,
  update, # where update is a function that updates x_point once. x_point is an arbitrary starting number.
  interval=interval,
  blit=True
)
```

<sub>2026 MS.</sub>
