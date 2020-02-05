from datetime import datetime, timedelta
from monthdelta import monthdelta

class Diary:
    """ Helper functions for iterating over multiple dates"""

    @staticmethod
    def s3paths(bucket, startDate, endDate):
        """ Paths in s3 bucket between two dates"""

        paths = []
        for date in Diary.dates(startDate, endDate):
            paths.append('s3a://%s/%s' % (bucket, date))
        return paths


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

    @staticmethod
    def dates(startDate, endDate):
        """ Iterates through all months between two dates"""
        date = startDate

        endDatetime = datetime.strptime(endDate, "%Y-%m-%d")

        while (datetime.strptime(date, "%Y-%m-%d") <= endDatetime) :
            yield date

            date = (datetime.strptime(date, "%Y-%m-%d") \
                    + timedelta(1)) \
                     .strftime('%Y-%m-%d')
