package com.github.kakusosaku.designpattern.creational.factory.method;

/**
 * Description
 *
 * @author kaku
 * Date    6/11/21
 */
public class OrcWeapon implements Weapon {

    private WeaponType weaponType;

    public OrcWeapon(WeaponType weaponType) {
        this.weaponType = weaponType;
    }

    @Override
    public WeaponType getWeaponType() {
        return weaponType;
    }

    @Override
    public String toString() {
        return "Orc " + weaponType;
    }

}
