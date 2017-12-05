months = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 30}

def countSundays(years, startDay):
    sundayCount = 0
    for year in years:
        monthStartDay = startDay
        for month in range(1, 13):
            if monthStartDay == 7:
                sundayCount += 1

            if month in months.keys():
                monthStartDay += 2 if months[month] == 30 else 3

            if monthStartDay > 7:
                monthStartDay -= 7

        if not (year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)):
            startDay += 1
        else:
            startDay += 2

        if startDay > 7:
            startDay = 1

    return sundayCount

def main():
    years = list(map(lambda x: x, range(1901, 2001)))
    totalSundays = countSundays(years, 2)
    print(totalSundays)

if __name__ == '__main__':
    main()