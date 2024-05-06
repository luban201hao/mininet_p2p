package com.mininet.test;

import com.mininet.config.Config;
import com.mininet.generate.Final_OA;

public class Final_OA_test {
    public static void main(String[] args) throws Exception {
        Config.setDisInterStarAndCalc((int)(2*Math.PI*(6371.0+780)/20.0));
        Config.setDisStarEarthAndCalc(780);
        Final_OA.clearTrash();
        // latM = 67.5, f = 1/2 P
        Final_OA final_oa=new Final_OA(6,20,12,6,60,"AS_240_6.py","/mnt/hgfs/vm_new/test_data/AS_240_6/");
        final_oa.gen();
    }
}
