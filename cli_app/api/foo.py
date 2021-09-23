import os


def foo_file(my_file):
    print(f'filepath={os.path.abspath(my_file)}')
