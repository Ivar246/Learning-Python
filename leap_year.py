def is_leap(year):
    if year%4 == 0:
        if year%100:
            if year%400:
                return False
            else: 
                return False
        else:
            return True
    else:
        return False
        
def days_in_month(year, month):     
    month_days = [31, 28, 31, 30, 30, 31, 32, 31, 30, 30, 31, 30]  
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]


year = int(input('Enter year: '))
month = int(input('Enter month:'))
days = days_in_month(year, month)
print(days)