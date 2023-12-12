#!/usr/bin/env python
""" generated source for module Function """
class Function(object):
    """ generated source for class Function """

    def __init__(self, arg, expr):
        """ generated source for method __init__ """
        self.arg = arg
        self.expr = expr

    def call(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return self.expr.eval(copy)

