from Batches import Batches
from MonthlyClock import MonthlyClock

class MonthlyBatches(Batches):

    def __init_(self):
        super().__init__(self, MonthlyClock())
