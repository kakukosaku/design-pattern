# Design Patterns

For create more concise code, you should learn Design Patterns.

# Overview

**Design Principles**

1. [Open Close Principle - 开放封闭原则](#open-close-principleocp)
2. [Dependency Inversion Principle - 依赖倒置原则](#dependency-inversion-principle)
3. [Interface Segregation Principle - 接口隔离原则](#interface-segregation-principle)
4. [Single Responsibiligy Principle - 单一职责原则](#single-responsibility-principle)
5. [Liskov's Substitution Principle - 里氏替换原则](#liskovs-substitution-principle)
6. [迪米特原则](#迪米特原则)
7. [组合/聚合原则](#组合聚合原则)

**Design Patterns**

Creational Design Patterns: 

1. [Singleton](#Singleton-单例模式)
2. [Simple Factory](#Simple-Factory-工厂模式)
3. [Factory Method](#Factory-Method-工厂方法模式)
4. [Abstract Factory](#Abstract-Factory-抽象工厂模式)
5. [Builder](#Builder-建造者模式)
6. [Prototype](#Prototype-原型模式)
7. [Object Pool](#Object-Pool-对象池模式)

Structural Design Patterns:

1. [Adapter](#Adapter-适配器模式)
2. [Bridge](#Bridge-桥接模式)
3. [Composite](#Composite-组成模式)
4. [Decorator](#Decorator-装饰器模式)
5. [Flyweight](#Flyweight)
6. [Proxy](#Proxy-代理模式)

Behavioral Design Patterns:

1. [Chain of Responsibility](#Chain-of-Responsibility-责任链模式)
2. [Command](#Command-命令模式)
3. [Iterator](#Iterator-迭代器模式)
4. [Mediator](#Mediator-中介模式)
5. [Memento](#Memento)
5. [Observer](#Observer-观察者模式)
8. [Visitor](#Visitor-访客模式)
6. [Strategy](#Strategy-策略模式)
7. [Template Method]()
9. [Null Object]()

# References

- https://www.oodesign.com/

- https://github.com/kamranahmedse/design-patterns-for-humans

- https://java-design-patterns.com/

UML Syntax Reference:

- https://www.claudiodesio.com/ooa&d/UMLSR_EN/UMLSR.htm (Class Diagram)

## Design Principles

以下情形应该**避免**

1. Rigidity: 系统铁板一块, 迁一发而动全身, 对一处的改动影响到系统的很多动方
2. Fragility: 系统脆弱, 小的改动会有意料不到的大影响
3. Immobility: 模板耦合严重, 其中的功能模块无法单独复用

为此, 你需要遵守以下原则(Principles)

### Open Close Principle(OCP)

> Software entities like classes, modules and functions should be **open for extension but closed for modifications**.

为了完成产品提出迭代需求, 带的应该是对现有代码的拓展而非修改! 这意味着对已交付的代码应有合理的拓展性. 这样做带了很多好处, 如: 向后兼容; 避免因修改之前代码需要回归测试等(backward compatibility & regression testing...)

常见的实现方式有: 通过抽象类(定义功能)&实现类(实现具体的功能)的方式, 这样保证了(新的)实现类是对抽象类的拓展而非修改

具体的设计模式: 模板模式(Template Pattern), 策略模式(Strategy Pattern)

### Dependency Inversion Principle

> High-level modules should not depend on low-level modules. Both should depend on abstractions.

> Abstractions should not depend on details. Details should depend on abstractions.

听起来很抽象: 高层模块不应该依赖于低层模块, 二者皆应依赖于抽象; 抽象不应依赖于细节, 细节应该依赖于抽象. 我们首先定义 "依赖(depend on)": 依赖是指高层模块的功能的完成, 必须建立在低层模块提供的功能之上. 

有个比较容易理解的例子(讲人话🙃):

**场景**: 很多妈妈都会在睡前给小孩子读儿童读物, 讲故事, 我们简化一下: 妈妈读儿童读物. 

**分析**: 以面向对象的思维编写这部分的功能代码, 抽象出2个对象: `妈妈_对象` & `儿童读物_对象`. 整个功能的完成在于`妈妈_对象`读`儿童读物_对象`, 易知`妈妈_对象`为高层模块, `妈妈_对象`对外提供"妈妈读儿童读物"的功能. 而此功能的实现"依赖(depend on)" 另一个对象`儿童读物_对象`. 但这样有2个明显的坏处:

1. `妈妈_对象`无法单独使用, 必须依赖于`儿童读物_对象`
2. 同时违背了OCP原则, 增加"妈妈读报纸"功能时, 需要修改之前"妈妈读儿童读物"功能的代码.

**解决办法**: 增加"抽象(abstraction)", "妈妈读儿童读物/妈妈读报纸" -> "妈妈读可读之物", 注意这里的可读之物, 即是对儿童读物, 报纸等的抽象! 具体的解释: 在高层与低层之间加入一层抽象层, 使得高层与低层之前的依赖转为依赖抽象; 而抽象不应该依赖于细节, 细节应该依赖于抽象, 则是指先定义什么是"可读之物", 再定义什么是儿童读物/报纸(儿童读物/报纸依赖于"可读之物"这一抽象!)

也被称为Inversion of Control(IOC), 实际为同一思想. 具体的解释: 在开发框架时, 当一个模块需要另一个模块时, 实例化之, 并直接持有其引用会将2个模块强耦合在一起, 为了实现解耦, 一个模块提供钩子(hook, a property or parameter)然后由额外的模块管理依赖, 将该模块的引用注入到另一个模块.

> By applying the Dependency Inversion the modules can be easily changed by other modules just changing the dependency module. Factories and Abstract Factories can be used as dependency frameworks, but there are specialized frameworks for that, known as Inversion of Control Container.

具体的设计模式: 工厂模式(Factory), 抽象工厂模式(Abstract Factory)

### Interface Segregation Principle

> Clients should not be forced to depend upon interfaces that they don't use.

设计接口时, 不应该引入多余方法, 否则将使得实现该接口的类被强制实现该方法.

### Single Responsibility Principle

> A class should have only one reason to change.

如果我们因2个原因去修改一个类, 那么这个类应该重构为2个, 各自有且仅有一个原因而修改它.

### Liskov's Substitution Principle

> Drived types must be completely substitutable for their base types.

这个原则是对OCP原则的拓展, 是指, 当子类拓展父类时, 应该是**同一类行为**的拓展而非改变原有行为! 子类应在不修改代码情况下, 能完全代替父类. 

此外, 还有一些拓展的原则, 如:

### 迪米特原则

一个对象应该对其它对象保持最少的了解

### 组合/聚合原则

组合/聚合优于继承, 继承将父类的细节显露给子类, 将一项功能的实现改为多个类的组合/聚合, 降低了类与类之间的耦合程度, 达到高内聚低耦合.

## Design Patterns

### Singleton 单例模式

> Ensure that only one instance of a class is created and Provide a global access point to the object.

实质: 

全局只需初始化一个实例, 该实例全局可用(需注意多线程环境下, 并发修改问题)

使用场景:

- Logger Class
- Configuration Class
- Access resources in shared mode

示例:

[Java](src/main/java/com/github/kakusosaku/singleton)

[Python](src/main/python/singleton.py)

### Simple Factory 工厂模式

> Simplified version of Factory Method, Creates objects without exposing the instantiation logic to the client and Refers to the newly created object through a common interface.

实质:

A framework delegate the creation of objects derived from a common superclass to the factory - we need flexibility in adding new types of objects that must be created by the class.

在面向对象的语言中, 一般通过父类实例化对象, 而工厂模式(简单工厂模式), 无需知道直接父类是谁, 通过工厂类实例化所需对象.

也即: 通过同一`工厂对象`生产不同的对象, 不暴露任何实例化的逻辑(无需知道实例是由哪个父类实例化而来). 

使用场景:

Along with singleton pattern the factory is one of the most used patterns. Almost any application has some factories. Here are a some examples in java:

a. factories providing an xml parser: javax.xml.parsers.DocumentBuilderFactory or javax.xml.parsers.SAXParserFactory

b. java.net.URLConnection - allows users to decide which protocol to use

示例:

pass

### Factory Method 工厂方法模式

> Defines an interface for creating objects, but let subclasses to decide which class to instantiate and Refers to the newly created object through a common interface.

与Factory模式的区别在于, 通过工厂的父子类继承, override工厂父类的某些方法, 达到实现"新工厂"产生定制的对象.

也即: 通过暴露某些方法, 使得子类能介入工厂实例化的逻辑中(关键在有无继续的子工厂!)

### Abstract Factory 抽象工厂模式

> Offers the interface for creating a family of related objects, without explicitly specifying their classes.

实质:

抽象共同接口`FactoryInterface`表示工厂应具有的创建方法, 然后由`AbstractFactory`作为`FactoryInterface`实现类`SomeFactory`的上层建筑, 达到屏蔽`SomeFactory`实现细节的目的. 使得在使用一系列工厂类时, 屏蔽具体工厂类实现细节, 更易用&解耦.

也即: 与工厂方法类似(有许多类似的工厂), 但是, 是通过定义抽象的工厂类(接口), 使得这许多的工厂, 有同样的使用(实现了同样的工厂抽象)

使用场景:

复杂逻辑的对象实例化.

示例:

pass

### Builder 建造者模式

> Defines an instance for creating an object but letting subclasses decide which class to instantiate and Allows a finer control over the construction process.

将复杂对象实例化过程(例如: constructor 需要很多参数, constructor 有很多处理步骤), 通过建造者模式, 拆解, 更清晰的实例化过程&更集中, 可复用的实例化复杂对象.

也即: 将初始化需要的 "众多参数", 改为先实例化对象, 再调用对象提供的 "建造" 方法完成实例构建.

使用场景:

初始化参数很多(该对象有很多属性需要设置).

示例:

pass

### Prototype 原型模式

> Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

> Create object based on an existing object through cloning.

### Object Pool 对象池模式

> Reuses and shares objects that are expensive to create.

## Structural Design Patterns

### Adapter 适配器模式

实质:

Convert the interface of a class into another interface clients expect. 适配器, 将不兼容的API, 在适配器中统一

使用场景:

充电器的角色, 将各类需要充电的设备(Type-C口, USB口等通过充电器(这一适配器)统一到插板上)

示例:

pass

### Bridge 桥接模式

实质:

将部分功能, 抽象出来由另一个对象提供, 这样, 提供该功能的对象与原对象decouple && 将abstraction & implementation decouple.

Bridge pattern is about preferring composition over inheritance. Implement details are pushed from a hierarchy to another object with a separate hierachy.

使用场景:

网站各模块主题从各模块中抽象出来

示例:

pass

### Composite 组成模式

实质:

将整体与个体(很多各类)的关系抽象, 使得整体对待个体以统一的方式

使用场景:

互联网公司人员(产品, 设计, 研发, 市场, 行政etc) -> 公司 与 雇员(岗位, 薪资, 职责etc)的抽象

示例:

pass

## decorator 装饰器模式

实质:

dynamically change behavior of an object at runtime by wrapping them in a object of a decorator class. Another class!

The intent of this pattern is to add additional responsibilities dynamically to an object.

使用场景:

API权限校验

示例:

pass

### facade 门面模式

实质:

对复杂对象, 提供简单的API (Facade pattern provides a simplified interface to a complex subsystem).

使用场景:

log4j

示例:

pass

### flyweight

### proxy 代理模式

实质:

用一个类代理另一个类的功能 (a class represents the functionality of another class).

使用场景:

Nginx代理后端App提供 HTTP 服务

示例:

pass

## Behavioral Design Pattern

### chain of responsibility 责任链模式

实质:

将连续的if-else if-else if-else 转换为责任链, 以注册successor(继任者), 依次处理Request.

使用场景:

多张银行卡的支付顺序(第一张能全额支持的银行卡处理支付请求)

示例:

pass

### command 命令模式

实质:

对动作进行抽象封装, 使得命令的发出者&实际执行者解耦(Allows you to encapsulate actions in objects. The key idea behind this pattern is to provide the means to decouple client from receiver). 细节(命令发起的"命令")依赖于抽象("对实际命令的抽象"), 抽象不应依赖于细节.

使用场景:

消费者可以发出 "点菜命令", 也可以发出 "需要提供水的命令/打开风扇" 之类的命令, 均由服务生执行

示例:

pass

### Iterator 迭代器模式

实质:

访问对象中的元素, 而无需暴露实现细节(It presents a way to access the elements of an object without exposing the underlying presentation).

使用场景:

```Python
for i in Iterator:
    pass
```

```golang
for Iterator.Next() {
    Iterator.Scan()
}
```

示例:

pass

### Mediator 中介模式

实质:

将2个对象的交互, 交由第三者(定义的抽象, 接口)控制, 以降低2个对象之间的耦合度.

使用场景:

比如, 证券(经纪)公司提供的开户受理, 通过公司Open API团队, 再封装抽象后, 与其它渠道商合作, 由渠道商对外提供开户受理, 引流.

示例:

pass

### Memento

### Observer 观察者模式

实质:

Defines a dependency between objects so that whenever an object changes its state, all its dependents are notified.

使用场景:

类似于Publish/Subscribe 模式吧...重点在于, "注册"进一个类, 以在该类发生变化时有"感知/通知".

示例:

pass

### Visitor 访客模式

实质:

Visitor pattern lets you add further operations to objects without having to modify them.

使用场景:

pass

示例:

pass

### Strategy 策略模式

实质:

Strategy pattern allows you to switch the algorithm or strategy based upon the situation.

使用场景:

比如证券公司有个人业务, 机构业务, 海外个人业务各类繁多的账户类型开户. 不同类型的业务(账户类型)所需要的采集的个人信息不同, 除去前端的必传/逻辑校验外, 后端是保证数据完整/一致性的重要一关! 针对不同的业务/账户, 采取不同的数据校验方法(Validator). 

将不同的 `Validator` 视为不同的Strategy.

示例:

[python]()