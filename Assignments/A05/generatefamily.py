import os
import pandas as pd

currentlocation=os.path.dirname(os.path.abspath(__file__))
print(currentlocation)
dfs=[]
for i in os.listdir(currentlocation+'\\resources\\'):
    print(i)
    dfs.append(pd.read_csv(currentlocation+'\\resources\\'+i))

combined_df = pd.concat(dfs, axis=0, ignore_index=True)

combined_df.drop_duplicates(subset=['first_name', 'gender'], inplace=True)

combined_last_name_column = combined_df['last_name'] 

combined_df=combined_df[['first_name',"gender"]]
combined_file = currentlocation+'/first_names.csv'
combined_df.to_csv(combined_file, index=False)


combined_last_name_column.drop_duplicates(inplace=True)

combined_file2 = currentlocation+'/last_names.csv'

combined_last_name_column.to_csv(combined_file2, index=False, header=True)