import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Define parameters
lambda_val = 4    # Average number of events per interval
size = 10000      # Number of intervals (samples)

# STEP 2: Generate Poisson-distributed data
data = np.random.poisson(lam=lambda_val, size=size)
"""
lam → λ (mean number of events per interval)

size → how many such intervals to simulate

"""

# STEP 3: Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=np.arange(data.min(), data.max() + 1) - 0.5, 
         density=True, color='mediumpurple', edgecolor='black', rwidth=0.8)

# STEP 4: Labels and decorations
plt.title(f'Poisson Distribution (λ = {lambda_val})', fontsize=16)
plt.xlabel('Number of Events per Interval', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.xticks(range(data.min(), data.max() + 1))
plt.grid(True)
plt.show()
