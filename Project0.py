'''
import pandas as pd
import numpy as np
import time
import datetime
CITY_DATA_DICT = {'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv'}
def getFilter():
    month = ''
    day =''
    '''
'''
    print("Welcome to US bikeshare Program")
    # To Ask user to provide the city he want to get the data about
    while True :
        city =input("-Choose what city do you want to see its data " "chicago,new york , washington , Please .. \n").lower() # We use the lower function to avoid case sensitivity
        if city not in CITY_DATA_DICT.keys() :                        # Check if the city he Entered in the dictionary we created or not
            print("Please , Provide a valid city name")
        else:
            print(f"You have Entered {city} city")
            break

    filterSelect = {'month': ['january', 'febraury', 'march', 'april', 'may', 'june'],
         'day': ['saturday','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'],'both' : 'both' , 'none' : 'none'}

    filterInput = input("Do you want to get Data by month,day,both or none.. \n").lower()
    while filterInput not in filterSelect.keys():
        filterInput = input("Please Enter a valid input to get Data by month,day,both or none.. \n").lower()


    if filterInput=='month' or filterInput=='both' :
        while True :
            month = input("Please, Enter a month between (Jan and June) or all \n").lower()
            if month in filterSelect['month'] or month =='all' :
                print(f"You have entered {month}")
                break
            else :
                print("Please Enter a valid month title")
    else :
        month = 'all'
    if filterInput == 'day' or filterInput == 'both' :
        while True :
            day = input("Please, Enter a day in the week or all \n").lower()
            if day in filterSelect['day'] or day == 'all':
                print(f"You have entered {day}")
                break
            else :
                print("Please Enter a valid day title ")
    elif  filterInput =='none':
        day = 'all'

    return city,month,day

def load_data(city,month,day):
    df = pd.read_csv(CITY_DATA_DICT[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

'''
'''
def main() :
    city,month,day= getFilter() # pass the values returned
    df = load_data(city, month, day)
    print(df)

if __name__ == "__main__":
	main()
'''








'''
    dataFrame = pd.read_csv(CITY_DATA_DICT[city]) # --> a data frame to get the data file
    dataFrame['Start Time'] = pd.to_datetime(dataFrame['Start Time'])

    dataFrame['month'] = dataFrame['Start Time'].dt.month                   # --> put the month into a single col as a number in the data Frame
    dataFrame['day_of_week'] = dataFrame['Start Time'].dt.day_name()        # --> put the day into a single col as a number in the data Frame

    # if the user enter the month
    if month != 'getallmonths' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        dataFrame= dataFrame[dataFrame['month'] == month]
    # if the user entered the day
    if day != 'getalldays':
        dataFrame = dataFrame[dataFrame['day_of_week'] == day.title()]

    return dataFrame
'''










import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }

def get_filters():


    city = input('Would you like to see data for Chicago, New York, or Washington? ')
    while True:
        print('You provided invalid city name')
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()

    # get user input for filter type (month, day or both).
    filter = input('Would you like to filter the data by month, day, both, or none? ').lower()
    while filter not in(['month', 'day', 'both', 'none']):
        print('You provided invalid filter')
        filter = input('Would you like to filter the data by month, day, both, or none? ').lower()


    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both':
        month = input('Which month - January, February, March, April, May, or June? ').lower()
        while month not in months:
            print('You provided invalid month')
            month = input('Which month - January, February, March, April, May, or June? ').lower()
    else:
        month = 'all'

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if filter == 'day' or filter == 'both':
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
        while day not in days:
            print('You provided invalid day')
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
    else:
        day = 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def main() :
    city,month,day= get_filters() # pass the values returned
    df = load_data(city, month, day)
    print(df)

if __name__ == "__main__":
	main()