from src.utils.MonthlyClock import MonthlyClock
import unittest

class DailyClock_test(unittest.TestCase):

    def testDates(self):
        startDate = '2009-02'
        endDate = '2010-05'
        
        year1Base = '2009'
        year2Base = '2010' 

        year1List = []
        for i in range(2,13):
            year1List.append('%s-%.2d' % (year1Base, i))
        
        year2List = []
        for i in range(1,6):
            year2List.append('%s-%.2d' % (year2Base, i))
    
        trueDates = year1List + year2List

        for date, trueDate \
            in zip(MonthlyClock().dates(startDate, endDate), \
            trueDates):
                self.assertEqual(date, trueDate)

if __name__ == '__main__':
    unittest.main()
