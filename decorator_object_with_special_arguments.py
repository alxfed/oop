# -*- coding: utf-8 -*-
"""https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
"""
_rule_stack = []
_ruleset_stack = []
_rulesets = {}
_main_host = None


class ruleset(object):

    def __init__(self, name):
        self.name = name
        self.rules = []
        if not len(_ruleset_stack):
            _rulesets[name] = self
        elif len(_rule_stack) > 0:
            _rule_stack[-1].func.append(self)
        else:
            raise Exception('Invalid rule context')

    def __enter__(self):
        _ruleset_stack.append(self)

    def __exit__(self, exc_type, exc_value, traceback):
        _ruleset_stack.pop()

    def define(self):
        index = 0
        new_definition = {}
        for rule in self.rules:
            new_definition['r_{0}'.format(index)] = rule.define()
            index += 1

        return self.name, new_definition


class rule(object):

    def __init__(self, operator, multi, *args):
        self.operator = operator
        self.multi = multi
        self.alias = None

    def __enter__(self):
        _rule_stack.append(self)

    def __exit__(self, exc_type, exc_value, traceback):
        _rule_stack.pop()

    def __call__(self, *args):
        if (len(args) == 1 and hasattr(args[0], '__call__')):
            self.func = [args[0]]

class when_all(rule):

    def __init__(self, *args):
        super(when_all, self).__init__('all', True, *args)


def main():
    with ruleset('animal'):
        @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
                  (m.predicate == 'lives') & (m.object == 'water') & (m.subject == c.first.subject))
        def frog(c):
            c.assert_fact({'subject': c.first.subject, 'predicate': 'is', 'object': 'frog'})

    return


if __name__ == '__main__':
    main()
    print('\ndone')