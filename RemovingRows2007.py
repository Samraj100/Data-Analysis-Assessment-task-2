import pandas as pd

oldweather_df = pd.read_csv('2007canberraweatherAUS.csv')

oldweather_df.drop(oldweather_df.index[57:3432], inplace=True)

oldweather_df.to_csv('2007canberraweatherAUS.csv', index=False)