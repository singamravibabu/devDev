# WORKING WITH DATES AND TIMES

> Use the 'datetime' module to work with date, time, datetime values
### 'datetime' contains three constructors
### 'date' constructor to construct dates
### 'time' constructor to construct times
### 'datetime' constructor to construct datetime

## Parsing strings
### strptime() - the 'p' in the method stands for parsing
### we can parse the date/time/datetime from a given text
### syntax: datetime.strptime(datetime_str, format_str)
### format codes:
```
%d      Day of month as a number
%m      Month as a number
%y      2-digit year
%Y      4-digit year
%H      Hour of day in 24-hour format
%M      Minute as a number
%S      Second as a number

## Formatting date/time/datetime
### strftime()