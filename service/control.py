import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from lib.run import run_air_conditioner
from lib.config import get_config
from lib.consts import (
    AIR_FLOW_LEVELS,
    DEHUMIDIFICATION_LEVELS,
)
from lib.errors import (
    InvalidTypeError,
    InvalidAirfolwLevel,
    InvaliddeHumidificationLevel,
)

def control_by_temperature(type_: str, temperature: int, airflow_level: str) -> None:
    _type_validation(type_)
    _airflow_level_validation(airflow_level)
    
    config = get_config()
    project_root_path = config['project_root_path'].rstrip('/')
    
    run_air_conditioner(
        irrppy_path = '/'.join([project_root_path, 'irrp.py']),
        command_file_path = '/'.join([
            project_root_path,
            'signal',
            config['product_name'],
            f'{type_}.json'
        ]),
        gpio = config['ir_led_gpio_bcm'],
        command = f'{temperature}:{airflow_level}',
    )

def dehumidify_control(dehumidification_level: int, airflow_level: str) -> None:
    _dehumidification_level_validation(dehumidification_level)
    _airflow_level_validation(airflow_level)
    
    config = get_config()
    project_root_path = config['project_root_path'].rstrip('/')
    dehumidification_level_cmd = DEHUMIDIFICATION_LEVELS[dehumidification_level]
    
    run_air_conditioner(
        irrppy_path = '/'.join([project_root_path, 'irrp.py']),
        command_file_path = '/'.join([
            project_root_path,
            'signal',
            config['product_name'],
            'dehumidify.json'
        ]),
        gpio = config['ir_led_gpio_bcm'],
        command = f'{dehumidification_level_cmd}:{airflow_level}',
    )

# private functions

def _airflow_level_validation(airflow_level: str):
    if airflow_level not in AIR_FLOW_LEVELS:
        raise InvalidAirfolwLevel(
            error = 'InvalidAirfolwLevel',
            message = f'airflow_level {airflow_level} is invalid.'
        )

def _type_validation(type_: str):
    types = ['hot', 'cool']
    if type_ not in types:
        raise InvalidTypeError(
            error = 'InvalidTypeError',
            message = f'type {type_} is neither "hot" nor "cool".'
        )

def _dehumidification_level_validation(dehumidification_level: int):
    if dehumidification_level not in DEHUMIDIFICATION_LEVELS:
        raise InvaliddeHumidificationLevel(
            error = 'InvaliddeHumidificationLevel',
            message = f'dehumidification_level {dehumidification_level} is invalid.'
        )
