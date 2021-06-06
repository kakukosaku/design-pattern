package com.github.kakusosaku.designpattern.creational.singleton;

/**
 * Description
 *
 * @author kaku
 * Date    6/5/21
 * <p>
 * 单例的实现, 大体分2种
 * 1. eagerly initialized (饿汉模式)
 * <p>
 * a. 常使用类的静态属性, 依赖于类加载机制保证线程安全 {@link StaticClsField}
 * <p>
 * b. 使用枚举类实现 {@link EnumImpl}
 * <p>
 * 2. lazily initialized (懒汉模式)
 * <p>
 * a. 线程安全的加载(synchronized on method)
 * <p>
 * b. 线程安全的加载(synchronized on instance)
 * <p>
 * c. 使用内部静态, 依赖于类加载机制保证线程安全
 */
public class Summary {

    public static void main(String[] args) {
        // eagerly initialized
        // static class field
        var inst1 = StaticClsField.getInstance();
        var inst2 = StaticClsField.getInstance();
        System.out.println(inst1);
        System.out.println(inst2);

        // eagerly initialized
        // enum implementation
        var inst3 = EnumImpl.getInstance();
        var inst4 = EnumImpl.getInstance();
        System.out.println(inst3);
        System.out.println(inst4);

        // lazy initialized
        // thread synchronize on method
        var inst5 = ThreadSafeOnMethod.getInstance();
        var inst6 = ThreadSafeOnMethod.getInstance();
        System.out.println(inst5);
        System.out.println(inst6);

        // lazy initialized
        // thread synchronize on instance
        var inst7 = ThreadSafeOnInstance.getInstance();
        var inst8 = ThreadSafeOnInstance.getInstance();
        System.out.println(inst7);
        System.out.println(inst8);

        // lazy static inner class holder
        var inst9 = StaticInnerClsHolder.getInstance();
        var inst10 = StaticInnerClsHolder.getInstance();
        System.out.println(inst9);
        System.out.println(inst10);
    }

}
