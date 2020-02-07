import os
from Configuration import Configuration
from MyContext import MyContext

class Executor:

    @staticmethod
    def run(className):

        os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
        os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

        exec('from %s import %s' % (className, className))
        
        cfg = Configuration.configuration('config.yml')

        context = MyContext().context(cfg, '%s%s_%s' \
                        % (className, cfg['dates']['startDate'], cfg['dates']['endDate']))

        exec('item = %s(cfg, context)' % className)

        exec( 'item.process(cfg["dates"]["startDate"], cfg["dates"]["endDate"])' )

