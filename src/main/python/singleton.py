#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# data: 18/07/19
#
# GitHub:
#
#   https://github.com/kakuchange
#
# Description:
#
#   Singleton implements, summarize from :)
#
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


# ---- ---- ---- ---- ----
# Method 1: A decorator
# Pros:
#   - 直观, 灵活度高
# Cons:
#   - return a function not a Class!
# ---- ---- ---- ---- ----
def singleton(class_):
    instance = {}
    def getinstance(*args, **kwargs):
        """Method 1 success!"""
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]
    return getinstance


@singleton
class Method1Cls:
    # Note!!!  decorator return a function->getinstance
    # __doc__ = ["Method 1 faild!", "method 1 success!"]
    pass


# ---- ---- ---- ---- ----
# Method 2: A base class
# Pros:
#   - reuse this base class
#   - true class
# Cons:
#   - multiple inheritance can override __new__ method
# ---- ---- ---- ---- ----
class SingletonBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            # cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Method2Cls(SingletonBase):
    __doc__ = ["Method 2 faild!", "Method 2 success!"]
    pass


# ---- ---- ---- ---- ----
# Method 3: A base class
# Pros:
#   - reuse this base class
#   - true class
#   - cover inheritance
# Cons:
#   - may by more complicated
# ---- ---- ---- ---- ----
class SingletonMeta(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Method3Cls(metaclass=SingletonMeta):
    __doc__ = ["Method 3 faild!", "Method 3 success!"]
    pass

def test(fakecls):
    try:
        assert fakecls() is fakecls()
    except AssertionError:
        if fakecls == Method1Cls:
            print('Method 1 failed')
        else:
            print(fakecls.__doc__[0])
    else:
        if fakecls == Method1Cls:
            print(fakecls.__doc__)
        else:
            print(fakecls.__doc__[1])


if __name__ == "__main__":
    test(Method1Cls)
    test(Method2Cls)
    test(Method3Cls)
