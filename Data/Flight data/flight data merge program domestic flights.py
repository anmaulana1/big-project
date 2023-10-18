
import pandas as pd

# Load CSV files
df_2005 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2005.csv'
df_2006 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2006.csv'
df_2007 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2007.csv'
df_2008 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2008.csv'
df_2009 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2009.csv'
df_2010 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2010.csv'
df_2011 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2011.csv'
df_2012 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2012.csv'
df_2013 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2013.csv'
df_2014 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2014.csv'
df_2015 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2015.csv'
df_2016 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2016.csv'
df_2017 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2017.csv'
df_2018 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2018.csv'
df_2019 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2019.csv'
df_2020 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2020.csv'
df_2021 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2021.csv'
df_2022 = 'https://raw.githubusercontent.com/anmaulana1/big-project/main/Data/Flight%20data/Domestic%20data/T_T100D_SEGMENT_ALL_CARRIER_DOMESTIC_2022.csv'

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


dfw = pd.read_pickle('/Users/daanmichel/TU Delft/TIL Programming/big-project/Data/Flight data/MERGED_DATA_DOMESTIC.pkl')
print(dfw.info())