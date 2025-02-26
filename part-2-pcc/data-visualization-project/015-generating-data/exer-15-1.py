"""
15-1. Cubes: A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5000 cubic numbers.
"""

import matplotlib.pyplot as plt

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

five_nums = list(range(1,6))
five_t_nums = list(range(1,5001))

five_cubes = [num**3 for num in five_nums]
five_t_cubes = [num**3 for num in five_t_nums]

# First subplot for first 5 numbers
ax1.scatter(five_nums, five_cubes, s=50)
ax1.set_title('Cubes of First 5 Numbers', fontsize=12)
ax1.set_xlabel('Numbers')
ax1.set_ylabel('Cubes')

# Second subplot for first 5000 numbers
ax2.scatter(five_t_nums, five_t_cubes, s=5)
ax2.set_title('Cubes of First 5000 Numbers', fontsize=12)
ax2.set_xlabel('Numbers')
ax2.set_ylabel('Cubes')

# Adjust layout and display
plt.tight_layout()
plt.show()