import pandas as pd
import numpy as np
import time
from datetime import timedelta , datetime

CITY_DATA_DICT = { 'chicago':'chicago.csv','new york':'new_york_city.csv','washington':'washington.csv'}

def get_filter():
    #Function get_filter is made to take the user input and filter the data based on it
    # return three args city month day to construct a dataframe
    while True:
        city = input("- Choose what city do you want to see its data Chicago,New York,Washington, Please .. \n").lower()  # We use the lower function to avoid case sensitivity
        # Check if the city he Entered in the dictionary of cities we created or not
        if city not in CITY_DATA_DICT.keys():
            print("Please ,Provide a valid city name")
        else:
            print(f"You have Entered {city} city")
            break

    #This dictionary is made to collect all options together in one place and can use it in every Statement Easily to select the filter
    inputSelect = {'month' :  ['january', 'february', 'march', 'april', 'may', 'june' , 'all'] ,
                   'day'  :  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' , 'all'] ,
                   'both'  : 'both' , 'none' :'none'}
    inputFilter = input("Do you want to get Data by month,day,both or none(will get All Data) ?.... \n").lower()


    # Check if the input valid or not
    while True:
        if inputFilter not in inputSelect.keys() :
            print("You have Entered not valid filter...")
            inputFilter = input("Do you want to get Data by month,day,both or none ?.... \n").lower()
        else :
            print(f"you have Entered {inputFilter.title()}")
            break

    # if the user want the data contain a specific month and if he does not need it will get all months
    if inputFilter =='month' or inputFilter =='both' or inputFilter =='all':
        month = input("Please, Enter a month between (Jan and June) or Enter all if you want to get all months \n").lower()
        while month not in inputSelect['month'] :
            print("You have entered not valid month name...")
            month = input("Please, Enter a month between (Jan and June) or Enter all if you want to get all months \n").lower()
        print(f"you have entered {month.title()}")
    else:
        month ="all"

    # if the user want the data contain a specific day and if he does not need it will get all days
    if inputFilter =='day' or inputFilter =='both'  or inputFilter =='all':
        day = input("Please, Enter a day from the week (ex:Sunday,Monday,..) or Enter all if you want to get all days  \n").lower()
        while day not in inputSelect['day'] :
            print("You have entered not valid day name...")
            day = input("Please, Enter a day from the week or Enter all if you want to get all days  \n").lower()
        print(f"you have entered {day.title()}")
    else:
        day ="all"
    print('-'*50)
    return city,month,day

def load_data(city,month,day) :
    #load data function is made to get the data from the csv files and construct a data frame by every city name the user input

    #Read the data and put it into a data frame
    dataFrame = pd.read_csv(CITY_DATA_DICT[city])
    dataFrame['Start Time'] = pd.to_datetime(dataFrame['Start Time'])

    #Convert the start time series into time_Date to be easy to do operation on it
    dataFrame['month'] = dataFrame['Start Time'].dt.month
    dataFrame['day_of_week'] = dataFrame['Start Time'].dt.day_name()

    #Get the series based on the filter user has entered
    if month != 'all':
        months = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
        month = months[month]
        dataFrame = dataFrame[dataFrame['month'] == month]

    if day != 'all':
        dataFrame = dataFrame[dataFrame['day_of_week'] == day.title()]
    return dataFrame

def popluar_times_oftravel(dataFrame):
    # popluar_times_oftravel answers the questions of time Statistics like most common days , months , etc..

    start_time = time.time()
    # to print the most common month
    months = {1:'january', 2:'february',3: 'march', 4:'april',5: 'may',6: 'june'}
    month_df = dataFrame['month'].mode()[0]            # Get the most frequent month in this series
    month_name= months[month_df]
    print(f"- The most common month is : {month_name} .")

    #To get the most frequent day
    day_df =dataFrame['day_of_week'].mode()[0]
    print(f"- The most common day is : {day_df} .")

    #To get the most frequent hour
    dataFrame['hour'] =dataFrame['Start Time'].dt.hour
    hour_df = dataFrame['hour'].mode()[0]
    print(f"- The most common hour is : {hour_df} .")   #to get the most frequent hour
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

    return ("We are Preparing your Data , please wait ......")

