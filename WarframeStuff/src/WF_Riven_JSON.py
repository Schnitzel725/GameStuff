import datetime as dt
import pandas as pd
import os

# print (os.getcwd())

path = 'RivenStats_' + dt.datetime.now().strftime('%b-%d-%Y_%H%M%S')

original = os.getcwd()
os.mkdir(path)
os.chdir(path)

# reads JSON data from websites listed below
pc = pd.read_json('http://n9e5v4d8.ssl.hwcdn.net/repos/weeklyRivensPC.json', orient='columns')
ps4 = pd.read_json('http://n9e5v4d8.ssl.hwcdn.net/repos/weeklyRivensPS4.json', orient='columns')
xb = pd.read_json('http://n9e5v4d8.ssl.hwcdn.net/repos/weeklyRivensXB1.json', orient='columns')

# converts the dataframe's columns to something understandable
def json_convert(df, platform):
    df = df[['itemType', 'compatibility', 'rerolled', 'pop', 'min', 'max', 'avg', 'stddev']]
    df.columns = ['Item Type', 'For Weapon', 'Rerolled', 'Popularity', 'Lowest Price (Platinum)', 'Highest Price (Platinum)', 'Average Trade Value', 'Average Price Variation']
    file_name = platform + '_json_data.xlsx'
    df.to_excel(file_name, sheet_name='PC')

# calls method and writes to three excel files (PC_json_data.xlsx, XBOX_json_data.xlsx, PS4_json_data.xlsx)
json_convert(pc, 'PC')
json_convert(xb, 'XBOX')
json_convert(ps4, 'PS4')

os.chdir(original) # go back to original directory to prevent folder inside of folder inside of folder etc.
