package com.github.kakusosaku.designpattern.creational.factory.method;

/**
 * Description
 *
 * @author kaku
 * Date    6/11/21
 */
public class Summary {

    public static void main(String[] args) {
        Blacksmith elfBlacksmith = new ElfBlacksmith();
        Weapon elfSwordWeapon = elfBlacksmith.manufactureWeapon(WeaponType.SHORT_SWORD);
        System.out.println(elfSwordWeapon);

        Blacksmith orcBlacksmith = new OrcBlacksmith();
        Weapon orcSwordWeapon = orcBlacksmith.manufactureWeapon(WeaponType.SHORT_SWORD);
        System.out.println(orcSwordWeapon);
    }

}
