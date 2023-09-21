#test for todo classes
from lib.todo import*
from lib.todo_list import*

# def test_class_todo_list():
#     test_todo_list = TodoList()
#     assert 1 == 2

def test_class_todo():
    test_task = Todo("cut the grass")
    
    assert test_task.complete == False
    assert test_task.task_name == "cut the grass"

def test_todo_mark_complete():
    test_task = Todo("wash ya face")
    test_task.mark_complete()
    assert test_task.complete == True


def test_class_todo_list_add():
    mow = Todo("cut the grass")
    test_task_todo_list = TodoList()
    test_task_todo_list.add(mow)
    assert mow.complete == False
    assert test_task_todo_list.incomplete() == [mow]

def test_todo_list_complete():
    mow = Todo("cut the grass")
    test_task_todo_list = TodoList()
    test_task_todo_list.add(mow)
    mow.mark_complete()
    assert test_task_todo_list.complete() == [mow]

def test_todo_list_incomplete():
    mow = Todo("cut the grass")
    test_task_todo_list = TodoList()
    test_task_todo_list.add(mow)
    assert test_task_todo_list.incomplete() == [mow]

def test_give_up():
    mow = Todo("cut the grass")
    test_task_todo_list = TodoList()
    test_task_todo_list.add(mow)
    shave = Todo("shave your face")
    test_task_todo_list.add(shave)
    test_task_todo_list.give_up()
    assert test_task_todo_list.complete() == [mow,shave]
    assert test_task_todo_list.incomplete() == []
