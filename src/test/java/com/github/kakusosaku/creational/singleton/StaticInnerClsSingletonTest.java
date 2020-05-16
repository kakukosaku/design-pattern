package com.github.kakusosaku.singleton;

import org.junit.Test;

import static org.junit.Assert.assertEquals;


/**
 * Description
 *
 * @author kaku
 * Date    2020-01-30
 */
public class StaticInnerClsSingletonTest {

    @Test
    public void getInstanceTest() {
        StaticInnerClsSingleton inst1 = StaticInnerClsSingleton.getInstance();
        StaticInnerClsSingleton inst2 = StaticInnerClsSingleton.getInstance();
        assertEquals(inst1, inst2);
    }
}
