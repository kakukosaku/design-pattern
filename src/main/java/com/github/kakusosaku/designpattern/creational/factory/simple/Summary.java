package com.github.kakusosaku.designpattern.creational.factory.simple;

/**
 * Description
 *
 * @author kaku
 * Date    6/10/21
 */
public class Summary {

    public static void main(String[] args) {
        Car car1 = CarFactory.getCar(CarType.FORD);
        System.out.println(car1.getDescription());

        Car car2 = CarFactory.getCar(CarType.FERRARI);
        System.out.println(car2.getDescription());
    }

}
