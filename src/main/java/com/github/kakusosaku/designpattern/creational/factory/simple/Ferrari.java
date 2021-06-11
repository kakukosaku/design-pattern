package com.github.kakusosaku.designpattern.creational.factory.simple;

/**
 * Description
 *
 * @author kaku
 * Date    6/10/21
 */
public class Ferrari implements Car {

    static final String DESCRIPTION = "This is Ferrari.";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }

}
