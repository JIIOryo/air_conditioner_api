from typing import Any, List
import json
import os
import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from lib.errors import (
    KeyNotExist,
)

PROJECT_ROOT_PATH = os.path.join(os.path.dirname(__file__), '../')
CONFIG_PATH = '/'.join([
    PROJECT_ROOT_PATH,
    'config.json',
])

def read_json(json_path: str) -> dict:
     with open(json_path) as f:
         return json.load(f)

def get_config() -> dict:
    return read_json(CONFIG_PATH)

def get_config_items(keys: List[str]) -> dict:
    config = get_config()
    result = {}
    for key in keys:
        if key not in config:
            raise KeyNotExist('key: {key} does not exist.'.format(key = key))
        result[key] = config[key]
    return result

def get_config_item(key: str) -> Any:
    return get_config_items([key])[key]
