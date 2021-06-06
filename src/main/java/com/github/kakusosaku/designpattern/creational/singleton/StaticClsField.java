package com.github.kakusosaku.designpattern.creational.singleton;

/**
 * Description
 *
 * @author kaku
 * Date    6/5/21
 */
public final class StaticClsField {

    /**
     * Private constructor so nobody can instantiate the class
     */
    private StaticClsField() {
    }

    /**
     * Static to class instance of class.
     */
    private static final StaticClsField INSTANCE = new StaticClsField();

    public static StaticClsField getInstance() {
        return INSTANCE;
    }

}
