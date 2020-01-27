from datetime import datetime
from monthdelta import monthdelta

class Calendar:

    def paths(name, startDate, endDate):

        paths = []
        for date in Calendar.dates(startDate, endDate):
            paths.append('data/%s/%s/*.csv' % (name, date))

        return paths

    def dates(startDate, endDate):

        date = startDate

        endDatetime = datetime.strptime(endDate, "%Y-%m")

        while (datetime.strptime(date, "%Y-%m") <= endDatetime) :
            yield date

            date = (datetime.strptime(date, "%Y-%m") \
                    + monthdelta(1)) \
                     .strftime('%Y-%m')
