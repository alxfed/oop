# -*- coding: utf-8 -*-
"""...
"""
def print_args(function):
     def wrapper(*args, **kwargs):
         print('Arguments:', args, kwargs) # this is the additional functionality the whole story has been started for
         return function(*args, **kwargs)
     return wrapper

@print_args
def write(text, kwarg:str):
    print(text)


def main():
    write('foo', kwarg='one kwarg')
    return


if __name__ == '__main__':
    main()
    print('main - done')