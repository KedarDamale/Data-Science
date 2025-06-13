import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Define parameters
n = 10          # Number of trials per experiment (e.g. flipping a coin 10 times)
p = 0.5         # Probability of success (e.g. getting heads)
size = 10000    # Number of experiments

# STEP 2: Generate binomially distributed data
data = np.random.binomial(n=n, p=p, size=size)
#np.random.binomial(n=trials, p=probability, size=N)

# STEP 3: Visualize the distribution using histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=np.arange(data.min(), data.max()+2)-0.5, 
         density=True, color='skyblue', edgecolor='black', rwidth=0.8)

# STEP 4: Plot details
plt.title(f'Binomial Distribution: n={n}, p={p}', fontsize=16)
plt.xlabel('Number of Successes', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.xticks(range(data.min(), data.max()+1))
plt.grid(True)
plt.show()
