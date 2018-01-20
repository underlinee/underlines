import os
import configparser

if 'MODE' in os.environ:
    mode = os.environ['MODE']
else:
    mode = 'DEFAULT'

all_configs = configparser.ConfigParser()
all_configs.read('../../config.ini')
config = all_configs[mode]

def get(name):
    return config[name]