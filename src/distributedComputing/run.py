""" Execute the 'process' method of any class that has one """

from Executor import Executor
import sys

className = sys.argv[1]

Executor.run(className)
