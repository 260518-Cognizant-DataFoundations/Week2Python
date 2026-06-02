# Matplotlib is a data visualization library that lets us make different types of charts

# pyplot is mayplotlib module that lets us easily create charts
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] # defining our x axis
y = [10, 20, 30, 40, 50] # defining our y axis

plt.plot(x, y, linestyle="--", color="forestgreen", marker="o") # plot() creates the chart
plt.title("Hello World Chart", fontsize=32, fontweight="bold")
plt.xlabel("Months")
plt.ylabel("Potatoes Eaten")
plt.grid(True, alpha=0.5) # alpha adjusts transparency
plt.show() # show() shows the chart

"""
Remember, this ^ could have been as simple as just:
plt.plot(x, y)
plt.show()

But there are a TON of options to customize charts. Look into them!
"""

# Doing a bar chart now -

types_of_potatoes = ["Russet", "Fingerling", "Yukon Gold"]
potatoes_eaten = [400, 200, 515]

plt.bar(types_of_potatoes, potatoes_eaten, color=["saddlebrown", "goldenrod", "peru"])
plt.title("Potatoes Eaten")
plt.xlabel("Types of Potatoes")
plt.ylabel("Number Eaten")
plt.show()