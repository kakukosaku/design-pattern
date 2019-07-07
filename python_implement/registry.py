#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# date: 18/08/02 Fri
#
# GitHub:
#
#   https://github.com/kakuchange
#
# Description:
#
#   Keep track of all subclasses of a given class.
import doctest


class RegistryHolder(type):
    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            Here the name of the class is used as key but it could be any class
            parameter.
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    def get_registry(self):
        return dict(self.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    """
        Any class that will inherits from BaseRegisteredClass will be included
        inside the dict RegistryHolder.REGISTRY, the key being the name of the
        class and the associated value, the class itself.
    """
    pass


def test():
    """Test Function
    # before
    >>> print(BaseRegisteredClass.get_registry())
    {'BaseRegisteredClass': <class '__main__.BaseRegisteredClass'>}
    >>> class ClassRegistree(BaseRegisteredClass):
    ...     def __init__(self, *args, **kwargs):
    ...         pass
    ...

    # After inheritance
    >>> print(ClassRegistree.get_registry())
    {'BaseRegisteredClass': <class '__main__.BaseRegisteredClass'>, 'ClassRegistree': <class '__main__.ClassRegistree'>}
    """
    # for k in RegistryHolder.REGISTRY:
    # for k in ClassRegistree.__class__.REGISTRY:
    #     print(k)


if __name__ == "__main__":
    print('python3 strategy.py -v get more information :)')
    doctest.testmod()
