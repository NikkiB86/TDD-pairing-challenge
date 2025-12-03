from lib.includes_todo import *

def test_includes_todo_true():

    result = includes_todo("#TODO buy milk")

    assert result == True


def test_includes_todo_false():

    result = includes_todo("#TODO buy milk")

    assert result == False   