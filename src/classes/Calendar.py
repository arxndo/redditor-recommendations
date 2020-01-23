import os

class Calendar:

    def __init__(o, startMonth, startYear, endMonth, endYear):
        o.startMonth = startMonth
        o.startYear = startYear
        o.endMonth = endMonth
        o.endYear = endYear

    def dates(o):
        month = o.startMonth
        year = o.startYear 
        while o.withinBounds(month, year):
            yield month, year
            month, year = Calendar.advanceMonth(month, year) 
        
    def show(o):
        for month, year in o.dates():
            print('month = %d, year = %d' % (month, year) )

    @staticmethod
    def advanceMonth(month, year):
        month += 1
        if month == 13:
           month = 1
           year += 1
        return month, year

    def withinBounds(o, month, year):
        return (year < o.endYear) | ( (year == o.endYear) & (month <= o.endMonth) )

