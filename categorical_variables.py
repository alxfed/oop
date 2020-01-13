# -*- coding: utf-8 -*-
"""https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Categorical.html
"""
import pandas


def main():
    c = pandas.Categorical(
        ['a', 'b', 'c', 'a', 'b', 'c'],
        ordered=True,
        categories = ['c', 'b', 'a'])
    print(c)
    return


if __name__ == '__main__':
    main()
    print('main - done')