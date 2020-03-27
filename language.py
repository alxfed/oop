# -*- coding: utf-8 -*-
"""...
"""
class rule(object):
    """rule object. All decorators inherit to this object.
    """
    def __init__(self, operator, multi, *args):
        self.operator = operator
        self.multi = multi
        self.alias = None

        if len(_ruleset_stack) and isinstance(_ruleset_stack[-1], ruleset):
            _ruleset_stack[-1].rules.append(self)

        if not len(args):
            raise Exception('Invalid number of arguments')

        self.count = None
        self.pri = None
        self.cap = None
        self.dist = None
        self.func = []
        new_args = []
        for arg in args:
            if isinstance(arg, dict):
                if 'count' in arg:
                    self.count = arg['count']
                elif 'pri' in arg:
                    self.pri = arg['pri']
                elif 'cap' in arg:
                    self.cap = arg['cap']
                elif 'dist' in arg:
                    self.dist = arg['dist']
                else:
                    self.func = arg
            elif isinstance(arg, value) or isinstance(arg, rule):
                new_args.append(arg)
            else:
                self.func = arg

        if not multi:
            self.expression = new_args[0]
        else:
            self.expression = new_args

    def __enter__(self):
        _rule_stack.append(self)

    def __exit__(self, exc_type, exc_value, traceback):
        _rule_stack.pop()

    def __call__(self, *args):
        if (len(args) == 1 and hasattr(args[0], '__call__')):
            self.func = [args[0]]

        return self

    def define(self, parent_name=None):
        defined_expression = None
        if not self.multi:
            defined_expression = self.expression.define()
        else:
            index = 0
            defined_expression = []
            for current_expression in self.expression:
                new_expression = None
                name = None
                if current_expression.alias:
                    name = current_expression.alias
                elif len(self.expression) == 1:
                    if parent_name:
                        name = '{0}.m'.format(parent_name)
                    else:
                        name = 'm'
                else:
                    if parent_name:
                        name = '{0}.m_{1}'.format(parent_name, index)
                    else:
                        name = 'm_{0}'.format(index)

                if isinstance(current_expression, all):
                    new_expression = {'{0}$all'.format(name): current_expression.define(name)['all']}
                elif isinstance(current_expression, any):
                    new_expression = {'{0}$any'.format(name): current_expression.define(name)['any']}
                elif isinstance(current_expression, none):
                    new_expression = {'{0}$not'.format(name): current_expression.define()['none'][0]['m']}
                else:
                    new_expression = {name: current_expression.define()}

                defined_expression.append(new_expression)
                index += 1

        if len(self.func):
            if len(self.func) == 1 and not hasattr(self.func[0], 'define'):
                defined_expression = {self.operator: defined_expression, 'run': self.func[0]}
        elif self.operator:
            defined_expression = {self.operator: defined_expression}

        if self.count:
            defined_expression['count'] = self.count

        if self.pri:
            defined_expression['pri'] = self.pri

        if self.cap:
            defined_expression['cap'] = self.cap

        if self.dist == True:
            defined_expression['dist'] = 1

        if self.dist == False:
            defined_expression['dist'] = 0

        return defined_expression


class when_all(rule):
    def __init__(self, *args):
        super(when_all, self).__init__('all', True, *args)

def main():
    return


if __name__ == '__main__':
    main()
    print('\ndone')