import numpy as np
import matplotlib.pyplot as plt

# Set plotting settings
plt.rcParams['figure.figsize'] = (16, 8)
plt.rcParams['axes.facecolor'] = 'none'  # Transparent axes background
plt.rcParams['savefig.facecolor'] = 'none'  # Transparent figure background

# Generate data
np.random.seed(0)
mu, sigma = 0, 1  # Mean and standard deviation
x = np.random.normal(mu, sigma, 1000)
cum_sum = np.cumsum(x)
sample_size = np.arange(1, len(x) + 1)
averages = np.divide(cum_sum, sample_size)

# Create plot
fig, ax = plt.subplots()
ax.set_xlabel('Size of a Sample', fontsize=16)
ax.set_ylabel('Average', fontsize=16)
ax.axhline(0, ls='-', c='blue', label='Mean')

# Plot red line as dots
ax.plot(sample_size, averages, 'ro', markersize=3, alpha=0.7, label='Sample Average')

# Legend settings
ax.legend(loc="upper right", frameon=False, prop={'size': 14})

# Set transparent background
fig.patch.set_alpha(0)  # Transparent figure background
ax.patch.set_alpha(0)  # Transparent axis background

# Title
plt.title('Law of Large Numbers', fontsize=20)

# Show plot
plt.show()
