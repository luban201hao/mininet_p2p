package com.mininet.utils;

import com.mininet.config.Config;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.swing.*;
import java.awt.*;

public class CalUpDown {
    private static final double PI=180;

    private int n;
    private int P;
    private int F;
    private double latM;

    private int AS_total;

    private int k;
    private int phaseCount;
    int x0,y0;
    double point1,point2,point3,point4;
    String resultPath;
    String islsPath;
    List<List<link_info>> link_infos;

    public int getK() {
        return k;
    }
    public int getPhaseCount(){return phaseCount;}

    public CalUpDown(int n, int p, int f, double latM, String resultPath, String islsPath, int AS_total) {
        this.n = n;
        P = p;
        F = f;
        this.latM=latM;
        this.resultPath = resultPath;
        this.islsPath = islsPath;
        this.AS_total=AS_total;
        link_infos=new ArrayList<>();
    }

    static public boolean isInteger(double x)
    {
        double x_floor=Math.floor(x);
        double diff=x-x_floor;
        if(diff<=0.5)
        {
            if(Math.abs(x-x_floor)<1e-6)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            double x_ceil=Math.ceil(x);
            if(Math.abs(x-x_ceil)<1e-6)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }

    public void calcK()
    {
        //z从1增加到100，假如出现整数且小于P，认为K存在，
        double tmp=(double)P/(double)F;
        for(int z=1;z<=100;++z)
        {
            if(isInteger(z*tmp))
            {
                this.k=(int)Math.round(z*tmp);
                break;
            }
            if(z*tmp>=P)
            {
                this.k=P;
                break;
            }
        }
    }

    public void calPhaseCount()
    {
        int kn=this.k*this.n;
        if(kn%2==0)
        {
            System.out.println("kn%2=0,result="+kn*(0.5-this.latM/PI));
            if(isInteger(kn*(0.5-this.latM/PI)))
            {
                this.phaseCount=kn;
            }
            else
            {
                this.phaseCount=2*kn;
            }
        }
        else
        {
            //注意 1/2结果为0，因而整数和整数相除，结果取为整数
            System.out.println("kn%2!=0,result1="+kn*(0.5-this.latM/PI)+",result2="+kn*(1-this.latM/PI));
            if(isInteger(kn*(0.5-this.latM/PI)) || isInteger(kn*(1-this.latM/PI)))
            {
                this.phaseCount=2*kn;
            }
            else
            {
                this.phaseCount=4*kn;
            }
        }
        //分配通断信息数组

    }

    //初始化参数，并将通断向量全部置为0
    public void init_para()
    {
        this.point1=this.latM-(2*PI/(double)(n*k));
        this.point2=PI-this.latM;
        this.point3=PI+this.latM-(2*PI/(double)(n*k));
        this.point4=2*PI-this.latM;

        //建立link_info list
        for(int i=0;i<this.k;++i)
        {
            List<link_info> tmp=new ArrayList<>();
            for(int j=0;j<this.n;++j)
            {
                double lat_left=latM+(2*PI*(double)i)/((double)n*(double)k)-2*PI*(double)j/(double)n;
                double lat_right=lat_left+2*PI/n;
                if(lat_left<0)
                {
                    lat_left+=2*PI;
                }
                if(lat_right<0)
                {
                    lat_right+=2*PI;
                }
                else if(lat_right>2*PI)
                {
                    lat_right-=2*PI;
                }
                link_info link_info_tmp=new link_info(lat_left,lat_right,i,j,this.phaseCount);
                tmp.add(link_info_tmp);
            }
            this.link_infos.add(tmp);
        }
    }
    //判断通断性
    boolean break_or_not(link_info link_info_tmp)
    {
        //此处如果只差一点点，应当判断为通，防止误差
        if(link_info_tmp.getLat_left()>point1+1e-6 && link_info_tmp.getLat_left()<point2-1e-6)
        {
            return true;
        }
        if(link_info_tmp.getLat_left()>point3+1e-6 && link_info_tmp.getLat_left()<point4-1e-6)
        {
            return true;
        }
        return false;
    }
    //找出下一步需要增加的纬度
    double find_lat_add()
    {
        double tmp=PI;
        double nearest=PI;
        for(int i=0;i<k;++i)
        {
            for(int j=0;j<n;++j)
            {
                double lat_left=this.link_infos.get(i).get(j).getLat_left();
                if(lat_left>0 && lat_left<=point1)
                {
                    tmp=point1-lat_left;
                }
                else if(lat_left>point4 && lat_left<=2*PI)
                {
                    tmp=2*PI-lat_left+point1;
                }
                else if(lat_left>point1 && lat_left<=point2)
                {
                    tmp=point2-lat_left;
                }
                else if(lat_left>point2 && lat_left<=point3)
                {
                    tmp=point3-lat_left;
                }
                else if(lat_left>point3 && lat_left<=point4)
                {
                    tmp=point4-lat_left;
                }
                else
                {
                    System.out.println("invalid lat_left:"+lat_left);
                }
                if(Math.abs(tmp)<1e-6)
                {
                    continue;
                }
                if(tmp<nearest)
                {
                    nearest=tmp;
                }
            }
        }
        System.out.println("last find, add_lat="+nearest);
        return nearest;
    }

    //增加纬度
    void add_lat(double lat_add)
    {
        for(int i=0;i<k;++i)
        {
            for(int j=0;j<n;++j)
            {
                double lat_left=link_infos.get(i).get(j).getLat_left();
                double lat_right=link_infos.get(i).get(j).getLat_right();
                lat_left+=lat_add;
                lat_right+=lat_add;
                if(lat_left>2*PI)
                {
                    lat_left-=2*PI;
                }
                if(lat_right>2*PI)
                {
                    lat_right-=2*PI;
                }
                link_infos.get(i).get(j).setLat_left(lat_left);
                link_infos.get(i).get(j).setLat_right(lat_right);
            }
        }
    }


    //首先计算k值范围内的通短性，其余对应到k值范围内的位置
    public void calc()
    {
        calcK();
        calPhaseCount();
        init_para();

        System.out.println("this.k="+this.k);
        System.out.println("this.phaseCount="+this.phaseCount);

        int q=0;
        double lat_add;
        double lat_add_accumulate=0;

        while(q<this.phaseCount)
        {
            //判断每条链路在此时隙是否处于断开状态，如果是，将向量对应处设置为1
            for(int i=0;i<k;++i)
            {
                for(int j=0;j<n;++j)
                {
                    if(break_or_not(link_infos.get(i).get(j)))
                    {
                        link_infos.get(i).get(j).getPhase_matrix()[q]=1;
                    }
                }
            }

            lat_add=find_lat_add();
            add_lat(lat_add);
            ++q;
            lat_add_accumulate+=lat_add;
            System.out.println("lat_accumulate="+lat_add_accumulate);
        }
    }

    public void print_info(String outputPath) throws IOException {
        FileWriter fileWriter=new FileWriter(outputPath);
        for(int i=0;i<this.k;++i)
        {
            for(int j=0;j<this.n;++j)
            {
                link_info link_info_tmp=this.link_infos.get(i).get(j);
                fileWriter.write(link_info_tmp.getLat_left()+","+link_info_tmp.getLat_right()+","+link_info_tmp.getX0()+","+link_info_tmp.getY0()+","+link_info_tmp.getPhase_count()+"\n");
                for(int k=0;k<link_info_tmp.getPhase_count();++k)
                {
                    fileWriter.write(link_info_tmp.getPhase_matrix()[k]+",");
                }
                fileWriter.write("\n");
            }
        }
        fileWriter.close();
    }

    public void write_isls() throws Exception {
        String[][] isls= FileToMatrix.fileToString(islsPath);
        FileWriter fileWriter=new FileWriter(resultPath);
        System.out.println("in func write_isls");
        //写入时隙数量
        //将0时隙都设置为可用，以便进行计算
//        for(int i=0;i<k;++i)
//        {
//            for(int j=0;j<n;++j)
//            {
//                this.link_infos.get(i).get(j).getPhase_matrix()[0]=0;
//            }
//        }

        fileWriter.write(this.phaseCount+"\n");
        //首先写入k范围内的
        for(int i=0;i<k;++i)
        {
            for(int j=0;j<n;++j)
            {
                //找出此处i、j对应的信息，然后写入通断信息向量，注意只取左侧的
                for(int m=0;m<isls.length;++m)
                {
                    //System.out.println(Integer.valueOf(isls[m][0])+","+ Integer.valueOf(i*n+j) +"," +Integer.valueOf(isls[m][0])+","+ Integer.valueOf(i*n+j+n));
                    if(Integer.valueOf(isls[m][0]).equals( Integer.valueOf(i*n+j) ) && Integer.valueOf(isls[m][1]).equals( Integer.valueOf(i*n+j+n)) )
                    {
                        System.out.println(Integer.valueOf(isls[m][0])+","+ Integer.valueOf(i*n+j) +"," +Integer.valueOf(isls[m][1])+","+ Integer.valueOf(i*n+j+n));
                        //写入原来的行
                        fileWriter.write(isls[m][0]+","+isls[m][1]+","+isls[m][2]+","+isls[m][3]+","+isls[m][4]+"\n");
                        //写入通断信息矩阵
                        for(int z=0;z<this.phaseCount;++z)
                        {
                            fileWriter.write(this.link_infos.get(i).get(j).getPhase_matrix()[z]+",");
                        }
                        fileWriter.write("\n");
                    }
                }
            }
        }
        //假如k<P，继续写入
        if(k<P-1)
        {
            for(int i=k;i<P-1;++i)
            {
                for(int j=0;j<n;++j)
                {
                    //找出在0-k范围内对应的j值，并记录为j1
                    int cha=i/k;
                    int j1=j-k*cha;
                    while(j1<0)
                    {
                        j1+=n;
                    }
                    int i1=i%k;
                    System.out.println("i="+i+",j="+j+",i1="+i1+",j1="+j1+",cha="+cha);
                    //找出此处i、j对应的信息，然后写入通断信息向量，注意只取左侧的
                    for(int m=0;m<isls.length;++m)
                    {
                        if(Integer.valueOf(isls[m][0])==i*n+j && Integer.valueOf(isls[m][1])==i*n+j+n)
                        {
                            //写入原来的行
                            fileWriter.write(isls[m][0]+","+isls[m][1]+","+isls[m][2]+","+isls[m][3]+","+isls[m][4]+"\n");
                            //写入j1对应的通断信息矩阵
                            for(int z=0;z<this.phaseCount;++z)
                            {
                                fileWriter.write(this.link_infos.get(i1).get(j1).getPhase_matrix()[z]+",");
                            }
                            fileWriter.write("\n");
                        }
                    }
                }
            }
        }
        //写入轨道内链路的信息，全通
        for(int m=0;m<isls.length;++m)
        {
            if(Integer.valueOf(isls[m][0])+this.n!=Integer.valueOf(isls[m][1]))
            {
                fileWriter.write(isls[m][0]+","+isls[m][1]+","+isls[m][2]+","+isls[m][3]+","+isls[m][4]+"\n");
                for(int z=0;z<this.phaseCount;++z)
                {
                    fileWriter.write("0,");
                }
                fileWriter.write("\n");
            }
        }

        fileWriter.close();
    }

    public void make_router_lsdb() throws Exception {
        int AS_num=AS_total;
        int orbit_per_AS=P/AS_num;
        IpUtils32 ipUtils_routerid=new IpUtils32(20,0);
        IpUtils32 ipUtils_neighbor=new IpUtils32(20,0);
        IpUtils172 ipUtils_if_self172=new IpUtils172();
        IpUtils_AS ipUtils_se=new IpUtils_AS(10,0,0);

        String[][] isls_link=FileToMatrix.fileToString(this.resultPath);

        //第一个int表示编号，第二个int表示在isls_link中第一行的行号
        Map<Integer,List<Integer>> leo_link_map=new HashMap<>();

        System.out.println("begin find leo_link_map");
        for(int i=0;i<n*P;++i)
        {
            List<Integer> tmpList=new ArrayList<>();
            for(int a=1;a<isls_link.length;a=a+2)
            {
                //System.out.println(Integer.valueOf(isls_link[a][0])+","+Integer.valueOf(isls_link[a][1])+","+i);
                if(Integer.valueOf(isls_link[a][0])==i || Integer.valueOf(isls_link[a][1])==i )
                {
                    //添加信息
                    if(isls_link[a][2].toCharArray()[0]=='A') {
                        System.out.println("add Map<" + i + ",[" + a + "]>");
                        tmpList.add(a);
                    }
                }
            }
            leo_link_map.put(i,tmpList);
        }

        for(int i=0;i<AS_num;++i)
        {
            FileWriter fileWriter= new FileWriter("routerLsdb/as"+i+"_router.lsdb");
            //找出轨道区内的每颗卫星，其中a表示轨道号，b表示轨道内编号
            for(int a=i*orbit_per_AS;a<i*orbit_per_AS+orbit_per_AS;++a)
            {
                for(int b=0;b<n;++b)
                {
                    int leo_num=a*n+b;
                    List<Integer> tmpList=leo_link_map.get(leo_num);

                    System.out.println(leo_num);
                    //
                    int length=tmpList.size()*24+24+12;

                    //写出其router_id
                    ipUtils_routerid.setIp2Ip3(0,leo_num);
                    String router_id=ipUtils_routerid.ipStr;
                    //此处lsh->options=2表示支持外部路由
                    fileWriter.write("!,0,2,1,"+router_id+","+router_id+",-2147483644,0,"+length+",\n");
                    //写入第二行
                    fileWriter.write("@,2,0,"+(2*tmpList.size()+1)+","+this.phaseCount+",\n");
                    //找出所有的轨道区内链路
                    for(int c=0;c<tmpList.size();++c)
                    {
                        int link_line=tmpList.get(c);
                        //01节点为自身，10节点为对面
                        if(Integer.valueOf(isls_link[link_line][0])==leo_num)
                        {
                            ipUtils_neighbor.setIp2Ip3(0,Integer.valueOf(isls_link[link_line][1]));
                            ipUtils_if_self172.setIp2Ip3(Integer.valueOf(isls_link[link_line][3]),Integer.valueOf(isls_link[link_line][4]));
                            //router_id统一用00
                            fileWriter.write("#,1,"+ipUtils_neighbor.ipStr+","+ipUtils_if_self172.ipStr01+",10,");
                        }
                        //10为自身，01为对面
                        else if(Integer.valueOf(isls_link[link_line][1])==leo_num)
                        {
                            ipUtils_neighbor.setIp2Ip3(0,Integer.valueOf(isls_link[link_line][0]));
                            ipUtils_if_self172.setIp2Ip3(Integer.valueOf(isls_link[link_line][3]),Integer.valueOf(isls_link[link_line][4]));
                            //router_id统一用00
                            fileWriter.write("#,1,"+ipUtils_neighbor.ipStr+","+ipUtils_if_self172.ipStr10+",10,");
                        }

                        for(int d=0;d<this.phaseCount;++d)
                        {
                            fileWriter.write(isls_link[link_line+1][d]+",");
                        }
                        fileWriter.write("\n");
                        fileWriter.write("#,3,"+ipUtils_if_self172.ipStr00+",255.255.255.252,10,");
                        for(int d=0;d<this.phaseCount;++d)
                        {
                            fileWriter.write("0,");
                        }
                        fileWriter.write("\n");
                    }

                    //写出此处初始星地接口IP地址
                    int x=a;
                    int y=b-a/k;
                    while(y<0)
                    {
                        y+=n;
                    }
                    ipUtils_se.setIp2Ip3(x,y);
                    fileWriter.write("#,5,"+ipUtils_se.ipStr0+",255.255.255.0,10,");
                    for(int d=0;d<this.phaseCount;++d)
                    {
                        fileWriter.write("0,");
                    }
                    fileWriter.write("\n");
                    System.out.println(ipUtils_se.ipStr0+","+ipUtils_routerid.ipStr);
                }
            }

            fileWriter.close();
        }
    }

    public void make_ase_lsdb() throws Exception
    {
        int AS_num=AS_total;
        int orbit_per_AS=P/AS_num;
        IpUtils32 ipUtils_routerid=new IpUtils32(20,0);
        IpUtils172 ipUtils_as_other172=new IpUtils172();
        //a表示轨道号，b表示轨道内编号
        int a,b,leo_num;
        String[][] isls_link=FileToMatrix.fileToString(this.resultPath);

        Map<Integer,Integer> leo_linkB_map=new HashMap<>();
        int AS_left_count,AS_right_count;

        for(int i=0;i<n*P;++i)
        {
            for(int x=1;x<isls_link.length;x+=2)
            {
                if(Integer.valueOf(isls_link[x][0])==i || Integer.valueOf(isls_link[x][1])==i )
                {
                    //添加信息
                    if(isls_link[x][2].toCharArray()[0]=='B') {
                        System.out.println("add Map<" + i + "," + x + ">");
                        leo_linkB_map.put(i,x);
                        break;
                    }
                }
            }
        }

        for(int i=0;i<AS_num;++i)
        {
            FileWriter fileWriter= new FileWriter("aseLsdb/as" + i + "_ase.lsdb");

            //左侧一列
            if(i!=0)
            {
                a=orbit_per_AS*i;

                for(b=0;b<n;++b)
                {
                    leo_num=a*n+b;
                    //找出此卫星对应的B类链路在isls_link中的行号
                    int line_number=leo_linkB_map.get(leo_num)+1;

                    ipUtils_routerid.setIp2Ip3(0,leo_num);
                    //找出左侧所有轨道区
                    for(int c=0;c<i;++c)
                    {
                        ipUtils_as_other172.setIp2(c);
                        fileWriter.write("!,0,2,5,"+ipUtils_as_other172.ipStr00+","+ipUtils_routerid.ipStr+",-2147483645,0,36\n");
                        fileWriter.write("@,255.255.240.0,0,0,0,20,0.0.0.0,0,\n");
                        fileWriter.write("#,"+this.phaseCount+",");
                        for(int d=0;d<this.phaseCount;++d)
                        {
                            fileWriter.write(isls_link[line_number][d]+",");
                        }
                        fileWriter.write("\n");
                    }

                    AS_left_count=i;

                }//end for b


            }//end for i

            //右侧一列
            if(i!=AS_num-1)
            {
                a=(i+1)*orbit_per_AS-1;
                for(b=0;b<n;++b)
                {
                    leo_num=a*n+b;
                    //找出此卫星对应的B类链路在isls_link中的行号
                    int line_number=leo_linkB_map.get(leo_num)+1;

                    ipUtils_routerid.setIp2Ip3(0,leo_num);
                    //找出左侧所有轨道区
                    for(int c=i+1;c<AS_num;++c)
                    {
                        ipUtils_as_other172.setIp2(c);
                        //router_id取为00
                        fileWriter.write("!,0,2,5,"+ipUtils_as_other172.ipStr00+","+ipUtils_routerid.ipStr+",-2147483645,0,36\n");
                        //子网掩码为16位
                        fileWriter.write("@,255.255.240.0,0,0,0,20,0.0.0.0,0,\n");
                        fileWriter.write("#,"+this.phaseCount+",");
                        for(int d=0;d<this.phaseCount;++d)
                        {
                            fileWriter.write(isls_link[line_number][d]+",");
                        }
                        fileWriter.write("\n");
                    }

                }

            }
            fileWriter.close();
            //as_se_ase_info.close();
        }
    }

    public void make_neighbor() throws Exception {
        int a,b;
        IpUtils32 ipUtils_routerid=new IpUtils32(20,0);
        String[][] isls_link=FileToMatrix.fileToString(this.resultPath);

        //第一个int表示编号，第二个int表示在isls_link中第一行的行号
        Map<Integer,List<Integer>> leo_link_map=new HashMap<>();
        System.out.println("in func make neighbor");
        for(int i=0;i<n*P;++i)
        {
            List<Integer> tmpList=new ArrayList<>();
            for(int x=1;x<isls_link.length;x=x+2)
            {
                if(Integer.valueOf(isls_link[x][0])==i || Integer.valueOf(isls_link[x][1])==i )
                {
                    //添加信息，无论是A类还是B类的链路，都要添加
                    System.out.println("add Map<" + i + ",[" + x + "]>");
                    tmpList.add(x);
                }
            }
            leo_link_map.put(i,tmpList);
        }
        for(a=0;a<P;++a)
        {
            for(b=0;b<n;++b)
            {
                int leo_num=a*n+b;
                FileWriter fileWriter=new FileWriter("neighbor/neighbor"+leo_num+".conf");

                if(a==0 || a==P-1)
                {
                    fileWriter.write("3,");
                }
                else
                {
                    fileWriter.write("4,");
                }
                fileWriter.write(this.phaseCount+"\n");

                List<Integer> tmpList=leo_link_map.get(leo_num);
                for(int c=0;c<tmpList.size();++c)
                {
                    int link_line=tmpList.get(c);
                    //自己为1号节点
                    if(Integer.valueOf(isls_link[link_line][0])==leo_num)
                    {
                        ipUtils_routerid.setIp2Ip3(0,Integer.valueOf(isls_link[link_line][1]));
                    }
                    //自己为2号节点
                    if(Integer.valueOf(isls_link[link_line][1])==leo_num)
                    {
                        ipUtils_routerid.setIp2Ip3(0,Integer.valueOf(isls_link[link_line][0]));
                    }
                    fileWriter.write(ipUtils_routerid.ipStr+",");
                    for(int d=0;d<this.phaseCount;++d)
                    {
                        fileWriter.write(isls_link[link_line+1][d]+",");
                    }
                    fileWriter.write("\n");
                }//end for c
                fileWriter.close();
            }//end for b
        }//end for a
    }
    public void make_ospf_conf(String ethpath,String ospf_dir,String running_dir) throws Exception {
        String[][] ethlist;
        ethlist= FileToMatrix.fileToString(ethpath); //此处输出二维矩阵，网卡较少的leo出现null
        FileWriter fileWriter,fileWriter1;
        char linkType;
        int isASBR;
        int leo_in_a_AS=n*P/AS_total;
        int orbitPerAS=P/AS_total;

        int interAS_sub128,interAS,end_number;

        IpUtils172 ipUtils172=new IpUtils172();
        IpUtils32 ipUtils_routerid=new IpUtils32(20,0);
        for(int i=0;i<ethlist.length;++i){
            isASBR=0;
            //开始写入ospfd.conf，其中i表示卫星编号
            fileWriter=new FileWriter(ospf_dir+"/"+ethlist[i][0]+"ospfd.conf");
            fileWriter.write("! -*- ospf -*-\n");
            fileWriter.write("hostname "+ethlist[i][0]+"_ospfd\n");
            fileWriter.write("password zebra\n");
            fileWriter.write("enable password zebra\n");
            fileWriter.write("!\n");
            fileWriter.write("router ospf\n");

            fileWriter.write(" ospf router-id "+ipUtils_routerid.ipStr +"\n");
            ipUtils_routerid.addIp(1);

            int j=2;
            do {
                linkType=ethlist[i][j+1].toCharArray()[0];
                if(linkType=='A'){
                    fileWriter.write(" network " + ethlist[i][j] + " area 0.0.0.0\n");
                }else{
                    isASBR=1;
                }
                j += 3;
            } while (j < ethlist[0].length && ethlist[i][j] != null);
            if(isASBR==1){
                fileWriter.write("redistribute kernel metric-type 1\n");
                fileWriter.write("redistribute connected metric-type 1\n");
            }
            j=1;
            do {
                linkType=ethlist[i][j+2].toCharArray()[0];
                if(linkType=='A'){
                    fileWriter.write("interface "+ ethlist[i][j]+"\n");
                    fileWriter.write(" ip ospf network point-to-point\n");
                    fileWriter.write(" ip ospf hello-interval 3\n");
                    fileWriter.write(" ip ospf dead-interval 12\n");
                }
                j += 3;
            } while (j < ethlist[0].length && ethlist[i][j] != null);

            fileWriter.write("set_phase_all "+this.phaseCount+"\n");
            fileWriter.write("readneighbor "+running_dir+"neighbor/neighbor"+i+".conf\n");
            int AS_this=i/leo_in_a_AS;
            fileWriter.write("inputlsdb "+running_dir+"routerLsdb/as"+AS_this+"_router.lsdb\n");
            fileWriter.write("ase_input "+running_dir+"aseLsdb/as"+AS_this+"_ase.lsdb\n");
            fileWriter.write("input_se_info "+running_dir+"as_se_info/as"+AS_this+"_se_info.conf\n");
            //fileWriter.write("input_se_ase_info "+running_dir+"as_se_ase_info/as"+AS_this+"_se_ase.conf\n");

            if(i==0)
            {
                if(Config.isServer == 0) {
                    fileWriter.write("log file /mnt/hgfs/vm_new/ospflog/leo0ospfd.log");
                }
                else
                {
                    fileWriter.write("log file /home/test/wyc/ospflog/leo0ospfd.log");
                }
            }
            if(i==(n*P/AS_total))
            {
                System.out.println("log file /mnt/hgfs/vm_new/ospflog/leo"+i+"ospfd.log");
                if(Config.isServer == 0) {
                    fileWriter.write("log file /mnt/hgfs/vm_new/ospflog/leo" + i + "ospfd.log");
                }else{
                    fileWriter.write("log file /home/test/wyc/ospflog/leo" + i + "ospfd.log");
                }
            }


            fileWriter.close();

            //开始写入zebra.conf
            fileWriter1=new FileWriter(ospf_dir+"/"+ethlist[i][0]+"zebra.conf");
            j=2;
            fileWriter1.write("hostname Router\n");
            fileWriter1.write("password zebra\n");
            fileWriter1.write("enable password zebra\n");

//            do{
//                linkType=ethlist[i][j+1].toCharArray()[0];
//                if(linkType=='B'){
//
//                    System.out.println(ethlist[i][j]);
//
//                    interAS=IpUtils172.getIP2(ethlist[i][j]);
//                    interAS_sub128=interAS-128;
//                    end_number=IpUtils172.getEnd(ethlist[i][j]);
//
//                    System.out.println(ethlist[i][j]+","+interAS+","+interAS_sub128+","+end_number);
//
//                    if(end_number%2==1){//发布右端AS
//                        for(int k=interAS_sub128+1;k<AS_total;++k){
//                            ipUtils172.setIp2Ip3(k,0);
//                            fileWriter1.write("ip route " + ipUtils172.ipStr00 +"/20 " +IpUtils_AS.ipStrPeer(ethlist[i][j])+"\n");
//
//                        }
//                        for(int k=interAS+1;k<128+AS_total-1;++k){
//                            ipUtils172.setIp2Ip3(k,0);
//                            fileWriter1.write("ip route " + ipUtils172.ipStr00 +"/20 " +IpUtils_AS.ipStrPeer(ethlist[i][j])+"\n");
//                        }
//
//                    }else{//发布左侧AS
//                        for(int k=interAS_sub128;k>=0;--k){
//                            ipUtils172.setIp2Ip3(k,0);
//                            fileWriter1.write("ip route " + ipUtils172.ipStr00 +"/20 " +IpUtils_AS.ipStrPeer(ethlist[i][j])+"\n");
//                        }
//                        for(int k=interAS-1;k>=128;--k){
//                            ipUtils172.setIp2Ip3(k,0);
//                            fileWriter1.write("ip route " + ipUtils172.ipStr00 +"/20 " +IpUtils_AS.ipStrPeer(ethlist[i][j])+"\n");
//                        }
//                    }
//                }
//                j += 3;
//            }while (j < ethlist[0].length && ethlist[i][j] != null);

            fileWriter1.close();
        }
    }

    public void make_inter_oa(String ethpath,String running_dir) throws Exception {
        String[][] ethlist;
        ethlist= FileToMatrix.fileToString(ethpath);
        System.out.println("in func make_inter_oa");
        //找出每个节点的星地接口或OA接口
        Map<Integer,List<String>> leo_se_map=new HashMap<>();
        Map<Integer,List<String>> leo_oa_map=new HashMap<>();
        int leo_in_a_AS=n*P/AS_total;
        for(int a=0;a<ethlist.length;++a)
        {
            for(int b=3;b<ethlist[a].length;++b)
            {
                if(ethlist[a][b]!=null)
                {
                    //添加星地接口
                    if(ethlist[a][b].toCharArray()[0]=='S')
                    {
                        List<String> tmpList=new ArrayList<>();
                        tmpList.add(ethlist[a][b-1]);
                        tmpList.add(ethlist[a][b-2]);
                        leo_se_map.put(a,tmpList);
                    }
                    //添加OA接口
                    if(ethlist[a][b].toCharArray()[0]=='B')
                    {
                        List<String> tmpList=new ArrayList<>();
                        //地址
                        tmpList.add(ethlist[a][b-1]);
                        //网卡名
                        tmpList.add(ethlist[a][b-2]);
                        leo_oa_map.put(a,tmpList);
                    }
                }
            }
        }
        for(int i=0;i<ethlist.length;++i)
        {
            int AS_this=i/leo_in_a_AS;
            FileWriter fileWriter=new FileWriter("inter_oa/inter_oa"+i+".conf");
            List<String> tmpList;
            if(leo_oa_map.containsKey(i))
            {
                tmpList=leo_oa_map.get(i);
                fileWriter.write("interface "+tmpList.get(1)+"\n");
                fileWriter.write(" ip ospf hello-interval 3\n");
                fileWriter.write(" ip ospf dead-interval 12\n");
                fileWriter.write(" if_inter_oa "+tmpList.get(0).split("/")[0]+" "+IpUtils_AS.ipStrPeer(tmpList.get(0))+"\n");
            }
            tmpList=leo_se_map.get(i);
            fileWriter.write("interface "+tmpList.get(1)+"\n");
            fileWriter.write(" if_se\n");
            fileWriter.write("input_se_ase_info "+running_dir+"as_se_ase_info/as"+AS_this +"_se_ase.conf\n");
            fileWriter.write("load_station "+running_dir+"station_info/station"+i+".conf\n");
            fileWriter.close();
        }
    }

    public void make_se_info() throws IOException {

        int orbit_per_AS=P/AS_total;
        //此处i表示AS号
        for(int i=0;i<AS_total;++i)
        {
            FileWriter fileWriter=new FileWriter("as_se_info/as"+i+"_se_info.conf");
            fileWriter.write(this.P+","+this.n+","+this.k+","+orbit_per_AS+"\n");
            for(int a=0;a<orbit_per_AS;++a)
            {
                //轨道号等于
                //k0可通过轨道号进行计算，与AS无关
                int orbit_num=a+orbit_per_AS*i;
                int k0=orbit_num%this.k;
                fileWriter.write(orbit_num+","+k0+"\n");
            }
            fileWriter.close();
        }
    }

    public void make_se_ase_info() throws Exception {
        int leo_in_a_AS=n*P/AS_total;
        int orbit_per_AS=P/AS_total;
        String[][] isls_link=FileToMatrix.fileToString(this.resultPath);
        Map<Integer,Integer> leo_linkB_map=new HashMap<>();
        IpUtils32 ipUtils_routerid=new IpUtils32(20,0);
        System.out.println("in func make_se_ase_info");
        for(int i=0;i<n*P;++i)
        {
            for(int x=1;x<isls_link.length;x+=2)
            {
                if(Integer.valueOf(isls_link[x][0])==i || Integer.valueOf(isls_link[x][1])==i )
                {
                    //添加信息
                    if(isls_link[x][2].toCharArray()[0]=='B') {
                        System.out.println("add Map<" + i + "," + x + ">");
                        leo_linkB_map.put(i,x);
                        break;
                    }
                }
            }
        }
        //此处i表示AS号
        for(int i=0;i<AS_total;++i)
        {
            FileWriter fileWriter=new FileWriter("as_se_ase_info/as"+i+"_se_ase.conf");
            if(i==0|| i==AS_total-1)
            {
                fileWriter.write(this.n+"\n");
            }
            else
            {
                fileWriter.write(2*this.n+"\n");
            }
            if(i!=0)
            {
                //写入左侧所有的router_id
                for(int x=0;x<n;++x)
                {
                    int leo_num=x+leo_in_a_AS*i;
                    int line_num=leo_linkB_map.get(leo_num);
                    ipUtils_routerid.setIp2Ip3(0,leo_num);

                    //左侧待发布的轨道数量
                    int orbit_left=orbit_per_AS*i;

                    fileWriter.write(ipUtils_routerid.ipStr+","+orbit_left+",");
                    for(int y=0;y<orbit_left;++y)
                    {
                        fileWriter.write(y+",");
                    }
                    fileWriter.write("\n");
                    fileWriter.write(this.phaseCount+",");
                    for(int y=0;y<this.phaseCount;++y)
                    {
                        fileWriter.write(isls_link[line_num+1][y]+",");
                    }
                    fileWriter.write("\n");
                }
            }
            if(i!=AS_total-1)
            {
                //写入右侧所有的router_id
                for(int x=0;x<n;++x)
                {
                    int leo_num = x + leo_in_a_AS * (i + 1) - n;
                    int line_num=leo_linkB_map.get(leo_num);
                    ipUtils_routerid.setIp2Ip3(0,leo_num);

                    //右侧的轨道数量
                    int orbit_right=(AS_total-i-1)*orbit_per_AS;

                    fileWriter.write(ipUtils_routerid.ipStr+","+orbit_right+",");
                    for(int y=(i+1)*orbit_per_AS;y<P;++y)
                    {
                        fileWriter.write(y+",");
                    }
                    fileWriter.write("\n");
                    fileWriter.write(this.phaseCount+",");
                    for(int y=0;y<this.phaseCount;++y)
                    {
                        fileWriter.write(isls_link[line_num+1][y]+",");
                    }
                    fileWriter.write("\n");
                }
            }
            fileWriter.close();
        }//end for i
    }

    public void makeStation()
    {
        String[][] stationInfo = null;
        try {
            stationInfo = FileToMatrix.fileToString("station.txt");
            if(stationInfo == null) {
                return;
            }
            for(int i=0;i<this.P; ++i)
            {
                for(int j=0;j<this.n;++j)
                {
                    FileWriter fileWriter=new FileWriter("station_info/station"+String.valueOf(i*this.n+j)+".conf");
                    fileWriter.write(this.n+","+this.P+","+this.k+","+this.P/this.AS_total+"\n");
                    int x0 = i;
                    int y0 = j - i/k;
                    if(y0 < 0)
                    {
                        y0+=n;
                    }
                    int k0 = i%k;
                    fileWriter.write(x0+","+y0+","+k0+"\n");
                    int station_n = Integer.valueOf(stationInfo[0][0]);
                    fileWriter.write(String.valueOf(station_n)+"\n");
                    for(int ii=1;ii<=station_n;++ii)
                    {
                        fileWriter.write(stationInfo[ii][0]+","+stationInfo[ii][1]+","+stationInfo[ii][2]+"\n");
                    }
                    fileWriter.close();
                }
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }


    }

    public void Draw()
    {
        JFrame ck = new JFrame();
        int x=1600;
        int y=1000;
        ck.setSize(x, y);
        ck.setLocationRelativeTo(null);
        ck.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Mypanel myhb = new Mypanel(this.n,this.P,"AS_eth.txt",x,y);
        ck.add(myhb);
        ck.setVisible(true);

//        myhb.MyPaint(ck.getGraphics());
//        myhb.addPhase();
//        myhb.paint(ck.getGraphics());

    }
}
