FILEPATH = "todos.txt"
# hi

def get_todos(filepath=FILEPATH):
    """ Reads a text file and return the list
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do times list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print('Hello from functions')
    print(get_todos())