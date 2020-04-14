# 1er janvier 1901 est un mardi
year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
leap_year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


sundays_counter = 0
Year = 1901
Day = 0
while Year != 2001:
    Month = 0
    Day_year = 0
    if Year % 4 != 0:
        while Day_year < 365:
            Month += 1
            Day_month = 0
            while Day_month < year[Month]:
                Day_year += 1
                Day_month += 1
                Day += 1
                if (Day-6) % 7 == 0 and Day_month == 1:
                    sundays_counter +=1
    else:
        while Day_year < 366:
            Month += 1
            Day_month = 0
            while Day_month < leap_year[Month]:
                Day_year += 1
                Day_month += 1
                Day += 1
                if (Day-6) % 7 == 0 and Day_month == 1:
                    sundays_counter +=1
    Year += 1
    
print(Day)
print(sundays_counter)