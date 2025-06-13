import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Set parameters
df = 4          # degrees of freedom
size = 10000    # number of random samples

# STEP 2: Generate Chi-Square distributed data
data = np.random.chisquare(df=df, size=size)
"""
df: degrees of freedom (k)

size: number of samples

"""

# STEP 3: Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, density=True, color='cornflowerblue', edgecolor='black')

# STEP 4: Titles and labels
plt.title(f'Chi-Square Distribution (df = {df})', fontsize=16)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Probability Density', fontsize=14)
plt.grid(True)
plt.show()
