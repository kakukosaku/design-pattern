#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# date: 18/08/02
#
# GitHub:
#
#   https://github.com/kakuchange
#
# Description:
#
#   Selectable operations over the same data
import types
import doctest


class StrategyExample:

    def __init__(self, strategy_name="Strategy Example 0", func=None):
        self.name = strategy_name
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name + ' from execute 0')


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')

def test():
    """Test Function :)
    >>> strat0 = StrategyExample()
    >>> strat1 = StrategyExample(strategy_name='Strategy Example 1', func=execute_replacement1)
    >>> strat2 = StrategyExample(strategy_name='Strategy Example 2', func=execute_replacement2)
    >>> strat0.execute()
    Strategy Example 0 from execute 0
    >>> strat1.execute()
    Strategy Example 1 from execute 1
    >>> strat2.execute()
    Strategy Example 2 from execute 2
    """

if __name__ == '__main__':
    print('python3 strategy.py -v get more information :)')
    doctest.testmod()
