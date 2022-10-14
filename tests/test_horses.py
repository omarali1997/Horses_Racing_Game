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

def test_contender_str(contender):
    assert str(contender) == "king (arabian): 70/100"

def test_horse_str_repr():
    kind=HorsesRacing()
    kind.set_name("Kind")
    kind.set_Breed("american")
    kind.set_point(40)
    assert str(kind) == "Kind (american): 40/100"
    assert repr(kind) == "name= Kind, Breed= american point= 40, high_point= 100"


def test_tie(horse,contender):
    horse.set_name("Sugar")
    horse.set_Breed("arabian")
    assert horse.racing(contender)=="Sugar and king battled hard. It's a tie."
    assert horse.get_point()==40
    assert contender.get_point()==60


def test_win(horse,contender):
    horse.set_name("Lucky")
    horse.set_Breed("american")
    assert horse.racing(contender)=="Lucky won. Congratulations!"
    assert horse.get_point()==60
    assert contender.get_point()==0

def test_lose(horse,contender):
    horse.set_name("Rose")
    horse.set_Breed("thoroughbred")
    assert horse.racing(contender)=="Rose fainted!"
    assert horse.get_point()==0
    assert contender.get_point()==80

def test_round_numbers(horse,contender):
    horse.set_name("Rose")
    horse.set_Breed("thoroughbred")
    horse.racing(contender)
    assert HorsesRacing.get_round_numbers()==4

# #################### Fixtures #################### # 

@pytest.fixture
def horse():
    horse = HorsesRacing()
    return horse

@pytest.fixture
def contender():
    king = HorsesRacing()
    king.set_name("king")
    king.set_Breed("arabian")
    king.set_point(70)
    return king