package com.github.kakusosaku.designpattern.creational.factory.abstracted;

/**
 * Description
 *
 * @author kaku
 * Date    7/24/21
 */
public class ElfKing implements King {

    static final String DESCRIPTION = "This is the Elven king!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }

}
