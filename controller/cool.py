import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.control import control_by_temperature

def cool(request: dict) -> None:
    """
    Parameters
    ----------

    request: dict
        example: {"temperature": 26, "airflowLevel": "1"}
    """
    control_by_temperature(
        type_ = 'cool',
        temperature = request['temperature'],
        airflow_level = request['airflowLevel']
    )
