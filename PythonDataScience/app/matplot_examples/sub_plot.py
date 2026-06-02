# subplots - multiple charts in a single figure

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 20, 30, 40, 50]
returns = [1, 2, 3, 4, 5]

# Create a figure (the window with our charts) with 1 row and 2 columns of charts
# Figsize() is the size of the figure in inches
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Each ax (axis) is its own chart in the figure

ax1.plot(months, sales, marker="o", color="blue")
ax1.set_title("Monthly Sales")
ax1.set_xlabel("Month")
ax1.set_ylabel("Units Sold")

ax2.plot(months, returns, marker="x", markerfacecolor="green",
         markeredgecolor="limegreen", color="red")
ax2.set_title("Monthly Returns")
ax2.set_xlabel("Month")
ax2.set_ylabel("Units Returned")

plt.tight_layout() # Automatically adjusts spacing between subplots

plt.show()