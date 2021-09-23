### 25th August, 2021.

### Exploring US Bikeshare Data
Overview
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about the data by computing descriptive statistics.
### Description
Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. Comparison of the system usage between three large cities: Chicago, New York City, and Washington, DC is made.

The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
Gender
Birth Year


Statistics Computed
We explore info about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, I wrote code to provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day
#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
#3 Trip duration

total travel time
average travel time
#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

# Additionally
The last part of the program asks the user if they would like to view some raw data and shows five lines of raw data upon request.



### Files used
In order to answer these questions I used the following csv files which contains the required data for analysis:
chicago.csv
new_york_city.csv
washington.csv

The data used can be accessed using the following link:
https://drive.google.com/file/d/1km4EggJaSvHos_7KKFuHoJxbh-StyM4G/view

### Software used
I made use of the following software when working on the project:
Atom code editor,
Python 3 installed within Anaconda and
Git bash (The terminal application I used to run the code).

### Credits
I got help on some ideas to use in the project from these two sources:
https://github.com/SadiqAlreemi/Explore-US-Bikeshare-Data/blob/master/Python_Project.py and
https://github.com/YashMotwani/US-Bikeshare-Data-Exploration-Program/blob/master/bikeshare_2.py
