import pandas as pd
import numpy as np
from geopy.distance import great_circle
from geopy.point import Point
from os import listdir

# Goal: get an average cruise distance over the Endeavor's lifetime
# then multiply that number by 207 and add it to the result of en_mileage.py

allfiles = listdir(path='C:/Users/16308/Coding/en_mileage/csv_files')
cruise_distances = {}
cruise_averages = {}
zeros = []

for i in range(len(allfiles)):
    filepath = "C:/Users/16308/Coding/en_mileage/csv_files/" + allfiles[i]
    dataframe = pd.read_csv(filepath, dtype = {"cruise": str, "lat": float, "lon": float})
    df = pd.DataFrame(dataframe)
    cruises = np.unique(df["cruise"])

    for i in cruises:
        cruise_distances[i] = []

    coord_list = []

    for index, row in df.iterrows():
        lat_lon = (row['cruise'], row['lat'], row['lon'])
        coord_list.append(lat_lon)

    for i in range(len(coord_list)):
        if i + 1 != len(coord_list):
            row1 = coord_list[i]
            coord1 = (row1[1], row1[2])
            row2 = coord_list[i+1]
            coord2 = (row2[1], row2[2])
            if row1[0] == row2[0]:
                cruise_name = row1[0]
                distance = great_circle(coord1,coord2).miles
                cruise_distances[cruise_name].append(distance)

    for i in cruises:
        if len(cruise_distances[i]) != 0:
            cruise_averages[i] = sum(cruise_distances[i])
        else:
            zeros.append(i)
    
    # print(cruise_averages.items())
    # print(len(cruise_averages))
    # print(len(cruises))

print(zeros)

average = sum(cruise_averages.values()) / len(cruise_averages)
print(average)