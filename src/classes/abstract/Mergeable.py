class Mergeable:

    def merge(self, startDate, endDate):
        df = self.context \
            .read \
            .format('csv') \
            .load('data/%s/2005-12/*.csv' % self.name) \
            .groupBy('%s' % self.column1Name) \
            .agg( {'sum(%s)' % self.column2Name : 'sum'} ) \
            .write \
            .option('header', 'true') \
            .csv('data/%s/%s.csv' % (self.name, self.name))
