import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set Seaborn's styling
sns.set_theme()

# Generate a range of x values
x = np.linspace(0, 10, 500)

# Compute the sine of each x value
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Customize the plot
plt.title('Sine Graph')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Display the plot
plt.show()