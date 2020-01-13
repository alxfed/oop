# -*- coding: utf-8 -*-
"""https://stackoverflow.com/questions/10547343/add-object-into-pythons-set-collection-and-determine-by-objects-attribute
"""
'''
When a new object is being added to a python set, the hash code of the object is first computed and then, 
if one or more objects with the same hash code is/are already in the set, these objects are tested for 
equality with the new object.

The upshot of this is that you need to implement the __hash__(...) and __eq__(...) methods on your class. 
For example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __hash__(self):
        return hash(self.age)

    def __repr__(self):
        return '<Person {}>'.format(self.name)

tom = Person('tom', 18)
mary = Person('mary', 22)
mary2 = Person('mary2', 22)

person_set = {tom, mary, mary2}
print(person_set)
# output: {<Person tom>, <Person mary>}
However, you should think very carefully about what the correct implementation of __hash__ and __eq__ should be 
for your class. The above example works, but is non-sensical (e.g. in that both __hash__ and __eq__ are defined 
only in terms of age).
'''


def main():
    a = set()
    b = a
    return


if __name__ == '__main__':
    main()
    print('main - done')