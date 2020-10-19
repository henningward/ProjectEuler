import time

# https://projecteuler.net/problem=16
# Power digit sum

def firstDayOfMonths(year):
    jan = 31
    feb = 28
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31

    if IsLeapYear(year):
        feb = 29

    res = [1, jan + 1]
    res.append(res[-1] + feb)
    res.append(res[-1] + mar)
    res.append(res[-1] + apr)
    res.append(res[-1] + may)
    res.append(res[-1] + jun)
    res.append(res[-1] + jul)
    res.append(res[-1] + aug)
    res.append(res[-1] + sep)
    res.append(res[-1] + oct)
    res.append(res[-1] + nov)
    res.append(res[-1])
    return res
    
def IsLeapYear(year):
    if (year % 4 == 0):
        if not (year % 100 == 0):
            return True
        elif (year % 400 == 0):
            return True
    return False

def problem19():
    totalSundays = 0
    dayIndex = 1
    for year in range(1901, 2001):
        days = 366
        firstDays = firstDayOfMonths(year)
        if IsLeapYear(year):
            days = 366
        for day in range(1, days):
            dayIndex = dayIndex + 1
            if dayIndex % 7 == 0:
                if day in firstDays:
                    totalSundays = totalSundays + 1
    print(totalSundays)
     
                



start_time = time.time()
problem19()
print("--- %s seconds ---" % (time.time() - start_time))

