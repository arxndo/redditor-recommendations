from Calendar import Calendar

class Mergeable:

    def paths(self, startDate, endDate):

        paths = []
        for date in Calendar.dates(startDate, endDate):
            paths.append('data/%s/%s/*.csv' % (self.name, date))

        return paths

    def merge(self, startDate, endDate):

        df = self.context \
            .read \
            .format('csv') \
            .load(self.paths(startDate, endDate)) \
            .groupBy('_c0') \
            .agg( {'_c1' : 'sum'} ) \
            .write \
            .csv('data/%s/%s_%s' % (self.name, startDate, endDate))
