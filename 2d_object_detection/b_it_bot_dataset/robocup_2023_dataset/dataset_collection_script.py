import itertools
import os
import pandas as pd
import numpy as np

# object list
# ['AllenKey', 'Axis2', 'Bearing2', 'Drill', 'F20_20_B', 'F20_20_G', 'Housing', 'M20', 'M20_100', 'M30', 'Motor2', 'S40_40_B', 'S40_40_G', 'Screwdriver', 'Spacer', 'Wrench']


# Note: 
# M20, M30, S40_40_B, S40_40_G, F20_20_B, F20_20_G are in both lists
# Because they are quite similar (in pair), so we want more data for them 


objs1 = ['AllenKey', 'Axis2', 'Bearing2', 'Drill', 'F20_20_B', 'F20_20_G', 'Housing', 'M20', 'M30', 'S40_40_B', 'S40_40_G']
objs1 = sorted(objs1)
print(objs1)

records = []
for j in range(1): # TODO: if requires, run it 2 times
    for i in range(5, 6):
        combinations = list(itertools.combinations(objs1, i))
        records.extend(combinations)
    
# count an object in records
count = 0
for record in records:
    if "AllenKey" in record:
        count += 1
print("Each object appears {} times".format(count))

df = pd.DataFrame.from_records(records)
df.columns = [1, 2, 3, 4, 5]
df["collected"] = [None for _ in range(len(df))]
df["annotated"] = [None for _ in range(len(df))]
df.to_csv("robocup_2023_dataset_collection_set1.csv")

objs2 = ['M20', 'M20_100', 'M30', 'Motor2', 'S40_40_B', 'S40_40_G', 'Screwdriver', 'Spacer', 'Wrench', 'F20_20_B', 'F20_20_G']
objs2 = sorted(objs2)
print(objs2)

records = []
for j in range(1): # TODO: if requires, run it 2 times
    for i in range(5, 6):
        combinations = list(itertools.combinations(objs2, i))
        records.extend(combinations)

# count an object in records
count = 0
for record in records:
    if "M20" in record:
        count += 1
print("Each object appears {} times".format(count))

df = pd.DataFrame.from_records(records)
df.columns = [1, 2, 3, 4, 5]
df["collected"] = [None for _ in range(len(df))]
df["annotated"] = [None for _ in range(len(df))]
df.to_csv("robocup_2023_dataset_collection_set2.csv")