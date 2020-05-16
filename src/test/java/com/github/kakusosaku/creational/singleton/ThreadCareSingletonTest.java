package com.github.kakusosaku.singleton;

import org.junit.Test;

import static org.junit.Assert.assertEquals;


/**
 * Description
 *
 * @author kaku
 * Date    2020-01-31
 */
public class ThreadCareSingletonTest {

    @Test
    public void getInstanceTest() {
        ThreadCareSingleton inst1 = ThreadCareSingleton.getInstance();
        ThreadCareSingleton inst2 = ThreadCareSingleton.getInstance();
        assertEquals(inst1, inst2);
    }
}
