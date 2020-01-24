import os

class Calendar:

    def __init__(self, startMonth, startYear, endMonth, endYear):
        self.startMonth = startMonth
        self.startYear = startYear
        self.endMonth = endMonth
        self.endYear = endYear

    def dates(self):
        month = self.startMonth
        year = self.startYear 
        while self.withinBounds(month, year):
            yield month, year
            month, year = Calendar.advanceMonth(month, year) 
        
    def show(self):
        for month, year in self.dates():
            print('month = %d, year = %d' % (month, year) )

    @staticmethod
    def advanceMonth(month, year):
        month += 1
        if month == 13:
           month = 1
           year += 1
        return month, year

    def withinBounds(self, month, year):
        return (year < self.endYear) | ( (year == self.endYear) & (month <= self.endMonth) )

