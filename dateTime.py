# The DateTime module is categorized into 6 main classes – 

# date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month and day.
# time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.
# datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
# timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
# tzinfo – It provides time zone information objects.
# timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).

from datetime import date

my_date = date(1996, 12, 11)  # year,month,day
 
print("Date passed as argument is", my_date)

today = date.today()
print("Today's date is : ",today)

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


import time

currentTime = time.time()       # returns number of seconds after the epoch ,i.e, 1st jan 1970

from datetime import datetime

date_time = datetime.fromtimestamp(1887639468)      # (number of seconds after the epoch ) => it will give corresponding date and time
print("Datetime from timestamp:", date_time)

Str = date.isoformat(today)         # converts datetime to string format
print("String Representation", Str)



# date class methods

# Function Name 	    Description

# ctime()	            Return a string representing the date
# fromisocalendar()	    Returns a date corresponding to the ISO calendar
# fromisoformat()	    Returns a date object from the string representation of the date
# fromordinal()	        Returns a date object from the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1
# fromtimestamp()	    Returns a date object from the POSIX timestamp
# isocalendar()	        Returns a tuple year, week, and weekday
# isoformat()	        Returns the string representation of the date
# isoweekday()	        Returns the day of the week as integer where Monday is 1 and Sunday is 7
# replace()	            Changes the value of the date object with the given parameter
# strftime()	        Returns a string representation of the date with the given format
# timetuple()	        Returns an object of type time.struct_time
# today()	            Returns the current local date
# toordinal()	        Return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1
# weekday()	            Returns the day of the week as integer where Monday is 0 and Sunday is 6

print(my_date.ctime())      # Wed Dec 11 00:00:00 1996
print(my_date.fromisocalendar(2022,2,5))    # (year,week,day[1-7])
print(my_date.strftime('%d/%m/%Y'))         # 11/12/1996




from datetime import time
 
my_time = time(13, 24, 56)
 
print("Entered time", my_time)

Time = time(11, 34, 56,500)
 
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)



# time class methods

# Function Name	        Description

# dst()	                Returns tzinfo.dst() is tzinfo is not None
# fromisoformat()	    Returns a time object from the string representation of the time
# isoformat()	        Returns the string representation of time from the time object
# replace()	            Changes the value of the time object with the given parameter
# strftime()	        Returns a string representation of the time with the given format
# tzname()	            Returns tzinfo.tzname() is tzinfo is not None
# utcoffset()	        Returns tzinfo.utcffsets() is tzinfo is not None






from datetime import datetime
 
a = datetime(1999, 12, 12, 12, 12, 12, 342380)      # (year, month, day, hour, minute, sec, millisec)
print(a)

print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

today = datetime.now()
 
print("Current date and time is", today)


# datetime class methods

# Function Name	        Description

# astimezone()	        Returns the DateTime object containing timezone information.
# combine()	            Combines the date and time objects and return a DateTime object
# ctime()	            Returns a string representation of date and time
# date()	            Return the Date class object
# fromisoformat()	    Returns a datetime object from the string representation of the date and time
# fromordinal()	        Returns a date object from the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1. The hour, minute, second, and microsecond are 0
# fromtimestamp()	    Return date and time from POSIX timestamp
# isocalendar()	        Returns a tuple year, week, and weekday
# isoformat()	        Return the string representation of date and time
# isoweekday()	        Returns the day of the week as integer where Monday is 1 and Sunday is 7
# now()	                Returns current local date and time with tz parameter
# replace()	            Changes the specific attributes of the DateTime object
# strftime()	        Returns a string representation of the DateTime object with the given format
# strptime()	        Returns a DateTime object corresponding to the date string
# time()	            Return the Time class object
# timetuple()	        Returns an object of type time.struct_time
# timetz()	            Return the Time class object
# today()	            Return local DateTime with tzinfo as None
# toordinal()       	Return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1
# tzname()	            Returns the name of the timezone
# utcfromtimestamp()	Return UTC from POSIX timestamp
# utcoffset()	        Returns the UTC offset
# utcnow()	            Return current UTC date and time
# weekday()	            Returns the day of the week as integer where Monday is 0 and Sunday is 6




# timeDelta Class
# Python timedelta class is used for calculating differences in dates and also can be used for date manipulations in Python. It is one of the easiest ways to perform date manipulations.


