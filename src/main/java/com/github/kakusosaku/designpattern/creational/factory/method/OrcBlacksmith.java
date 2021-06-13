package com.github.kakusosaku.designpattern.creational.factory.method;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Description
 *
 * @author kaku
 * Date    6/11/21
 */
public class OrcBlacksmith implements Blacksmith {

    private static Map<WeaponType, OrcWeapon> ORC_ARSENAL;

    static {
        ORC_ARSENAL = new HashMap<>(WeaponType.values().length);
        Arrays.stream(WeaponType.values()).forEach(type -> ORC_ARSENAL.put(type, new OrcWeapon(type)));
    }

    @Override
    public Weapon manufactureWeapon(WeaponType weaponType) {
        return ORC_ARSENAL.get(weaponType);
    }

}
