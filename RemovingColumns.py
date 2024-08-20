import pandas as pd

weather_df = pd.read_csv('weatherAUS.csv')
weather_df.head()

weather_df.drop(columns=['Humidity9am'], inplace=True)
weather_df.head()

cleanedweather_df = weather_df.loc[:,['Date', 'Location', 'Rainfall', 'Temp3pm', 'Humidity3pm', 'WindSpeed3pm']]
cleanedweather_df.head()