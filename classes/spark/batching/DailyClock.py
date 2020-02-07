from datetime import datetime, timedelta
from monthdelta import monthdelta
from calendar import monthrange

class DailyClock:
    """ Helper functions for iterating over multiple dates"""

    @staticmethod
    def s3paths(bucket, startDate, endDate):
        """ Paths in s3 bucket between two dates"""

        paths = []
        for date in DailyClock.dates(startDate, endDate):
            paths.append('s3a://%s/%s' % (bucket, date))
        return paths

    @staticmethod
    def startOfMonth(date):
        return date + '-01'

    @staticmethod
    def endOfMonth(date):
        date = datetime.strptime(date, '%Y-%m')
        (_, lastDay) = monthrange(date.year, date.month)
        return '%d-%.2d-%.2d' % (date.year, date.month, lastDay)

    @staticmethod
    def toUTC(date):
        return int(datetime.strptime(date, '%Y-%m-%d').timestamp())

    @staticmethod
    def nextDate(date):
        return (datetime.strptime(date, '%Y-%m-%d')+ timedelta(1)) \
                        .strftime('%Y-%m-%d') 

    @staticmethod
    def monthDates(date):
        """ Iterates through all dates within a given month"""
        date = date + '-01'

        endDate = datetime.strptime(date, '%Y-%m-%d') + monthdelta(1)

        while (datetime.strptime(date, "%Y-%m-%d") < endDate) :
            yield date

            date = (datetime.strptime(date, "%Y-%m-%d") \
                    + timedelta(1)) \
                     .strftime('%Y-%m-%d')

    def dates(self, startDate, endDate):
        """ Iterates through all months between two dates"""
        date = DailyClock.startOfMonth(startDate)

        endDate = DailyClock.endOfMonth(endDate)

        while (datetime.strptime(date, "%Y-%m-%d") <= endDate) :
            yield date

            date = (datetime.strptime(date, "%Y-%m-%d") \
                    + timedelta(1)) \
                     .strftime('%Y-%m-%d')
