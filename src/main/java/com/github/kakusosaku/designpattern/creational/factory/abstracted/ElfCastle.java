package com.github.kakusosaku.designpattern.creational.factory.abstracted;

/**
 * Description
 *
 * @author kaku
 * Date    7/24/21
 */
public class ElfCastle implements Castle {

    static final String DESCRIPTION = "This is the Elven castle!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }

}
