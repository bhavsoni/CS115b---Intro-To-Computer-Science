'''
Created on ___________4/17/17____________
@author:   _________Bhavin Soni______________
Pledge:    ___I pledge my honor that I have abided by the Stevens Honor System____________________

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
DAYS_IN_WEEK = ( 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and self.day == d2.day
    
    def tomorrow(self):
        '''change the calling object so that it represents one calendar day after the date it originally represented'''
        if self.isLeapYear() and self.month == 2 and self.day == 28: #if the date is a leap year and its feb 28 then feb has 29 days so add 1 day
            self.day += 1
        elif DAYS_IN_MONTH[self.month] < (self.day + 1): #if the days in that month is less than the next day, then subtract those days in that month to rest it day 0, add one day and add one month
            if self.isLeapYear() and self.month == 2 and self.day == 29:
                self.day -= DAYS_IN_MONTH[self.month]
            else:
                self.day -= DAYS_IN_MONTH[self.month]
                self.day += 1
            self.month += 1
            if self.month == 13: #if the month becomes 13 (after december) then subtract that from 12 to return to january and then add 1 to the year
                self.month = self.month - 12
                self.year += 1
        else:
            self.day += 1 #else just add 1 to the day
    
    def yesterday(self):
        '''it should change the calling object so that it represents one calendar day before the date it originally represented.'''
        if self.isLeapYear() and self.month == 3 and self.day == 1: #takes account for leap year for feburary
            self.day = 29
            self.month -= 1
        elif self.month == 1 and self.day == 1: #if its new years then yesterday is one less year previous month and day is 31
            self.year -= 1
            self.month = 12
            self.day = 31
        elif self.day == 1:
            self.day = DAYS_IN_MONTH[self.month - 1] #if its the first of the month yesterday is the last months last day and subtract one month
            self.month -= 1
        else:
            self.day -= 1 #else just subtract 1 from each day
    
    def addNDays(self, N):
        ''' change the calling object so that it represents N calendar days after the date it originally represented.'''
        print(self) #print the initial day
        for i in range(N): # for every day added i in range of N add tomorrow print that date and subtract 1 from i(acts as a counter)
            self.tomorrow()
            print(self)
            i -= 1
    
    def subNDays(self,N):
        '''change the calling object so that it represents N calendar days before the date it originally represented'''
        print(self) #same exact thing as above except use yesterday function to subtract n days
        for i in range(N):
            self.yesterday()
            print(self)
            i -= 1
        
    def isBefore(self, d2):
        '''This method should return True if the calling object is a calendar date before the input
        named d2 (which will always be an object of type Date). If self and d2 represent the same day, 
        this method should return False. Similarly, if self is after d2, this should return False.'''
        if self.year == d2.year and self.month == d2.month and self.day == d2.day: #if the 2 dates are the same return false
            return False
        if self.year > d2.year: #if the year of the first date is greater than that of the second date then return false
            return False
        elif self.year < d2.year: #if the year of the first date is less than that of the second date then return true
            return True
        else: 
            if self.month > d2.month: #if the years are the same, then compare months
                return False #if first date month is greater than the second date then return false
            elif self.month < d2.month: #if its the opposite then return true
                return True
            else: #if the months are the same then compare days
                if self.day < d2.day:#if the day of the first date is less than the second date then return true
                    return True
                else:
                    return False #else return false
    
    def isAfter (self,d2):
        '''This method should return True if the calling object is a calendar date after the input
        named d2 (which will always be an object of type Date). If self and d2 represent the same day, 
        this method should return False. Similarly, if self is before d2, this should return False.'''  
        if self.year == d2.year and self.month == d2.month and self.day == d2.day: #if the two dates are equal then return false
            return False
        if self.year > d2.year: #same exact thing as above but switch up the True and False for each statement 
            return True
        elif self.year < d2.year:
            return False
        else:
            if self.month > d2.month: #if years are the same compare months
                return True
            elif self.month < d2.month:
                return False
            else:
                if self.day < d2.day: #if months are the same compare days
                    return False
                else:
                    return True
        
    def diff(self, d2):
        '''This method should return an integer representing the number of days between self and d2'''
        if self.year == d2.year and self.month == d2.month and self.day == d2.day: #if the dates are the same then the difference between them is 0
            return 0
        d = Date(self.month, self.day, self.year) #initialize d as a date 
        i = 0 #i is a counter for the amount days as difference between two days
        while not d.equals(d2): #while the two days are different
            if d.isBefore(d2): #if the first date is before the second date count down (negative) and keep adding a day until reaching the second date using tomorrow()
                i -= 1
                d.tomorrow()
            elif d.isAfter(d2): #if the first date is after the second date count up (positive) and keep adding a day until reaching the second date using yesterday()
                i += 1
                d.yesterday()
        return i #return i which is the number of days in difference
    
    def dow(self):
        '''This method should return a string that indicates the day of the week (dow) of the object (of type Date) that calls it.'''
        reference = Date(1,1,2017) #use jan 1 2017 as a reference. this is a sunday.
        diff = self.diff(reference) #the difference in days between the reference and the date 
        return DAYS_IN_WEEK[diff % 7] #use the difference and mod (mod will determine the remainder and correlate that to the DAYS_IN_WEEK - 0=sunday, 6=saturday) to find day of the week in regards to the reference date. DAYS_IN_WEEK must start with sunday.
 




d = Date(11,2,2010)
d.addNDays(5)

