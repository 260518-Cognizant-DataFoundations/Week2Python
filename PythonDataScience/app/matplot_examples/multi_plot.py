# We can easily show multiple lines in one line chart
# It's as simple as calling multiple plot() functions before show()

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
air_fryers = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650] # upward trend
toasters = [650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100] # downward trend
blenders = [300, 320, 310, 330, 290, 350, 370, 360, 340, 380, 390, 410] # mixed bag
