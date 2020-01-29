from pyspark.sql import functions as F
from Sequentiable import Sequentiable
from GraphObject import GraphObject
from Calendar import Calendar
import os

class MergedEdges:
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['cleanCommentsBucket']
        self.outBucket = cfg['s3']['mergedEdgesBucket']

    def merge(self, startDate, endDate):

        self.context \
        .read \
        .parquet \
        .load(Calendar.paths(self.inBucket, startDate, endDate)) \
        .groupBy('author_1', 'author_2') \
        .agg( {'weight' : 'sum'} ) \
        .withColumnRenamed('sum(weight)', 'weight') \
        .sort(F.desc('weight')) \
        .write \
        .parquet('s3a://%s/%s_%s' \
            % (self.outBucket, startDate, endDate))
