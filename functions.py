def get_todos(filepath="todos.txt"):

    """reads a text file and returns
    the list of to-do items"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


#like a modifying function and we do not need to return anything
def write_todos(todos_arg,filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

