import pandas as pd

weather_df = pd.read_csv('canberraweatherAUS.csv')

weather_df.dropna(inplace=True)

weather_df.to_csv('canberraweatherAUS.csv', index=False)