from datetime import timedelta

future_date_after_2yrs = today + timedelta(days=730)
 
future_date_after_2days = today + timedelta(days=2)
 
# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))       # future_date_after_2yrs: 2024-11-14 23:41:41.361623
print('future_date_after_2days:', str(future_date_after_2days))     # future_date_after_2days: 2022-11-17 23:41:41.361623





# Format Datetime
# Formatting Datetime can be very necessary as the date representation may differe from place to place. Like in some countries it can be yyyy-mm-dd and in other country it can be dd-mm-yyyy. To format Python Datetime strptime and strftime functions can be used.

# Python Datetime strftime
# strftime() method converts the given date, time or datetime object to the a string representation of the given format.

from datetime import datetime as dt

# Code	Description	                                                                Output

# %a	Abbreviated weekday name.	                                                Sun, Mon, …
# %A	Weekday as full name.	                                                    Sunday, Monday, …
# %w	Weekday as a decimal number.	                                            0, 1, 3, …, 6
# %d	Day of the month with a zero appended.	                                    01, 02, …, 31
# %-d	Day of the month as a decimal number.	                                    1, 2, …, 30
# %b	Abbreviated month name.	                                                    Jan, Feb, …, Dec
# %B	Full month name.	                                                        January, February, …
# %m	Month decimal number with a zero appended.	                                01, 02, …, 12
# %-m	Month as a decimal number.	                                                1, 2, …, 12
# %y	Year without century in decimal number with a zero appended.	            00, 01, …, 99
# %-y	Year without century.	                                                    0, 1, …, 99
# %Y	Year with century.	                                                        2015, 2021 etc.
# %H	24 Hours clock from 00 to 23.	                                            00, 01, …, 23
# %-H	24 Hours clock from 0 to 23.	                                            0, 1, …, 23
# %I	12 Hour clock from 01 to 12.	                                            01, 02, …, 12
# %-I	12 Hour clock from 01 to 12.	                                            1, 2, … 12
# %p	Locale’s AM or PM.	                                                        AM, PM
# %M	Minute in decimal number from 00 to 59.                                 	00, 01, …, 59
# %-M	Minute as a decimal number.                                             	0, 1, …, 59
# %S	Second in decimal number from 00 to 59	                                    00, 01, …, 59
# %-S	Second as a decimal number.	                                                0, 1, …, 59
# %f	Microsecond as a decimal number with a zero appended on the left.	        000000 – 999999
# %z	UTC offset in the form +HHMM or -HHMM.	 
# %Z	Time zone name.	 
# %j	The day of the year as a decimal number with a zero appended.	            001, 002, …, 366
# %-j	The Day of the year as a decimal number.	                                1, 2, …, 366
# %U	The year’s week number (Sunday as the first day of the week).	            00, 01, …, 53
# %W	Week number of the year (Monday as the first day of the week).	            00, 01, …, 53

 
now = dt.now()
print("Without formatting", now)        # Without formatting 2022-11-15 23:54:25.047929
 
# Example 1
s = now.strftime("%A %m %Y")
print('\nExample 1:', s)                # Example 1: Tuesday 11 2022
 
# Example 2
s = now.strftime("%a %m %y")            # Example 2: Tue 11 22
print('\nExample 2:', s)
 
# Example 3
s = now.strftime("%I %p %S")            
print('\nExample 3:', s)                # Example 3: 11 PM 25
    
# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)                # Example 4: 23:54:25

time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003", "27/05/99 07:35:5.523", "28/05/99 05:15:55.523"]

format_data = "%d/%m/%y %H:%M:%S.%f"    # it is the format in which the data is given and the format in which we want data
  
for i in time_data:
    print(datetime.strptime(i, format_data))
# 1999-05-25 02:35:08.023000
# 1999-05-26 12:45:00.003000
# 1999-05-27 07:35:05.523000
# 1999-05-28 05:15:55.523000


# practice

current = datetime.now()
print(current)
print(current.year)
print(current.month)
print(current.weekday())
print(current.day)
print(current.strftime("%j"))       # current day of the year

str = "Jan 1 2014 2:43 PM"
print(datetime.strptime(str,"%b %d %Y %I:%M %p"))

subtract_5_days = current - timedelta(days=5)
print(subtract_5_days)