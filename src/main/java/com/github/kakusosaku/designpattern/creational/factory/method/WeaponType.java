package com.github.kakusosaku.designpattern.creational.factory.method;

/**
 * Description
 *
 * @author kaku
 * Date    6/11/21
 */
public enum WeaponType {

    SHORT_SWORD("short sword"),
    SPEAR("spear"),
    AXE("axe"),
    UNDEFINED("");

    private String title;

    WeaponType(String title) {
        this.title = title;
    }

    @Override
    public String toString() {
        return title;
    }

}
