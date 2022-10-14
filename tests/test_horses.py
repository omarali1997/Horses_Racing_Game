import pytest
from Horses_Racing_Game.classes import HorsesRacing


# #################### Tests #################### #
def test_horse_name(horse):
    kind = horse.set_name("Kind")
    assert horse.get_name() == "Kind"

def test_horse_breed(horse):
    american = horse.set_Breed("american")
    assert horse.get_Breed() == "american"

def test_horse_point(horse):
    horse_point = horse.set_point(40)
    assert horse.get_point() == 40

def test_horse_str(horse):
    kind=HorsesRacing()
    kind.set_name("Kind")
    kind.set_Breed("american")
    kind.set_point(40)
    assert str(kind) == "Kind (american): 40/100"

def test_horse_repr(horse):
    kind=HorsesRacing()
    kind.set_name("Kind")
    kind.set_Breed("american")
    kind.set_point(40)
    assert repr(kind) == "name= Kind, Breed= american point= 40, high_point= 100"
    

# #################### Fixtures #################### # 

@pytest.fixture
def horse():
    horse1 = HorsesRacing()
    return horse1

def contender():
    pass