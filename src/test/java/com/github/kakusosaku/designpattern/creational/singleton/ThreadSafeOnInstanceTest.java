package com.github.kakusosaku.designpattern.creational.singleton;

import org.junit.Test;

import static org.junit.Assert.assertEquals;


/**
 * Description
 *
 * @author kaku
 * Date    2020-01-31
 */
public class ThreadSafeOnInstanceTest {

    @Test
    public void getInstanceTest() {
        ThreadSafeOnInstance inst1 = ThreadSafeOnInstance.getInstance();
        ThreadSafeOnInstance inst2 = ThreadSafeOnInstance.getInstance();
        assertEquals(inst1, inst2);
    }
}
