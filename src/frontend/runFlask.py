#import importPaths
import sys
sys.path.insert(0, '~/redditor-recommendations')

from flaskApp import app
app.run('0.0.0.0', 80)

