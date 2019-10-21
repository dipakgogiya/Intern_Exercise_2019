import time,datetime
from dateutil.tz import *
import pytz
from pytz import timezone
#NOTE :- https://www.journaldev.com/18745/python-datetime

print("1.Get Current Date and Print it in various format like DD/MM/YY, YY/MM/DD, MM-DD-YY, DD-MM-YY, YY-DD-MM")
print("2.Get Current month, current date, current week day, current year, and add hours, minutes, days, month and years in it.")
print("3.Get local timezone and current  UTC time. and Convert it in local timezone. also convert it in other timezone.")
print("4.Convert time to string and string to time")
print("5.Combine date and time object with timezone")
print("6.Get Current month name from date")
print("7.Get time in 12-hour clock & 24-hour clock")
print("8.Get Datetime with century number and without century number. ie. 2018 & 18.")
print("9.Get Locale equivalent of either (AM or PM.) from Date.")
print("10.Get Day of year from date time. (01,...366)")
print("11.Get Week number of year by both (Sunday as First Day of week & Monday as First Day of week).")
print("12.Addition of 2 Date times")
print("13. Difference of 2 Date times")
print("14. Multiplication of time with integer & Float.")
print("15. Division of time with integer & Float.")
print("16. Difference of 2 date time.quotient and the remainder. (divmod(t1, t2)). and get output of it in Various units. like hours, minutes, Days, months, seconds.")

while(True):
    number = int(input("Enter The Number to perform The Operation given in the operation :- "))
    if number == 1:
        #Get Current Date and Print it in various format like DD/MM/YY, YY/MM/DD, MM-DD-YY, DD-MM-YY, YY-DD-MM
        print datetime.datetime.now()
        print "The Format Is DD/MM/YY:",datetime.datetime.now().strftime("%d/%m/%y")
        print "The Format Is YY/MM/DD:",datetime.datetime.now().strftime("%y/%m/%d")
        print "The Format Is MM-DD-YY:",datetime.datetime.now().strftime("%m/%d/%y")
        print "The Format Is YY-DD-MM:",datetime.datetime.now().strftime("%y/%d/%m")
        print "The Format Is YYYY-DD-MM:",datetime.datetime.now().strftime("%Y/%d/%m")
    if number == 2:
        print("Current Date Time Is:",datetime.datetime.now())
        print "Current Month :- ",datetime.date.today().strftime("%B")
        print "Current Date :- ",datetime.date.today().strftime("%d")
        print "Current Week Day :- ",datetime.date.today().strftime("%A")
        print "Current Year :- ",datetime.date.today().strftime("%Y")
    elif number == 3:
       # This contains the local timezone 
        #local = tzlocal()
        now = datetime.datetime.now() # It return the local timezone
        now = now.replace(tzinfo = tzlocal())
        # prints a timezone aware datetime

        print "Local Time Zone:",now #Asia/Kolkata TimeZone
        
        #utc = tzutc()
        utc_now = now.astimezone(tzutc())
        print "current  UTC time :- ",utc_now
        
        fmt = "%Y-%m-%d %H:%M:%S %Z%z"
        
        # Current time in UTC
        now_utc = datetime.datetime.now(timezone('UTC'))
        print now_utc.strftime(fmt)
        
        # Convert to US/Pacific time zone
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        print now_pacific.strftime(fmt)
        
        # Convert to Europe/Berlin time zone
        now_berlin = now_pacific.astimezone(timezone('Europe/Berlin'))
        print now_berlin.strftime(fmt)
        """
        #get All TimeZones
        from pytz import all_timezones
        
        print len(all_timezones)
        for zone in all_timezones:
            if 'US' in zone:
                print zone
        
        """        
    elif number == 4:
       date_time = datetime.datetime.now().time()
       print date_time,type(date_time) #datetime.time format
       str_date_time = date_time.strftime("%H:%M:%S") #Convert date_time into String 
       print str_date_time,type(str_date_time) #String format
       print(datetime.datetime.strptime(str_date_time,"%H:%M:%S"),type(datetime.datetime.strptime(str_date_time,"%H:%M:%S")))
       
       
    elif number == 5:
        #Workinf with current date and time and combine it.
        date = datetime.date.today()
        time = datetime.datetime.now().time()
        time = datetime.time(time.hour,time.minute,time.second, tzinfo=pytz.timezone('Europe/London'))
        aware_datetime = datetime.datetime.combine(date, time) #Combine Function Only combine datetime object not string
        print aware_datetime
    elif number == 6:
        #Get Current month name from date
        print datetime.datetime.now().strftime("%B")
    elif number == 7:
        print datetime.datetime.now().time().strftime("%H:%M:%S") # Hour (24-hour clock)
        print datetime.datetime.now().time().strftime("%I:%M:%S") # Hour (12-hour clock)
    elif number == 8:
        print datetime.datetime.now().strftime("%y/%m/%d") # Get Datetime without century number
        print datetime.datetime.now().strftime("%Y/%m/%d") # Get Datetime with century number
    elif number == 9:
        print datetime.datetime.now().strftime("%y/%m/%d,%H:%M:%S,%p")
    elif number == 10:
        print datetime.datetime.now().strftime("%Y,%j") #Get Day of year from date time. (01,...366)
    elif number == 11:
        print datetime.datetime.now().strftime("%Y,%w")
        print datetime.datetime.now().strftime("%Y,%W")
    elif number == 12:
        #Addition of 2 Date times
        date1 = datetime.date.today()
        date2 = date1 + datetime.timedelta(days = 365)
        print "Current Date :- ",date1
        print "After Addition Of Date :- ",date2
    elif number == 13:
        t1 = datetime.datetime.now()
        #t1 = datetime.datetime(2017, 1, 31, 14, 17)
        t2 = datetime.datetime(2015, 12, 15, 16, 59)
        delta = t1 - t2
        print "Subtract DateTimes :- ",delta
    elif number == 14:
          d1 = datetime.datetime(1990, 1, 1)
          print d1 + 2 * datetime.timedelta(182.5)
    elif number == 15:
        d1 = datetime.datetime(1991, 1, 1)
        print d1 - datetime.timedelta(365) / 2    
    elif number == 16:
        first = datetime.datetime(1981, 6, 16, 4, 35, 25)
        second  = datetime.datetime(1973, 1, 18, 3, 45, 50)
        
        difference = first - second
        
        weeks,days = divmod(difference.days,7)
        minute,seconds = divmod(difference.seconds,60)
        
        hours,minute = divmod(minute, 60)
        
        print "There were ",difference.days,"between first and second"
        print "%d weeks, %d days, %d:%d:%d" % (weeks,days,hours,minute,seconds) 
    else:
        print "Invalid Choice..Please Try Again"
      
        
        
        
        
        