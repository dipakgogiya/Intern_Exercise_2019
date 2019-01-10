import calendar
from datetime import date, timedelta

print("1. calendar(year, w, l, c):")
print("2. firstweekday():")
print("3. isleap (year):")
print("4. leapdays (year1, year2):")
print("5. month (year, month, w, l):")
print("6. Identify weekday of given date and which weekday of month. ")
print("7. get date of all Saturday of month & two specific date:")
print("8. Get weekday of first date and last date of month.")
print("9. calendar.monthrange(year, month)")

while(True):
    number = int(input("Enter the number to perform operation given below:"))
    if number == 1:
        # 1. calendar(year, w, l, c)
        year = int(input("Enter The Year Is:"))
        print("The Calender Year", year, "Is:")
        print(calendar.calendar(year,2,1,6))
        print(calendar.calendar(year))
    
    elif number == 2:
        # 2. firstweekday()
        print("The starting day number in calendar is:")
        print(calendar.firstweekday()) #It print starting day number
    elif number == 3:
        # 3. isleap (year)
        if calendar.isleap(year): # To print the year is leap or not
            print("Year is Leap:")
        else:    print("Year is not leap:")
    elif number == 4:
        #4. leapdays(year1,year2) 
        print("Enter The Two years to print in between total leap days:")
        year1 = int(input("Enter The Year1 Is:"))
        year2 = int(input("Enter The Year2 Is:"))
        print("The Leap Day between", year1, "and", year2, "Are :- ")
        print(calendar.leapdays(year1,year2))
    elif number == 5:
        #5. month (year, month, w, l)
        year = int(input("Enter The Year:"))
        month = int(input("Enter The Month "))
        print("The Month ",month,"th of",year, "Is :-")
        print(calendar.month(year,month))
    elif number == 6:
        #Identify weekday of given date and which weekday of month.
        date = int(input("Enter The Date:"))
        month = int(input("Enter The Month:"))
        year = int(input("Enter The Year:"))
        print("The weekday is:",calendar.weekday(year, month, day),"It is ",list(calendar.day_name)[calendar.weekday(year,month,date)])
        
    elif number == 7:
        #get date of all Saturday of month & two specific date.
        def all_suturday(year):
            """
            @Func :- It will find all the saturday specified in the year
            @Param :- year is the year number and it's type is integer.
            """
        # January Starting Of The Year
            dt = date(year, 1, 1)
            print dt
        # First Saturday of the given year       
            dt += timedelta(days = 5 - dt.weekday())
            print dt
            while dt.year == year:
                yield dt
                dt += timedelta(days = 7)
                  
        year = int(input("Enter the year :- "))
        print(calendar.calendar(year))
        for s in all_suturday(year):
           print(s)
            
    elif number == 8:
        #Get weekday of first date and last date of month.
        year = int(input("Enter The Year:"))
        month = int(input("Enter The Month:"))
        print(calendar.monthrange(year, month))
        
    elif number ==9:
        exit()
        