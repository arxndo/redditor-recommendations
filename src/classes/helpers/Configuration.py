import yaml

class Configuration:
    
    @staticmethod
    def configuration(configName):

        with open(configName, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        return cfg
