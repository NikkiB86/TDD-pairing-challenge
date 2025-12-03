from lib.includes_todo import *

def test_includes_todo_true():

    result = includes_todo("#TODO buy milk")

    assert result == True


def test_includes_todo_false():

    result = includes_todo("drink tea")

    assert result == False   

def test_includes_todo_another_true():

    result = includes_todo("learn to test-drive my code #TODO")
    assert result == True
