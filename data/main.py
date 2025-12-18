# run this in terminal to download the dataset
#kaggle datasets download camnugent/california-housing-prices
import pandas as pd
df = pd.read_csv('housing.csv')
df = df[['latitude', 'longitude']]
df.to_csv('points.csv')