# -*- coding: utf-8 -*-
"""https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
"""
import logging

class DecoratorObject(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        self.f = f  # Prove that function definition has completed
        self.f()

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


def main():
    @DecoratorObject
    def aFunction():
        print("inside aFunction()")
    print("Finished decorating aFunction()")

    aFunction()
    return


if __name__ == '__main__':
    main()
    print('\ndone')