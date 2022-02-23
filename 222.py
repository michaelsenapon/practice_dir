def is_year_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    if (month == 2):
        if is_year_leap(year):
            return 29
        else:
            return 28
    months_length = [1, 3, 5, 7, 8, 10, 12]
    if month in months_length:
        return 31
    elif (month > 12):
        return None
    else:
        return 30
#
# Your code from LAB 4.3.1.7.
#

def day_of_year(year, month, day):
    days_length = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
