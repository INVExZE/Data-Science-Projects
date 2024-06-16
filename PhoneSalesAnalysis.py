import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go


sanjaydata = pd.read_csv("apple_products.csv")
print(sanjaydata.head()) 
print(sanjaydata.describe())
print(sanjaydata.isnull().sum())

highestRated = sanjaydata.sort_values(by = ["Star Rating"], ascending = False)
highestRated = highestRated.head(10)
print(highestRated['Product Name'])
iphone = highestRated['Product Name'].value_counts()
label = iphone.index
counts = highestRated["Number Of Ratings"]

figure = px.bar(highestRated, x = label , y = counts, title = "Number of ratings of highest Rated Iphone")

figure.show()

figure=px.scatter(data_frame=sanjaydata, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between Discount Percentage and number of ratings of iphones")
figure.show()

 



