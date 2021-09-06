import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(process)d %(levelname)s %(message)s")

class Mixin:
    def to_dict(self):
        logging.info(self.__dict__.items())
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith('_')

class InsideSample(Mixin):
    def __init__(self):
        self.name = "inside sample"
        self.description = "inside description text"
        self._private  = "inside private members"

class SampleClass(Mixin):
    def __init__(self):
        self.name = "name class"
        self.description = "description text"
        self.inside = InsideSample()
        self._private = "class private member"


s = SampleClass()
logging.info(s.to_dict())
