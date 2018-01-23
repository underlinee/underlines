import os
import configparser
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
import __root__

if 'MODE' in os.environ:
    mode = os.environ['MODE']
else:
    mode = "DEFAULT"

all_configs = configparser.ConfigParser()
all_configs.read(os.path.join(__root__.path(), 'config.ini'))
config = all_configs[mode]

def get(name):
    return config[name]