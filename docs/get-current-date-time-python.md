#### How to Get Current Date & Time in Python
You can use now() function of datetime python module. This tutorial will show you various ways to get current date and time in the python script. Below example scripts to get date and time has been tested with Python 2.7 and Python 3.5 on Linux system.

#### Get Current Date Time in Python
***
By default now() function returns output in YYYY-MM-DD HH:MM:SS:MS format. Use below sample script to get current date and time in Python script and print results on screen. Create file **getDateTime1.py** with below content.

```no-highlight
import datetime

currentDT = datetime.datetime.now()
print (str(currentDT))
```

Let’s execute the script **getDateTime1.py** as following command.

```no-highlight
user@ubuntu:~$ python getDateTime1.py 

2017-03-06 16:00:04.159338
```

#### Get Current Date Time Attributes in Python
***
You can also get the specific attribute of date and time. For example if you want to get only current year or month or date etc. create a **getDateTime2.py** file with following content, which will help you to understand to fetch specific attribute.

```no-highlight
import datetime

currentDT = datetime.datetime.now()

print ("Current Year is: %d" % currentDT.year)
print ("Current Month is: %d" % currentDT.month)
print ("Current Day is: %d" % currentDT.day)
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)
print ("Current Microsecond is: %d" % currentDT.microsecond)
```
Now, execute script **getDateTime2.py **like below

```no-highlight
user@ubuntu:~$ python getDateTime2.py 

Current Year is: 2017
Current Month is: 3
Current Day is: 6
Current Hour is: 16
Current Minute is: 6
Current Second is: 28
```

#### Get Formated Date Time in Python
***
Also, if you need date and time in specific format, you can specify directive to format date and time. Create **getDateTime3.py** file with following content. This example have some sample formated date and time outputs.
```no-highlight
import datetime

currentDT = datetime.datetime.now()

print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
print (currentDT.strftime("%Y/%m/%d"))
print (currentDT.strftime("%H:%M:%S"))
print (currentDT.strftime("%I:%M:%S %p"))
print (currentDT.strftime("%a, %b %d, %Y"))
```
Now execute **getDateTime3.py** from command line
```no-highlight
rahul@tecadmin:~$ python getDateTime3.py 
2017-03-06 16:13:59
2017/03/06
16:13:59
04:13:59 PM
Mon, Mar 06, 2017
```

Below is the list of directives can be used to format date and time output in your Python script.


DIRECTIVE|MEANING
| -----------:
%a|Locale’s abbreviated weekday name.
%A|Locale’s full weekday name.
%b|Locale’s abbreviated month name.
%B|Locale’s full month name.
%c|Locale’s appropriate date and time representation.
%d|Day of the month as a decimal number [01,31].
%H|Hour (24-hour clock) as a decimal number [00,23].
%I|Hour (12-hour clock) as a decimal number [01,12].
%j|Day of the year as a decimal number [001,366].
%m|Month as a decimal number [01,12].
%M|Minute as a decimal number [00,59].
%p|Locale’s equivalent of either AM or PM.
%S|Second as a decimal number [00,61].
%U|Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w|Weekday as a decimal number [0(Sunday),6].
%W|Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x|Locale’s appropriate date representation.
%X|Locale’s appropriate time representation.
%y|Year without century as a decimal number [00,99].
%Y|Year with century as a decimal number.
%z|Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
%Z|Time zone name (no characters if no time zone exists).
%%|A literal '%' character.