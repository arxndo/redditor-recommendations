class RawInput:
    
    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date)
        return self
