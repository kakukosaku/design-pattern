package com.github.kakusosaku.designpattern.creational.factory.simple;

/**
 * Description
 *
 * @author kaku
 * Date    6/10/21
 */
public class CarFactory {

    public static Car getCar(CarType carType) {
        return carType.getConstructor().get();
    }

}
