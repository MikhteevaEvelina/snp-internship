from datetime import datetime


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def date_in_future(integer):
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    today = str(datetime.now())
    year = int(today[0:4])
    month = int(today[5:7])
    day = int(today[8:10])
    time = today[11:19]
    if type(integer) != int:
        integer = 0
    while integer != 0:
        if leap_year(year):
            day_to_next_month = leap_day_in_month[month - 1] - day + 1
        else:
            day_to_next_month = day_in_month[month - 1] - day + 1
        if integer < day_to_next_month:
            day += integer
            integer = 0
        else:
            day = 1
            month = (month + 1) % 12
            if month == 0:
                month = 12
            if month == 1:
                year += 1
            integer -= day_to_next_month
    year = str(year)
    if len(str(month)) == 2:
        month = str(month)
    else:
        month = '0' + str(month)
    if len(str(day)) == 2:
        day = str(day)
    else:
        day = '0' + str(day)
    return day + '-' + month + '-' + year + ' ' + time


print(date_in_future([]))
print(date_in_future(2))
print(date_in_future(366))
