
from dinomic import Dinomic


class Plain(Dinomic):
    def __init__(self):
        self.x = 10

    def __missattr__(self, name):
        if name == 'y':
            return 40
        if name == 'no':
            raise AttributeError
        return 50


def test_plain():
    x = Plain()
    assert x.x == 10
    assert x.y == 40
    assert x.z == 50
    try:
        x.no
    except AttributeError as e:
        assert str(e) == "'Plain' object has no attribute 'no'"
