from src.utils.DailyClock import DailyClock
import unittest

class DailyClock_test(unittest.TestCase):

    def testDates(self):
        startDate = '2009-02'
        endDate = '2009-03'
        
        februaryBase = '2009-02'
        marchBase = '2009-03' 

        februaryList = []
        for i in range(1,29):
            februaryList.append('%s-%.2d' % (februaryBase, i))
        
        marchList = []
        for i in range(1,32):
            marchList.append('%s-%.2d' % (marchBase,i))
    
        trueDates = februaryList + marchList

        for date, trueDate \
            in zip(DailyClock().dates(startDate, endDate), \
            trueDates):
                self.assertEqual(date, trueDate)

if __name__ == '__main__':
    unittest.main()
