#!/usr/bin/env python
""" generated source for module Environment """
from pl_evalexception import EvalException

class Environment(object):
    """ generated source for class Environment """

    def __init__(self):
        """ generated source for method __init__ """
        self.map = {}
        self.funcMap = {}

    def put(self, var, val):
        """ generated source for method put """
        self.map[var] = val
        return val

    def putFunc(self, var, f):
        """ generated source for method put_0 """
        self.funcMap[var] = f
        return f

    def get(self, pos, var):
        """ generated source for method get """
        if var in self.map:
            return self.map[var]
        raise EvalException(pos, "undefined variable: " + var)

    def getFunc(self, pos, var):
        """ generated source for method getFunc """
        if var in self.funcMap:
            return self.funcMap[var]
        raise EvalException(pos, "undefined function: " + var)

    def copy(self):
        """ generated source for method copy """
        newEnv = Environment()
        for var in self.map:
            newEnv.put(var, self.map[var])
        for var in self.funcMap:
            newEnv.putFunc(var, self.funcMap[var])
        return newEnv

