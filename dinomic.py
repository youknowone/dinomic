
"""Dinomic injects dynamic invocation handler for python object when attributes
are not accessible.
"""


class MetaDinomic(type):
    """This is a metaclass. Use `Dinomic` for normal subclassing."""

    def __init__(cls, *args, **kwargs):
        def getattribute(self, name):
            sup = super(cls, self)
            try:
                r = sup.__getattribute__(name)
            except AttributeError as e:
                try:
                    r = self.__missattr__(name)
                except AttributeError:
                    pass
                else:
                    return r
                raise e
            else:
                return r

        super(MetaDinomic, cls).__init__(*args, **kwargs)

        cls.__getattribute__ = getattribute


class Dinomic(object):
    """Inherit this class to inject your object."""

    __metaclass__ = MetaDinomic