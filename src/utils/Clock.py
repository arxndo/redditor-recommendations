from datetime import datetime, timedelta

class Clock:
    """ Abstract class whose concrete instantiations
    specify the temporal order in which data is processed"""

    def __init__(self):
        pass


    def startOfMonth(date):
        pass


    def endOfMonth(date):
        pass


    def nextDate(date):
        pass

    
    def s3paths(self, bucket, startDate, endDate):
        """ s3 file names between two dates """

        paths = []
        for date in self.dates(startDate, endDate):
            paths.append('s3a://%s/%s' % (bucket, date))
        return paths


    def dates(self, startDate, endDate):
        """ Generator yielding all dates between two dates """

        date = self.startOfMonth(startDate)

        endDate = self.endOfMonth(endDate)

        endDateStamp = datetime.strptime(endDate, self.dateFormat)

        while (datetime.strptime(date, self.dateFormat) <= endDateStamp) :
            yield date
            date = self.nextDate(date)
