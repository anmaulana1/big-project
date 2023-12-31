import pandas as pd

# Load CSV files
df1 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2005.csv'
df2 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2006.csv'
df3 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2007.csv'
df4 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2008.csv'
df5 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2009.csv'
df6 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2010.csv'
df7 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2011.csv'
df8 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2012.csv'
df9 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2013.csv'
df10 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2014.csv'
df11 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2015.csv'
df12 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2016.csv'
df13 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2017.csv'
df14 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2018.csv'
df15 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2019.csv'
df16 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2020.csv'
df17 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2021.csv'
df18 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/International%20data/T_T100I_SEGMENT_ALL_CARRIER_INTERNATIONAL_2022.csv'

csv_files = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18]

# Initialize an empty list to store dataframes
dfs = []

# Load and append each CSV file from URLs to the list of dataframes
for url in csv_files:
    df = pd.read_csv(url)
    dfs.append(df)

# Concatenate the dataframes vertically
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a new Pickle File
merged_df.to_pickle('MERGED_DATA_INTERNATIONAL.pkl')



dfw = pd.read_pickle('/Users/daanmichel/TU Delft/TIL Programming/big-project/Data/Flight data/MERGED_DATA_INTERNATIONAL.pkl')
print(dfw.info())