package com.github.kakusosaku.designpattern.creational.factory.abstracted;

/**
 * Description
 *
 * @author kaku
 * Date    6/15/21
 */
public class Summary {

    public static void main(String[] args) {
        KingdomFactory factory = FactoryMaker.makeFactory(FactoryMaker.KingdomType.ELF);
        System.out.println(factory.createKing().getDescription());
        System.out.println(factory.createCastle().getDescription());
    }

}
