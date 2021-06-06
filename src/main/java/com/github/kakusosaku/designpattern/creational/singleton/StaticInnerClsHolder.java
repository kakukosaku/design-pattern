package com.github.kakusosaku.designpattern.creational.singleton;

/**
 * 利用类加载机制的"懒加载"的 单例模式
 *
 * @author kaku
 * Date    2020-01-30
 */
class StaticInnerClsHolder {

    /**
     * Private constructor
     */
    private StaticInnerClsHolder() {
    }

    /**
     * 该内部类, 在外部类 StaticInnerClsSingleton 被因使用"其它"属性而加载时, 不会导致单例被初始化.
     * <p>该方法是"线程安全"的, 原因在于: 实例是在内部类被加载时创建, 依赖于类加载机制的线程安全!</p>
     */
    private static class InstanceHolder {
        private static final StaticInnerClsHolder INSTANCE = new StaticInnerClsHolder();
    }

    /**
     * @return singleton instance of StaticInnerClsSingleton
     */
    public static StaticInnerClsHolder getInstance() {
        return InstanceHolder.INSTANCE;
    }

}
