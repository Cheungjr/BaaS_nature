import pandas as pd
import os
import csv

folder_path = 'carbon_result/'

# iterate over all .csv files
day_count  = 0
#avg distance for 3 kind of cities
tmp = [0.563784355,0.587603834,0.596720099,0.62655087,0.614117647,0.547033285,0.54429573,0.538454462,0.523274854,0.56244886,0.678936125,0.571172325]
tmp.sort()
rat_list = [ tmp ,[0] * 12,[0] * 12 ]

for filename in os.listdir(folder_path):

    if filename.endswith('.csv'): 
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, header=None)

        day_count += 1
        for i in range(1,df.shape[1]-1):
            for j in range(len(rat_list[0])):
                if rat_list[0][j] == float(df.iloc[8, i]):
                    rat_list[1][j] += (float(df.iloc[3, i]) - float(df.iloc[2, i])) / float(df.iloc[1, i])
                    rat_list[2][j] += (float(df.iloc[7, i]) - float(df.iloc[6, i])) / float(df.iloc[1, i])
                    break

for i in range(len(rat_list[0])):
    rat_list[1][i] /= day_count
    rat_list[2][i] /= day_count

 
with open('cabinet_result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(rat_list[0])
    writer.writerow(rat_list[1])
    writer.writerow(rat_list[2])

print(f"Processed and saved")
