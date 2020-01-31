package com.github.kakusosaku.singleton;

import java.io.Serializable;

/**
 * 利用双重检验锁(Double-Checked Locking idiom)机制的线程安全"懒加载"的 单例模式
 *
 * @author kaku
 * Date    2020-01-30
 */
class ThreadCareSingleton implements Serializable {

    private static volatile ThreadCareSingleton INSTANCE;

    public static ThreadCareSingleton getInstance() {
        if (INSTANCE == null) {
            synchronized (ThreadCareSingleton.class) {
                if (INSTANCE == null) {
                    INSTANCE = new ThreadCareSingleton();
                }
            }
        }
        return INSTANCE;
    }

    /**
     * 反序列化时, 解析返回object时调用, 返回已初始化好的"单例对象"
     *
     * @return singleton instance of ThreadCareSingleton
     */
    @SuppressWarnings("unused")
    private Object readResolve() {
        return INSTANCE;
    }

    /**
     * 提供统一的"类加载", 避免因不同容器类加载导致类存在不同空间, 影响单例模式
     *
     * @param classname returns the runtime class of this object.
     * @return the class of ThreadCareSingleton.
     * @throws ClassNotFoundException 类未找到异常
     */
    @SuppressWarnings("unused")
    private static Class getClass(String classname) throws ClassNotFoundException {
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        if (classLoader == null)
            classLoader = ThreadCareSingleton.class.getClassLoader();
        return (classLoader.loadClass(classname));
    }

}
