import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=input('\nEnter the city you wish to see results of "Chicago" OR "Washington" OR "New York" \n').lower()
            if(city in CITY_DATA):
                break
            else:
                print("Looks like you have entered incorrect city name!! Please choose one of the three cities")
        except Exception as e:
            print("Exception has occured: {}".format(e))
            
    print('You are about to see data about {}'.format(city.title()))
        

    # TO DO: get user input for month (all, january, february, ... , june)
    #try:
    #month_filter=input('Filter by month? Y for YES and N for NO)
    #if(month_filter=='Y' or)
    months=['all','january','february','march','april','may','june']
    while True:
        try:
            month=input('\nEnter the month january, february, march, april, may, june, all(for all months), none(for no month filter)\n').lower()
            if(month in months):
                break
            else:
                if(month=="none"):
                    month=None
                    break
                    print("Looks like you have entered incorrect month! Please re-enter name of the month")
        except Exception as e:
            print("Exception occured: {}".format(e))         


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays={'all':'all','su':'sunday','mo':'monday','tu':'tuesday','we':'wednesday','th':'thursday','fr':'friday','sa':'saturday'}
    while True:
        try:
            weekday=input("\nEnter weekday mo,tu,we,th,fr,sa,su,all(for all days) and none(for no day filter)\n").lower()
            if(weekday in weekdays):
                day=weekdays[weekday]
                break
            else:
                if(weekday.lower()=='none'):
                    day=None
                    break
                print("Incorrect weekday entered! Try again")
        except Exception as e:
            print("Exception occured: {}".format(e))
                
    print('-'*40)
    print('Your filters are as below:')
    print(city.title(),month,day)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all' and month!=None:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    df['month']=df['Start Time'].dt.month
    df['month']=df['month'].apply(lambda m:calendar.month_abbr[m])    
        
    if day != 'all' and day != None:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    df['weekday']=df['Start Time'].dt.weekday_name
    print('Most common day of week: ',df['weekday'].mode()[0])

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('Most common hour: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common Start Station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most common End Station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    #df['comb']=df['Start Station']+df['End Station']
    print('Most common trip: ',(df['Start Station']+df['End Station']).mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:{} hours'.format((df['Trip Duration'].sum())/3600))

    # TO DO: display mean travel time
    print('Average trip duration: {} minutes'.format((df['Trip Duration'].mean())/60))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('\nGender count:')
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nEarliest birth year: ',int(df['Birth Year'].min()))
    print('\nMost recent birth year: ',int(df['Birth Year'].max()))
    print('\nMost common birth year: ',int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_data(df):
    counter=0
    try:
        while True:
            rst=input('Display individual trip data? yes or no\n').lower()
            if(rst=='yes' and counter<df.size):
                for i in range(5):
                    print(df.iloc[counter])
                    print('-'*40)
                    counter+=1
            else:
                break
    except Exception as e:
        print('Exception occured: {}'.format(e))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        counter=0
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if(city!='washington'):
            user_stats(df)
        else:
            print("No user data available for this city")
        trip_data(df)    
        #while True:
         #   rst = input('Display next five trips data? yes or no').lower()
          #  if(rst=='yes'):
           #     trip_data(df)
            #else:
             #   break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            

if __name__ == "__main__":
	main()
