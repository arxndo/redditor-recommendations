import yaml

class Configuration:
    """ Configuration includes ip addresses, s3 bucket names
    usernames, passwords, and other parameters
    (see config_template.yml"""
    
    @staticmethod
    def configuration(configName):

        with open(configName, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        return cfg
