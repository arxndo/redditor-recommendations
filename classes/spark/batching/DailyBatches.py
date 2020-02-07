from Batches import Batches
from DailyClock import DailyClock

class DailyBatches(Batches):

    def __init__(self):
        super().__init__(self, DailyClock())
