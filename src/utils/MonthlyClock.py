from datetime import datetime
from monthdelta import monthdelta
from src.utils.Clock import Clock

class MonthlyClock(Clock):
    """ Clock for iterating through monthly batched data"""

    def __init__(self):
        super().__init__
        self.dateFormat = '%Y-%m'

    def startOfMonth(self, date):
        return date

    def endOfMonth(self, date):
        return date

    def nextdate(self, date):
        return (datetime.strptime(date, self.dateFormat)+ monthdelta(1)) \
                        .strftime(self.dateFormat) 


    def dates(self, startDate, endDate):
        """ Iterates through all months between two dates"""
        date = startDate

        endDatetime = datetime.strptime(endDate, "%Y-%m")

        while (datetime.strptime(date, "%Y-%m") <= endDatetime) :
            yield date

            date = (datetime.strptime(date, "%Y-%m") \
                    + monthdelta(1)) \
                     .strftime('%Y-%m')
