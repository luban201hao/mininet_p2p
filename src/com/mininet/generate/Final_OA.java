package com.mininet.generate;

import com.mininet.utils.CalUpDown;

import java.io.File;
import java.io.IOException;

public class Final_OA {
    private int AS_total;
    private int n;
    private int P;
    private int F;
    private double latM;
    private String topoPath;
    private String running_dir;

    public Final_OA(int AS_total, int n, int p, int f, double latM, String topoPath, String running_dir) {
        this.AS_total = AS_total;
        this.n = n;
        this.P = p;
        this.F = f;
        this.latM = latM;
        this.topoPath = topoPath;
        this.running_dir = running_dir;
    }

    public void gen() throws Exception {
        int orbit_per_AS=P/AS_total;

        OA_ospf_conf oa_conf=new OA_ospf_conf(AS_total,n,orbit_per_AS);
        oa_conf.mkisls("AS_isls.txt");

        CalUpDown calUpDown=new CalUpDown(n,P,F,latM,"AS_up_down.txt","AS_isls.txt",AS_total);
        calUpDown.calc();
        calUpDown.write_isls();
        calUpDown.make_router_lsdb();
        calUpDown.make_ase_lsdb();
        calUpDown.make_neighbor();

        oa_conf.make_eth_link("AS_isls.txt","AS_eth.txt","AS_link.txt",calUpDown.getK());
        oa_conf.maketopo("AS_eth.txt","AS_link.txt",topoPath,running_dir,calUpDown.getK(),n,P,calUpDown.getPhaseCount());

        calUpDown.make_ospf_conf("AS_eth.txt","ospf_conf",running_dir);
        calUpDown.make_inter_oa("AS_eth.txt",running_dir);
        calUpDown.make_se_info();
        calUpDown.make_se_ase_info();
        calUpDown.makeStation();
        calUpDown.Draw();
    }

    public static void clearDir(String dir)
    {
        File directory = new File(dir);
        for(String child:directory.list())
        {
            System.out.println(child);
            File childFile=new File(directory.getAbsoluteFile()+"/"+child);
            childFile.delete();
        }
    }

    public static void clearTrash()
    {
        clearDir("as_se_ase_info");
        clearDir("as_se_info");
        clearDir("aseLsdb");
        clearDir("inter_oa");
        clearDir("neighbor");
        clearDir("ospf_conf");
        clearDir("routerLsdb");
        clearDir("station_info");

        File file1=new File("AS_eth.txt");
        file1.delete();
        file1=new File("AS_isls.txt");
        file1.delete();
        file1=new File("AS_link.txt");
        file1.delete();
        file1=new File("AS_up_down.txt");
        file1.delete();
    }

    public static void main(String[] args) {
        clearTrash();
    }
}
