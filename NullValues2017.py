import pandas as pd

newweather_df = pd.read_csv('2017canberraweatherAUS.csv')

newweather_df.dropna(inplace=True)

newweather_df.to_csv('2017canberraweatherAUS.csv', index=False)