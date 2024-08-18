import pandas as pd

weather_df = pd.read_csv('weatherAUS.csv')

weather_df = weather_df.loc[:,['Date', 'Rainfall', 'Location', 'Temp3pm', 'Humidity3pm', 'WindSpeed3pm']]

weather_df.to_csv('weatherAUS.csv', index=False)