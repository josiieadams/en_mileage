import pandas as pd
import numpy as np
from geopy.distance import great_circle
from geopy.point import Point
from os import listdir

# allfiles = listdir(path='C:/Users/16308/Coding/en_mileage/csv_files/')
# filepath = "C:/Users/16308/Coding/en_mileage/csv_files/EN001_EN673.csv"

# dataframe = pd.read_csv(filepath, dtype = {"cruise": str, "lat": float, "lon": float})
#dataframe = pd.read_csv(filepath, names=["cruise", "lat", "lon"])
# df = pd.DataFrame(dataframe)
        
#df["cruise"] = df["cruise"].apply(lambda x: x.strip())
#df["lat"] = df["lat"].apply(lambda x: x.strip())
#df["lon"] = df["lon"].apply(lambda x: x.strip())

#df["cruise"] = df["cruise"].astype('object')
#df["lat"] = df["lat"].astype('float64')
#df["lon"] = df["lon"].astype('float64')

# print(df.info())

filepath = "C:/Users/16308/Coding/en_mileage/csv_files/EN001_EN673.csv"
dataframe = pd.read_csv(filepath)
df = pd.DataFrame(dataframe)
# print(dataframe.head(5))

coord_list = []

for index, row in df.iterrows():
    lat_lon = (row['cruise'], row['lat'], row['lon'])
    coord_list.append(lat_lon)

dist = []

for i in range(len(coord_list)):
    # if i + 1 < len(coord_list): also works
    if i + 1 != len(coord_list):
        row1 = coord_list[i]
        coord1 = (row1[1], row1[2])
        row2 = coord_list[i+1]
        coord2 = (row2[1], row2[2])
        if row1[0] == row2[0]:
            distance = great_circle(coord1,coord2).miles
            dist.append(distance)

dist_sum = 0

for i in range(len(dist)):
    dist_sum = dist_sum + dist[i]

print(dist_sum)