import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Define parameters of the distribution
mean = 0       # Center of the distribution (μ)
std_dev = 1    # Spread of the distribution (σ)
size = 10000   # Number of samples

# STEP 2: Generate normally distributed data using NumPy
data = np.random.normal(loc=mean, scale=std_dev, size=size)

# loc → μ (mean)

# scale → σ (standard deviation)

# size → number of data points


# STEP 3: Plot histogram and overlay actual PDF curve
plt.figure(figsize=(10, 6))

# Histogram: density=True normalizes the histogram
count, bins, ignored = plt.hist(data, bins=50, density=True, color='lightblue', edgecolor='black', alpha=0.7, label="Sampled Data Histogram")

# STEP 4: Plot theoretical PDF
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp( - (bins - mean)**2 / (2 * std_dev**2) )
plt.plot(bins, pdf, color='red', linewidth=2, label='Theoretical PDF')

# STEP 5: Decorations
plt.title('Normal Distribution (Gaussian Curve)', fontsize=16)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Probability Density', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
