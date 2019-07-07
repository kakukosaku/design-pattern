# Design Patterns

# Most of this repo python_implementation come from [python-patterns](https://github.com/faif/python-patterns).

    difference: Change from py2 -> py3 or add some flavor(doctest etc.) :)

A collection of design patterns and idioms in Python/Go.

- Python

    |pattern keyword|type|description|Note|
    |:-------------:|:---|:----------|:---|
    |singleton|creational pattern|a singleton with shared-state among instances|多实例共享状态, 仅就共享状态而言可以有N种方法达到|
    |registory|behavioral pattern|keep track of all subclasses of given class|利用元类或之类的手段, 在实例化时在某处(元类空间)中注册信息|
    |strategy|behavioral pattern|selectable operations over the same data|本质还是方法复写|
    |abstract_factory|creational pattern|use a generic function with specific factories|本质是以函数封装不同类的实例化!|
    |factory_method|creational patthern|delegate a specialized function/method to create instances|注意与抽象工厂作对比, 见下[note 1](#Notes)|
    |brog|creational pattern|a singleton with shared-state among instances|多实例共享状态(变量)|
----------

- Go

    |pattern keyword|type|description|Note|
    |:-------------:|:---|:----------|:---|

## Notes

1. 工厂类强调, 创建实例时不用知晓实际实例的类是哪个, 只需要拿着工厂类即可; 而工厂方法强调的是便捷(简单)的实例化入口.