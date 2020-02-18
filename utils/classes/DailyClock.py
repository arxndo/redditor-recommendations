from datetime import datetime, timedelta
from monthdelta import monthdelta
from calendar import monthrange
from utils.classes.Clock import Clock

class DailyClock(Clock):
    ''' Clock for iterating through daily batched data'''

    def __init__(self):
        super().__init__
        self.dateFormat = '%Y-%m-%d'

    def startOfMonth(self, date):
        return date + '-01'

    def endOfMonth(self, date):
        date = datetime.strptime(date, '%Y-%m')
        (_, lastDay) = monthrange(date.year, date.month)
        return '%d-%.2d-%.2d' % (date.year, date.month, lastDay)

    def toUTC(date):
        return int(datetime.strptime(date, self.dateFormat).timestamp())

    def nextDate(self, date):
        return (datetime.strptime(date, self.dateFormat)+ timedelta(1)) \
                        .strftime(self.dateFormat) 

    def monthDates(self, date):
        """ Iterates through all dates within a given month"""
        return self.dates(date, date)
