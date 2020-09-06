import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.control import dehumidify_control

def dehumidify(request: dict) -> None:
    """
    Parameters
    ----------

    request: dict
        example: {"dehumidificationLevel": 1, "airflowLevel": "1"}
    """
    dehumidify_control(
        dehumidification_level = request['dehumidificationLevel'],
        airflow_level = request['airflowLevel']
    )
