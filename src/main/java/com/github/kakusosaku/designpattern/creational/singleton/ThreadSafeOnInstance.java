package com.github.kakusosaku.designpattern.creational.singleton;

import java.io.Serializable;

/**
 * 利用双重检验锁(Double-Checked Locking idiom)机制的线程安全"懒加载"的 单例模式
 *
 * @author kaku
 * Date    2020-01-30
 */
class ThreadSafeOnInstance implements Serializable {

    private static volatile ThreadSafeOnInstance instance;

    private static boolean unInitialized = true;

    private ThreadSafeOnInstance() {
        if (unInitialized) {
            unInitialized = false;
        } else {
            throw new IllegalStateException("Already initialized.");
        }
    }

    public static ThreadSafeOnInstance getInstance() {
        // local variable increases performance by 25 percent
        var result = instance;
        if (result == null) {
            synchronized (ThreadSafeOnInstance.class) {
                result = instance;
                if (result == null) {
                    instance = result = new ThreadSafeOnInstance();
                }
            }
        }
        return result;
    }

    /**
     * 反序列化时, 解析返回object时调用, 返回已初始化好的"单例对象"
     *
     * @return singleton instance of ThreadCareSingleton
     */
    @SuppressWarnings("unused")
    private Object readResolve() {
        return instance;
    }

    /**
     * 提供统一的"类加载", 避免因不同容器类加载导致类存在不同空间, 影响单例模式
     *
     * @param className returns the runtime class of this object.
     * @return the class of ThreadCareSingleton.
     * @throws ClassNotFoundException 类未找到异常
     */
    @SuppressWarnings("unused")
    private static Class getClass(String className) throws ClassNotFoundException {
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        if (classLoader == null)
            classLoader = ThreadSafeOnInstance.class.getClassLoader();
        return (classLoader.loadClass(className));
    }

}
