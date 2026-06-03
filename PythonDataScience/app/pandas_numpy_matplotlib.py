"""
Ok we had lots of fun playing around with hardcoded data

But let's use a "real" .csv dataset and use all 3 technologies we've learned

We'll start by finally using a Pandas dataframe to load and manipulate the real data
Then use Numpy to do some calculations to use in our chart
And visualize the data with Matplotlib!
"""

import pandas as pd

# GOAL: Visualize monthly sales trends by product
# TODO: There's a lot more data in the dataset! You can make your own calcs and charts

# Load in the CSV data into a Pandas DataFrame
df = pd.read_csv("data/sales_data.csv")

# Peek at what we loaded in
print(df.head()) # See the first 5 records
print(df.info()) # General info like datatypes and mem usage
print(df.shape) # (# of rows, # of columns)
print(df.columns) # Column names
print(df.dtypes) # Datatypes of each column
print(df.describe()) # Summary stats

"""
PANDAS DATA CLEANING

We need to "clean up" the data
-One record has N/A for the product name
-A few records have a negative number for units sold
"""

# Filtering the dataframe to only include rows where "product" is not null
df = df[df["product"].notna()]

# Replacing values in the dataframe to turn negative units sold into 0
# TODO: Is setting 0 the best way to handle this? Depends on why the values are negative...
df["units_sold"] = df["units_sold"].clip(lower=0) # values will be 0 AT LOWEST

# Proof of na filtering and negative number cleaning
print(df.head()) # That record with na is gone! No more negative values for units sold!

"""
PANDAS DATA TRANSFORMATION

The data is "clean" now, but we'd like to reformat it to help with our analysis
Right now each row is one product/region/month combo
But we want total units sold per product per month!!

groupby() groups rows together! We'll see it below
"""

# Use groupby() to get sales per product per month
# reset_index is necessary to turn the groupby object back into a dataframe
monthly_product_sales = df.groupby(["month", "product"])["units_sold"].sum().reset_index()

print(type(monthly_product_sales)) # It's a dataframe!

# Isolate each type of product into its own variable (more visibility, easier plotting)
laptops = monthly_product_sales[monthly_product_sales["product"] == "Laptop"].reset_index()
headphones = monthly_product_sales[monthly_product_sales["product"] == "Headphones"].reset_index()
keyboards = monthly_product_sales[monthly_product_sales["product"] == "Keyboard"].reset_index()

print("===== Monthly Product Sales =====")
print(monthly_product_sales)

print("~~~~~ Laptop Sales ~~~~~")
# Print without the product name column
print(laptops[["month", "units_sold"]]) # "Only include these columns"

print("~~~~~ Headphones Sales ~~~~~")
print(headphones[["month", "units_sold"]])

print("~~~~~ Keyboard Sales ~~~~~")
print(keyboards[["month", "units_sold"]])
