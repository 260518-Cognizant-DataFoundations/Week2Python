# We can easily show multiple lines in one line chart
# It's as simple as calling multiple plot() functions before show()

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
air_fryers = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650] # upward trend
toasters = [650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100] # downward trend
blenders = [300, 320, 310, 330, 290, 350, 370, 360, 340, 380, 390, 410] # mixed bag

plt.plot(months, air_fryers, label="Air Fryers") # Label helps us create a Legend
plt.plot(months, toasters, label="Toasters")
plt.plot(months, blenders, label="Blenders")
# Notice that it chooses default colors! We can still change them though

# This takes our labels above, and makes our legend for us!
# We'll put the label on the bottom right outside the plot area
plt.legend(bbox_to_anchor=(1, 0))

plt.title("Monthly Sales of Kitchen Appliances")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.show()
