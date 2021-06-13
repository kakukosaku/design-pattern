package com.github.kakusosaku.designpattern.creational.factory.method;

/**
 * Description
 *
 * @author kaku
 * Date    6/11/21
 */
public class ElfWeapon implements Weapon {

    private WeaponType weaponType;

    public ElfWeapon(WeaponType weaponType) {
        this.weaponType = weaponType;
    }

    @Override
    public WeaponType getWeaponType() {
        return weaponType;
    }

    @Override
    public String toString() {
        return "Elven" + weaponType;
    }
}
