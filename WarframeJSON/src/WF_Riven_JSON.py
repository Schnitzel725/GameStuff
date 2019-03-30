import pandas as pd

pc = pd.read_json('http://n9e5v4d8.ssl.hwcdn.net/repos/weeklyRivensPC.json', orient='columns')
ps4 = pd.read_json('http://n9e5v4d8.ssl.hwcdn.net/repos/weeklyRivensPS4.json', orient='columns')
xb = pd.read_json('http://n9e5v4d8.ssl.hwcdn.net/repos/weeklyRivensXB1.json', orient='columns')

def json_convert(df, platform):
    df = df[['itemType', 'compatibility', 'rerolled', 'pop', 'min', 'max', 'avg', 'stddev']]
    df.columns = ['Item Type', 'For Weapon', 'Rerolled', 'Popularity', 'Lowest Price (Plat)', 'Highest Price (Plat)', 'Average Trade Value', 'Average Price Variation']
    file_name = platform + '_json_data.xlsx'
    wr = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(file_name, sheet_name='PC')

json_convert(pc, 'PC')
json_convert(xb, 'XBOX')
json_convert(ps4, 'PS4')

# print('done')
