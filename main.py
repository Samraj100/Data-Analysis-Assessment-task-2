import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('data/weatherAUS.csv')


weather_df = pd.read_csv('data/canberraweatherAUS.csv',
                            header=None,
                            names=['Date', 'Rainfall', 'Location', 'Temp3pm', 'Humidity3pm', 'WindSpeed3pm'])

oldweather_df = pd.read_csv('data/2007canberraweatherAUS.csv',
                            header=None,
                            names=['Date', 'Rainfall', 'Location', 'Temp3pm', 'Humidity3pm', 'WindSpeed3pm'])

newweather_df = pd.read_csv('data/2017canberraweatherAUS.csv',
                            header=None,
                            names=['Date', 'Rainfall', 'Location', 'Temp3pm', 'Humidity3pm', 'WindSpeed3pm'])


#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(weather_df)

def showCharts():
    weather_df.plot(
                    kind='bar',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rain in Canberra')
    plt.show()

def show2007Charts():
    oldweather_df.plot(
                    kind='bar',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rain in Canberra in 2007')
    plt.show()

def show2017Charts():
    newweather_df.plot(
                    kind='bar',
                    x='Date',
                    y='Rainfall',
                    color='blue',
                    alpha=0.3,
                    title='Rain in Canberra in 2017')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the rain data in Canberra
    4 - Visualise rain data in 2007
    5 - Visualise rain data in 2017
    6 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            show2007Charts()
        elif choice == 5:
            show2017Charts()
        elif choice == 6:
            quit = True
        else:
            print('A number between 1 and 6, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()