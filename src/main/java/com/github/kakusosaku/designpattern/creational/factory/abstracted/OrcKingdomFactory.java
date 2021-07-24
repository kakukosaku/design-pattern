package com.github.kakusosaku.designpattern.creational.factory.abstracted;

/**
 * Description
 *
 * @author kaku
 * Date    7/24/21
 */
public class OrcKingdomFactory implements KingdomFactory {

    @Override
    public King createKing() {
        return new OrcKing();
    }

    @Override
    public Castle createCastle() {
        return new OrcCastle();
    }

}
