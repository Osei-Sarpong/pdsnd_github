import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\nHey there! Nice to meet you. Let's delve straight into analyzing US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n\nFor the three possible cities: \nChicago\nNew York City\nWashington\nWhich would you like to compute statistics for?\n").lower()
        possible_cities = ['chicago', 'new york city', 'washington']
        if city in possible_cities:
            break
        else:
            print("\nChoose one of the cities in the prompt in order run your analysis!\n")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nFor the six possible months: \nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nWhich would you like to compute statistics for?\nType ALL to simply analyze all months\n').lower()
        possible_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in possible_months:
            break
        else:
            print("\nChoose one of the months in the prompt in order run your analysis\n!")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nFor the seven possible days: \nSunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nWhich would you like to compute statistics for?\nType ALL to simply analyze all days\n').lower()
        possible_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all' ]
        if day in possible_days:
            break
        else:
            print('\nChoose one of the days in the prompt in order run your analysis!\n')

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    selected_month = df['month'].mode()[0]
    common_month = ['January', 'February', 'March', 'April', 'May', 'June']
    print()
    print('The month that had the most bikes shared was:\n{}'.format(common_month[selected_month - 1] ))
    print()

    # display the most common day of week
    print()
    print('The day that had the most bikes shared was:\n{}'.format(df['day_of_week'].mode()[0]))
    print()

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    if common_start_hour < 12:
        common_start_hour = str(common_start_hour) + ' AM'
    else:
        common_start_hour = str(common_start_hour - 12) + ' PM'
    print()
    print('The start hour that had the most bikes shared was:\n{}'.format(common_start_hour))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print()
    print('The start station that had the most bikes shared was:\n{}'.format(df['Start Station'].mode()[0]))
    print()

    # display most commonly used end station
    print()
    print('The end station that had the most bikes shared was:\n{}'.format(df['End Station'].mode()[0]))
    print()

    # display most frequent combination of start station and end station trip
    df['Combined Stations'] = df['Start Station'] + ' and ' + df['End Station']
    print()
    print('The start and end station combination that had the most bikes shared was:\n{}'.format(df['Combined Stations'].mode()[0]))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print()
    print('The total travel time was:\n{}'.format(df['Trip Duration'].sum().round(2)))
    print()

    # display mean travel time
    print()
    print('The average(mean) travel time was:\n{}'.format(df['Trip Duration'].mean()))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print()
    print('These are the counts for the different user types:\n{}'.format(user_counts))
    print()

    # TO DO: Display counts of gender
    try:
      gender_counts = df['Gender'].value_counts()
      print()
      print('These are the counts for the different gender types:\n{}'.format(gender_counts))
      print()
    except KeyError:
      print()
      print('Sorry, data for the counts of the different gender types is unavailable for this city.')
      print()

    # TO DO: Display earliest, most recent, and most common year of birth
    # This displays the earliest year of birth
    try:
      earliest_year_of_birth = df['Birth Year'].min()
      print()
      print('The earliest year of birth is:\n{}'.format(int(earliest_year_of_birth)))
      print()
    except KeyError:
      print()
      print('Sorry, data for the earliest year of birth is unavailable for this city.')
      print()

    # This displays the most recent year of birth
    try:
      most_recent_year_of_birth = df['Birth Year'].max()
      print()
      print('The most recent year of birth is:\n{}'.format(int(most_recent_year_of_birth)))
      print()
    except KeyError:
      print()
      print('Sorry, data for the most recent year of birth is unavailable for this city.')
      print()

    # This displays the most common year of birth
    try:
      most_common_year_of_birth= df['Birth Year'].value_counts().idxmax()
      print()
      print('The most common year of birth is:\n{}'.format(int(most_common_year_of_birth)))
      print()
    except KeyError:
      print()
      print('Sorry, data for the most common year of birth is unavailable for this city.')
      print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(df):
    """Asks user whether or not they would like to see some raw data and then proceeds to show
    five lines of raw data upon request by the user"""
    index = 0
    while True:
        raw_data = input('Would you also like to view some raw data?\nType yes or no\n').lower()
        if raw_data != 'yes':
            break
        else:
            print(df[index: index + 5])
            index += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
