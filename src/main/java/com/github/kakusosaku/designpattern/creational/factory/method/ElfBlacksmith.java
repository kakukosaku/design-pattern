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
public class ElfBlacksmith implements Blacksmith {

    private static Map<WeaponType, ElfWeapon> ELF_ARSENAL;

    static {
        ELF_ARSENAL = new HashMap<>(WeaponType.values().length);
        Arrays.stream(WeaponType.values()).forEach(weaponType -> ELF_ARSENAL.put(weaponType, new ElfWeapon(weaponType)));
    }

    @Override
    public Weapon manufactureWeapon(WeaponType weaponType) {
        return ELF_ARSENAL.get(weaponType);
    }

}
