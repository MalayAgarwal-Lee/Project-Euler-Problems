'''
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

--> 1 Jan 1900 was a Monday.
--> Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
--> A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''



months = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def countSundays(years, startDay):
    sundayCount = 0
    for year in years:

        leapYear = False
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            leapYear = True

        monthStartDay = startDay

        for month in range(1, 13):
            if monthStartDay == 7:
                sundayCount += 1

            if month in months.keys():
                monthStartDay += 2 if months[month] == 30 else 3
            elif leapYear:
                monthStartDay += 1

            if monthStartDay > 7:
                monthStartDay -= 7

        startDay += 2 if leapYear else 1

        if startDay > 7:
            startDay -= 7

    return sundayCount

def main():
    years = list(map(lambda x: x, range(1901, 2001)))
    totalSundays = countSundays(years, 2)
    print(totalSundays)

if __name__ == '__main__':
    main()