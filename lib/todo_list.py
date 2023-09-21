#todo file
from lib.todo import*


class TodoList:
    def __init__(self):
        self.list_of_tasks = []
        

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.list_of_tasks.append(todo)
        



    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for i in self.list_of_tasks:
            if i.complete == False:
                incomplete_list.append(i)

        return incomplete_list
        

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = []
        for i in self.list_of_tasks:
            if i.complete == True:
                complete_list.append(i)

        return complete_list
        

    def give_up(self):

        for tasks in self.list_of_tasks:
            tasks.mark_complete()

        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete


