import pandas as pd
import os
import numpy as np

folder_path = 'city_compare/'

# iterate over all .csv files
day_count  = 0
#avg distance for 3 kind of cities
avg1 = avg2 = avg3 = avg4 = avg5 = 0
for filename in os.listdir(folder_path):
    
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, header=None)

        day_count += 1

        for i in range(1,df.shape[1] - 1):
            if df.iloc[0, i] == '一线城市':
                avg1 += (float(df.iloc[3, i]) - float(df.iloc[2, i])) / float(df.iloc[1, i])
            elif df.iloc[0, i] == '二线城市':
                avg2 += (float(df.iloc[3, i]) - float(df.iloc[2, i])) / float(df.iloc[1, i])
            elif df.iloc[0, i] == '三线城市':
                avg3 += (float(df.iloc[3, i]) - float(df.iloc[2, i])) / float(df.iloc[1, i])
            elif df.iloc[0, i] == '新一线城市':
                avg4 += (float(df.iloc[3, i]) - float(df.iloc[2, i])) / float(df.iloc[1, i])
            elif df.iloc[0, i] == '四线城市':
                avg5 += (float(df.iloc[3, i]) - float(df.iloc[2, i])) / float(df.iloc[1, i])
            else:
                continue


 
output = pd.DataFrame()       
output.loc[0,1] = '一线城市'
output.loc[0,2] = '新一线城市'
output.loc[0,3] = '二线城市'
output.loc[0,4] = '三线城市'
output.loc[0,5] = '四线城市'
output.loc[1,1] = avg1/day_count
output.loc[1,2] = avg4/day_count
output.loc[1,3] = avg2/day_count
output.loc[1,4] = avg3/day_count
output.loc[1,5] = avg5/day_count

# Define the output filename
output_name = 'result.csv' 
        
# Save the modified DataFrame to a new CSV file
output.to_csv(output_name, index=False)
print(f"Processed and saved: {output_name}")
