class AirConditionerError(Exception):
    def __init__(self, error, message):
        self.error = error
        self.message = message
    pass

class InvalidTypeError(AirConditionerError): pass
class InvalidAirfolwLevel(AirConditionerError): pass
class InvaliddeHumidificationLevel(AirConditionerError): pass

class KeyNotExist(Exception): pass
