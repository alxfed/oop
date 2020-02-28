# -*- coding: utf-8 -*-
"""...
"""
class Transform(object):
    def __init__(self, parameter):
        self.scale = parameter

    def __call__(self, variable):
        return variable * self.scale


def main():
    tran = Transform(2)
    result = tran(2)
    print(result)
    return


if __name__ == '__main__':
    main()
    print('\ndone')