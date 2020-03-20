# -*- coding: utf-8 -*-
"""...
"""
def print_args(function):
     def wrapper(*args, **kwargs):
         print('Arguments:', args, kwargs) # this is the additional functionality the whole story has been started for
         if args[1] == 'bar':
             return function(*args, **kwargs)
         else:
             return None
     return wrapper


@print_args
def write(text, mext, kwarg:str):
    print(text, mext)
    print(kwarg)


def main():
    write('foo', 'bar', kwarg='one kwarg')
    return


if __name__ == '__main__':
    main()
    print('\nmain - done')