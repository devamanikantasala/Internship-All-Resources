#Task 1 : Get the current day, month, year, hour, minute, seconds and timestamp from datetime module
from datetime import datetime as dt;
current_date_and_time = dt.now();
print(f"Date:{current_date_and_time.day}-{current_date_and_time.month}-{current_date_and_time.year}\nTime:{current_date_and_time.hour}:{current_date_and_time.minute}:{current_date_and_time.second}::{current_date_and_time.timestamp()}")

#Task 2 : Format the current date using this format: %m/%d/%Y, %H:%M:%S
formated_time = current_date_and_time.strftime("%m/%d/%Y , %H:%M:%S");
print(f'Formated Time:\n{formated_time}');

#Task 3 : Today is '5 December, 2019'. Change this string to time.
date_string = '5 December, 2019'
print(f"The Date String: {date_string}");
date_time = dt.strptime(date_string, '%d %B, %Y');
print(f'The Date in Time: {date_time}');

#Task 4 : Calculate the time difference between now and new year
from datetime import date as d
current_time = d(day=current_date_and_time.day, month=current_date_and_time.month, year=current_date_and_time.year)
target_time = d(day=1, month=1, year=2025)
print(f'The Difference between from {current_time} to {target_time}: {target_time-current_time}');

#Task 5 : Calculate the time difference between 1st Jan 1970 and now.
past_date = dt.strptime('1 Jan 1970', '%d %b %Y')
past_time = d(day=past_date.day, month=past_date.month, year=past_date.year);
print(f"The time difference from {current_time} to {past_time} : {current_time-past_time}");

#Task 6 : Think of for what purposes you can use the datetime module for?
# MyAnswer : 
# To perform time series analysis
# To get the timestamp of any activities in an application
# Adding posts on a blog including
# While developing time related applications like alarm clock, schedule message sender
# While recording the log activity of the certain operation taken place, 
# Industrially this module can be used to monitor the login logout activities of employee
# Also useful in developing some application like taking digital attendance by biometric, iris attendance
# And scheduling a task based on time..