def popular_staionsAndtrips(dataFrame) :
    #popular_staionsAndtrips answers the question about stations and trips like the the most common station ..
    start_station = dataFrame['Start Station'].mode()[0]
    print(f"- The most common Start Staion is :{start_station} . ")

    end_station = dataFrame['End Station'].mode()[0]
    print(f"- The most common End Staion is :{end_station} . ")

    common_trip = 'from ' + dataFrame['Start Station'] + ' to ' + dataFrame['End Station']
    common_trip0= common_trip.mode()[0]
    print(f"- The most common Trip from start to end is :{common_trip0} . ")
    print('-'*50)

def trip_duration(dataFrame):
    #trip_duration is made to get the duration stats about the trips
    start_time = time.time()

    totalTraveinSec = dataFrame['Trip Duration'].sum()  # To get The Total trave time in seconds
    totalDays = totalTraveinSec //86400                 # Calculate the no.of Days
    totalHours = (totalTraveinSec -totalDays*86400) //3600  # Calculate the no.of Days
    totalMin = totalTraveinSec % (3600) // 60               #Calculate the no.of mins
    tot_sec = totalTraveinSec % 3600 % 60

    # Get The duration in every time unit
    print(f"Total Trave Time is :\nin Days : {totalDays}\nin Hours : {totalTraveinSec//(3600)}"
          f"\nin Minutes : {totalTraveinSec//60} \nin Seconds : {totalTraveinSec}")

    print(f"The Total Travel Time is {totalDays} Days and {totalHours} Hours"
          f" and {totalMin} Minutes and {tot_sec} Seconds")
    print('-'*50)

    averageTravetimeinSec = dataFrame['Trip Duration'].mean()      #As the mean is the average
    averageDays = averageTravetimeinSec//86400
    averageHours= averageTravetimeinSec//3600
    averageMins = averageTravetimeinSec //60
    avg_sec = averageTravetimeinSec % 3600 % 60

    print(f"Average Time of Travel is : \nin Days : {averageDays} \nin Hours : {averageHours} \nin Minutes : {averageMins}\n"
          f"in Seconds : {averageTravetimeinSec}")
    print(f"Average time is {averageDays} and {(averageTravetimeinSec -averageDays*86400) //3600} and "
          f"{averageTravetimeinSec % (3600) // 60} and {avg_sec.__round__()} Seconds ")  # I used round here as the mean mostly will be float num.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)
def userInfo(dataFrame):
    start_time = time.time()
    #This Function take the dataframe and get the series of user type and Gender

    #Value_counts return the series of column selected
    userType= dataFrame['User Type'].value_counts()
    print(f"The types of Users are :\n{userType} ")
    print('-'*50)

    # Check if the gender exist in the dataframe or not as there is no columns of gender and birth date in washington DC file
    if 'Gender' in dataFrame.columns :
        userGender = dataFrame['Gender'].value_counts()
        print(f"The Gender of User is :\n{userGender}")
    else :
        print("Sorry,The Gender of Users Data does not available now...")
    print('-'*30)
    if 'Birth Year' in dataFrame.columns :
        birthYear= dataFrame['Birth Year']
        print(f"The Earlist year of birth is \t :{int(birthYear.min())}\n"
              f"The most recent year of birth is :{int(birthYear.max())}\n"
              f"The most common year of birth is :{int(birthYear.mode()[0])}")
    else :
        print("Sorry,The Birth Year of Users Data does not available now...")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def displayData(dataFrame):
    #To display the next 5 raws if the user asked to do
    ins= print("Do you want to display the first raws of Data ?...")
    inputQ = input("Please Enter yes or no ").lower()
    i = 0                                                             #--> The iterator
    if inputQ =='yes':
        while True :
            print(dataFrame.iloc[i:i+5])
            i+=5                                                     #--> to increment the iterator
            check = input("Do you want to show the next 5 raws ?...").lower()
            if check =='no':
                break
def main():
    while True:
        city, month, day = get_filter()
        df = load_data(city, month, day)
        popluar_times_oftravel(df)
        popular_staionsAndtrips(df)
        trip_duration(df)
        userInfo(df)
        displayData(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()