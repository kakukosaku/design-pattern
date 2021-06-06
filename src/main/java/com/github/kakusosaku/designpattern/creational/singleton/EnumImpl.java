package com.github.kakusosaku.designpattern.creational.singleton;

/**
 * Description
 *
 * @author kaku
 * Date    6/5/21
 */
public enum EnumImpl {

    INSTANCE;

    @Override
    public String toString() {
        return getDeclaringClass().getCanonicalName() + "@" + hashCode();
    }

    public static EnumImpl getInstance() {
        return INSTANCE;
    }
}
