import matplotlib.pyplot as plt
import numpy as np


# Define logistic map function
def logistic_map(r, x0, n):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x


# Parameters for bifurcation diagram
r_values = np.linspace(1, 4, 10000)  # Range of r values
n_skip = 100  # Skip initial transients
n_collect = 50  # Collect stable values after transients
x0 = 0.5  # Initial condition

x_vals = []
r_vals = []

# Generate bifurcation data
for r in r_values:
    x = logistic_map(r, x0, n_skip + n_collect)
    x_vals.extend(x[-n_collect:])  # Collect stable values only
    r_vals.extend([r] * n_collect)

# Plotting the bifurcation diagram
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.plot(r_vals, x_vals, ",k", alpha=0.6)  # Pixel marker for density
ax.set_xlabel("Growth Rate (r)")
ax.set_ylabel("Population (x)")
ax.set_title("Bifurcation Diagram of the Logistic Map")
ax.grid(True)  # Show grid


# Function to show x and y coordinates on click
def on_click(event):
    if event.inaxes == ax:  # Check if the click is within the plot area
        x, y = event.xdata, event.ydata
        print(f"Clicked coordinates: r = {x:.4f}, x = {y:.4f}")


# Connect the click event to the on_click function
fig.canvas.mpl_connect("button_press_event", on_click)

# Display the plot in an interactive window
plt.show()
