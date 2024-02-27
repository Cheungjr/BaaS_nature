import pandas as pd
import os
import numpy as np

folder_path = 'suburb/'

# iterate over all .csv files
day_count  = 0
avg1 = 0
avg2 = 0
for filename in os.listdir(folder_path):
    
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, header=None)

        day_count += 1
        avg1 += (float(df.iloc[3, 1]) - float(df.iloc[2, 1])) / float(df.iloc[1, 1])
        avg2 += (float(df.iloc[3, 2]) - float(df.iloc[2, 2])) / float(df.iloc[1, 2])

 
output = pd.DataFrame()       
output.loc[0,1] = '市中心'
output.loc[0,2] = '郊区'
output.loc[1,1] = avg1/day_count
output.loc[1,2] = avg2/day_count
# Define the output filename
output_name = 'result.csv' 
        
# Save the modified DataFrame to a new CSV file
output.to_csv(output_name, index=False)
print(f"Processed and saved: {output_name}")
