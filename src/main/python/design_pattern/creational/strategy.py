#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# date: 2020/05/16
#
# GitHub:
#
#   https://github.com/kakukosaku
#
# Description:
#
#   Selectable operations over the same data
#   该示例, 实现了基于策略模式的简单工厂模式(基于策略, 选择实际需要使用的类实例化对象)
#
from urllib import parse


class StrategyContainerMeta(type):

    DEFAULT_CLS_KEY = "default"

    def __new__(mcs, cls_name, bases, attrs):
        _strategy_mapping = dict(
            field=set(),
        )
        for _, attr_cls in attrs.items():
            if hasattr(attr_cls, "_strategy"):
                is_default = attr_cls._strategy.pop(mcs.DEFAULT_CLS_KEY, False)
                _strategy_mapping["field"].update(
                    set(attr_cls._strategy.keys()))
                if is_default:
                    if mcs.DEFAULT_CLS_KEY in _strategy_mapping:
                        raise ValueError(
                            "{}: init failed, you can only spefic only one default impl cls.".format(cls_name))
                    _strategy_mapping[mcs.DEFAULT_CLS_KEY] = attr_cls

                kv_pairs = list(attr_cls._strategy.items())
                kv_pairs.sort(key=lambda x: x[0])
                urlencoded_kv = parse.urlencode(kv_pairs)
                _strategy_mapping[urlencoded_kv] = attr_cls

        if not _strategy_mapping.get(mcs.DEFAULT_CLS_KEY):
            raise ValueError("{}: init failed, you must spefic one and only one default impl cls".format(cls_name))

        cls = super(StrategyContainerMeta, mcs).__new__(
            mcs, cls_name, bases, attrs)
        setattr(cls, "_strategy_mapping", _strategy_mapping)

        return cls


class StrategyContainerBase(object, metaclass=StrategyContainerMeta):

    class Demo(object):
        _strategy = {
            "default": True,
        }

    def __new__(cls, input_data, *args, **kwargs):
        strategy_data = dict()
        for field in cls._strategy_mapping["field"]:
            if field in input_data:
                strategy_data[field] = input_data[field]

        kv_pairs = list(strategy_data.items())
        kv_pairs.sort(key=lambda x: x[0])
        urlencoded_kv = parse.urlencode(kv_pairs)
        actual_cls = cls._strategy_mapping.get(
            urlencoded_kv) or cls._strategy_mapping["default"]
        return actual_cls(input_data, *args, **kwargs)


class StrategyInterface(object):

    def get_strategy_config(self):
        """获取策略配置"""
        raise NotImplementedError

    def get_strategy_config_hashable(self):
        """获取用策略匹配的 (k,v) 对

        Notes:
            1. 应该保证该 (k,v) 返回为固定方式排序过的
            2. return type should be hashable!

        Returns:
            tuple([("k1", "v1"), ("k2", "v2")])

        """
        raise NotImplementedError

    def __eq__(self, other):
        """magic method used by `==`

        Args:
            other: any object

        Returns:
            bool

        """
        if not hasattr(other, "get_strategy_config_hashable"):
            return False

        return hash(self.get_strategy_config_hashable()) == hash(other.get_strategy_config_hashable())

    def __ne__(self, other):
        """magic method used by `!=`

        References:
            1. https://stackoverflow.com/questions/4352244/python-should-i-implement-ne-operator-based-on-eq/30676267#30676267

        Args:
            other: any object

        Returns:
            bool

        """
        return not self == other

    def __hash__(self):
        return hash(self.get_strategy_config_hashable())


class StrategyConfig(StrategyInterface):

    def __init__(self, **kwargs):
        self.kv_pairs = tuple(sorted(kwargs.items(), key=lambda x: x[0]))
        self.strategy_config = dict(kwargs)

    def get_strategy_config_hashable(self):
        return self.kv_pairs

    def get_strategy_config(self):
        return self.strategy_config

    def __str__(self):
        return "StrategyConfig<%s>" % str(self.get_strategy_config())

    __repr__ = __str__


class StrategyFactoryMeta(type):

    def __new__(mcs, cls_name, bases, attrs):
        attrs.setdefault("actual_impl_cls_map", dict())
        attrs.setdefault("actual_impl_cls_default", None)
        attrs.setdefault("strategy_fields", list())
        return super(StrategyFactoryMeta, mcs).__new__(mcs, cls_name, bases, attrs)


class StrategyFactory(object, metaclass=StrategyFactoryMeta):

    actual_impl_cls_map = dict()
    actual_impl_cls_default = None
    strategy_fields = list()

    @classmethod
    def register(cls, strategy_obj, impl_cls, default=False):
        """为策略工厂 `注册` 实现类

        Args:
            strategy_obj:
            impl_cls:
            default:

        """
        if strategy_obj in cls.actual_impl_cls_map:
            raise ValueError("重复注册 `策略` 实现类: {}".format(impl_cls.__name__))

        if default and cls.actual_impl_cls_default:
            raise ValueError(
                "重复注册 default `策略` 实现类: {}".format(impl_cls.__name__))

        if default:
            cls.actual_impl_cls_default = impl_cls

        cls.actual_impl_cls_map[strategy_obj] = impl_cls
        for field in strategy_obj.get_strategy_config():
            if field not in cls.strategy_fields:
                cls.strategy_fields.append(field)

    @classmethod
    def get_register_config(cls):
        return cls.actual_impl_cls_map

    @classmethod
    def get_impl_cls(cls, strategy_config):
        """根据 `策略` 获取实现类, 工厂方法模式"""
        _strategy_config = dict()
        for field in cls.strategy_fields:
            if strategy_config.get(field):
                _strategy_config[field] = strategy_config.get(field)

        strategy_obj = StrategyConfig(**_strategy_config)
        return cls.actual_impl_cls_map.get(strategy_obj) or cls.actual_impl_cls_default

    def __new__(cls, data):
        return cls.get_impl_cls(data)(data)


def strategy_factory_register(strategy_factory_cls, default=False, **strategy_config):
    def decorator(cls):
        if not issubclass(strategy_factory_cls, StrategyFactory):
            raise ValueError("该装饰器必须用于`StrategyFactory`的子类")
        strategy_factory_cls.register(StrategyConfig(
            **strategy_config), cls, default=default)

        return cls

    return decorator


@strategy_factory_register(StrategyFactory, default=True)
class StrategyFactoryDefault(object):
    pass
