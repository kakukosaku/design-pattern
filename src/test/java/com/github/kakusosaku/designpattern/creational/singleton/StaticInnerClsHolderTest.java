package com.github.kakusosaku.designpattern.creational.singleton;

import org.junit.Test;

import static org.junit.Assert.assertEquals;


/**
 * Description
 *
 * @author kaku
 * Date    2020-01-30
 */
public class StaticInnerClsHolderTest {

    @Test
    public void getInstanceTest() {
        StaticInnerClsHolder inst1 = StaticInnerClsHolder.getInstance();
        StaticInnerClsHolder inst2 = StaticInnerClsHolder.getInstance();
        assertEquals(inst1, inst2);
    }
}
