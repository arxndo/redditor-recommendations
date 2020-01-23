import sys
sys.path.insert(0, 'src/classes')
sys.path.insert(0, '../classes')
from Calendar import Calendar

calendar = Calendar( startMonth = 5, \
                            startYear = 2005, \
                            endMonth = 2, \
                            endYear = 2006 )
calendar.show()

