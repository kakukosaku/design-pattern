package com.github.kakusosaku.designpattern.creational.singleton;

/**
 * Description
 *
 * @author kaku
 * Date    6/8/21
 */
public class ThreadSafeOnMethod {

    private static ThreadSafeOnMethod instance;

    /**
     * private constructor to prevent client from instantiating.
     */
    private ThreadSafeOnMethod() {
        if (instance == null) {
            instance = this;
        } else {
            throw new IllegalStateException("Already initialized");
        }
    }

    /**
     * Then instance gets created only when it is called for first time. lazy-loading
     *
     * @return {@link ThreadSafeOnMethod}
     */
    public static synchronized ThreadSafeOnMethod getInstance() {
        if (instance == null) {
            instance = new ThreadSafeOnMethod();
        }
        return instance;
    }

}
