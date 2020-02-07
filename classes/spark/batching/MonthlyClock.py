from datetime import datetime
from monthdelta import monthdelta

class MonthlyClock:
    """ Helper functions for iterating over multiple dates"""

    @staticmethod
    def s3paths(bucket, startDate, endDate):
        """ Paths in s3 bucket between two dates"""

        paths = []
        for date in MonthlyClock.dates(startDate, endDate):
            paths.append('s3a://%s/%s' % (bucket, date))
        return paths


    def dates(startDate, endDate):
        """ Iterates through all months between two dates"""
        date = startDate

        endDatetime = datetime.strptime(endDate, "%Y-%m")

        while (datetime.strptime(date, "%Y-%m") <= endDatetime) :
            yield date

            date = (datetime.strptime(date, "%Y-%m") \
                    + monthdelta(1)) \
                     .strftime('%Y-%m')
