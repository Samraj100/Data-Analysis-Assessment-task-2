import pandas as pd

weather_df = pd.read_csv('weatherAUS.csv')

weather_df.info()

weather_df.drop(weather_df.index[1:45589], inplace=True)
weather_df.drop(weather_df.index[3434:99871], inplace=True)

weather_df.to_csv('weatherAUS.csv', index=False)