import pandas as pd

# Load CSV files
df_2005 = 
df_2006 = 
df_2007 = 
df_2008 = 
df_2009 = 
df_2010 = 
df_2011 = 
df_2012 = 
df_2013 = 
df_2014 = 
df_2015 = 
df_2016 = 
df_2017 = 
df_2018 = 
df_2019 = 
df_2020 = 
df_2021 = 
df_2022 = 

csv_files = [df_2005, df_2006, df_2007, 
             df_2008, df_2009, df_2010, 
             df_2011, df_2012, df_2013,
             df_2014, df_2015, df_2016,
             df_2017, df_2018, df_2019,
             df_2020, df_2021, df_2022
             ]

# Initialize an empty list to store dataframes
dfs = []

# Load and append each CSV file from URLs to the list of dataframes
for url in csv_files:
    df = pd.read_csv(url)
    dfs.append(df)

#Concatenate the dataframes vertically
merged_df = pd.concat(dfs, ignore_index=True)

#Save the merged dataframe to a new Pickle File
merged_df.to_pickle('MERGED_DATA_DOMESTIC.pkl')


dfw = pd.read_pickle('/Users/daanmichel/TU Delft/TIL Programming/big-project/Data/Flight data/merged_flight_data.pkl')
print(dfw.info())