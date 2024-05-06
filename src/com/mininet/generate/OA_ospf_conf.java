package com.mininet.generate;

import com.mininet.config.Config;
import com.mininet.entity.tc_info_help;
import com.mininet.utils.FileToMatrix;
import com.mininet.utils.IpUtils172;
import com.mininet.utils.IpUtils_AS;

import java.io.FileWriter;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OA_ospf_conf {
    int AS_total; //自治系统的总数
    int leo_per_orbit;//每个轨道的卫星数量
    int orbit_per_AS;//每个AS内的轨道个数
    int orbit_all;

    public OA_ospf_conf(int AS_total, int leo_per_orbit, int orbit_per_AS) {
        this.AS_total = AS_total;
        this.leo_per_orbit = leo_per_orbit;
        this.orbit_per_AS = orbit_per_AS;
        this.orbit_all=AS_total*orbit_per_AS;
    }

    public void mkisls(String islspath) throws IOException {
        int orbit_num,row_num,AS_num;
        int id,column;
        FileWriter fileWriter=new FileWriter(islspath);
        //该条链路对应的第三位ip地址，写入isls文件中，便于后续直接使用
        int ip3;
        //对于AS内部链路进行列举
        for(AS_num=0;AS_num<AS_total;++AS_num){
            ip3=0;//对于每一个AS,ip3都从0开始计算
            //纵向链路连接
            for(orbit_num=0;orbit_num<orbit_per_AS;++orbit_num){
                //计算全局列数
                column=(AS_num*orbit_per_AS)+orbit_num;
                for(row_num=0;row_num<leo_per_orbit;++row_num){
                    //非首尾纵向链路连接
                    if(row_num<leo_per_orbit-1){

                        id=column*leo_per_orbit+row_num;
                        //写入纵向链路连接，卫星1，卫星1+1，A, AS号(作为ip地址第3位)
                        fileWriter.write(String.valueOf(id)+","+String.valueOf(id+1)+",A,"+String.valueOf(AS_num)+","+String.valueOf(ip3)+"\n");
                        ip3++;
                    }
                    //纵向链路头尾连接
                    else{
                        id=column*leo_per_orbit+row_num;

                        fileWriter.write(String.valueOf(id)+","+String.valueOf(column*leo_per_orbit)+",A,"+String.valueOf(AS_num)+","+String.valueOf(ip3)+"\n");
                        ip3++;
                    }
                }

            }
            //横向链路连接
            for(orbit_num=0;orbit_num<orbit_per_AS-1;++orbit_num){
                column=(AS_num*orbit_per_AS)+orbit_num;
                for(row_num=0;row_num<leo_per_orbit;++row_num){
                    id=column*leo_per_orbit+row_num;
                    fileWriter.write(String.valueOf(id)+","+String.valueOf(id+leo_per_orbit)+",A,"+String.valueOf(AS_num)+","+String.valueOf(ip3)+"\n");
                    ip3++;
                }

            }
        }

        //区域间链路
        int interIP2=128;
        for(AS_num=0;AS_num<AS_total-1;++AS_num){
            ip3=0;//每一对AS，ip3从0开始计算
            column=(AS_num*orbit_per_AS)+orbit_per_AS-1;
            for(row_num=0;row_num<leo_per_orbit;++row_num){
                id=column*leo_per_orbit+row_num;
                fileWriter.write(String.valueOf(id)+","+String.valueOf(id+leo_per_orbit)+",B,"+String.valueOf(interIP2)+","+String.valueOf(ip3)+"\n");
                ip3++;

            }
            interIP2++;
        }
        fileWriter.close();
    }//end func make_isls()

    public void make_eth_link(String islspath,String ethpath,String linkpath,int k) throws Exception {
        String[][] islslist;
        islslist = FileToMatrix.fileToString(islspath);
        int maxleo = 0;
        for (int i = 0; i < islslist.length; ++i) {
            if (Integer.parseInt(islslist[i][0]) > maxleo) {
                maxleo = Integer.parseInt(islslist[i][0]);
            }
            if (Integer.parseInt(islslist[i][1]) > maxleo) {
                maxleo = Integer.parseInt(islslist[i][1]);
            }
        }
        maxleo++;//实际卫星数比最大编号大1
        //网卡记录表和链路记录表
        String[] ethlist = new String[maxleo];
        String[] linklist = new String[islslist.length];
        int[] ethnum = new int[maxleo];

        for (int i = 0; i < maxleo; ++i) {
            ethlist[i] = "leo" + String.valueOf(i) + ",";
            ethnum[i] = 0;
        }
        for (int i = 0; i < islslist.length; ++i) {
            linklist[i] = "link" + String.valueOf(i) + ",";
        }
        //工具类，用于设置IP地址
        IpUtils172 ipUtils172=new IpUtils172();
        int source_num, dest_num, ip2, ip3;
        char linkType;

        for (int i = 0; i < islslist.length; ++i) {
            source_num = Integer.parseInt(islslist[i][0]);
            dest_num = Integer.parseInt(islslist[i][1]);
            linkType = islslist[i][2].toCharArray()[0];

            ip2 = Integer.parseInt(islslist[i][3]);
            ip3 = Integer.parseInt(islslist[i][4]);

            ipUtils172.setIp2Ip3(ip2, ip3);
            if (linkType == 'A') {
                ethlist[source_num] += "leo" + String.valueOf(source_num) + "-eth" + String.valueOf(ethnum[source_num]) + "," + ipUtils172.ipStr01 + "/30,A,";
                ethlist[dest_num] += "leo" + String.valueOf(dest_num) + "-eth" + String.valueOf(ethnum[dest_num]) + "," + ipUtils172.ipStr10 + "/30,A,";
                linklist[i] += "leo" + String.valueOf(source_num) + "," + "leo" + String.valueOf(source_num) + "-eth" + String.valueOf(ethnum[source_num]) + "," + ipUtils172.ipStr01 + "/30,";
                linklist[i] += "leo" + String.valueOf(dest_num) + "," + "leo" + String.valueOf(dest_num) + "-eth" + String.valueOf(ethnum[dest_num]) + "," + ipUtils172.ipStr10 + "/30,A";
                ethnum[source_num] += 1;
                ethnum[dest_num] += 1;

            } else {
                ethlist[source_num] += "leo" + String.valueOf(source_num) + "-eth" + String.valueOf(ethnum[source_num]) + "," + ipUtils172.ipStr01 + "/30,B,";
                ethlist[dest_num] += "leo" + String.valueOf(dest_num) + "-eth" + String.valueOf(ethnum[dest_num]) + "," + ipUtils172.ipStr10 + "/30,B,";
                linklist[i] += "leo" + String.valueOf(source_num) + "," + "leo" + String.valueOf(source_num) + "-eth" + String.valueOf(ethnum[source_num]) + "," + ipUtils172.ipStr01 + "/30,";
                linklist[i] += "leo" + String.valueOf(dest_num) + "," + "leo" + String.valueOf(dest_num) + "-eth" + String.valueOf(ethnum[dest_num]) + "," + ipUtils172.ipStr10 + "/30,B";
                ethnum[source_num] += 1;
                ethnum[dest_num] += 1;
            }
        }
        //ethlist中，写入星地接口
        IpUtils_AS ipUtils_se = new IpUtils_AS(10, 0, 0);
        for (int a = 0; a < AS_total * orbit_per_AS; ++a) {
            for (int b = 0; b < leo_per_orbit; ++b) {
                int leo_num = a * leo_per_orbit + b;
                System.out.println("in func make_link_eth,add se,leo_num=" + leo_num);
                int x = a;
                int y = b - a / k;
                while (y < 0) {
                    y += leo_per_orbit;
                }
                ipUtils_se.setIp2Ip3(x, y);
                ethlist[leo_num] += "leo" + leo_num + "-eth" + ethnum[leo_num] + "," + ipUtils_se.ipStr1 + "/24,S,";
            }
        }

        FileWriter fileWriter = new FileWriter(ethpath);
        for (int i = 0; i < maxleo; ++i) {  //maxleo比实际卫星数少1，也比行数少1
            fileWriter.write(ethlist[i]);
            fileWriter.write("\n");
            //System.out.println(ethlist[i]);
        }

        fileWriter.close();
        FileWriter fileWriter1 = new FileWriter(linkpath);
        for (int i = 0; i < linklist.length; ++i) {
            fileWriter1.write(linklist[i]);
            fileWriter1.write("\n");
            //System.out.println(ethlist[i]);
        }

        fileWriter1.close();
    }
    public void maketopo(String ethpath,String linkpath,String topopath,String running_dir,int k,int n,int P,int phaseAll) throws Exception{
        String[][] ethlist,linklist,updownlist;
        ethlist= FileToMatrix.fileToString(ethpath); //此处输出二维矩阵，网卡较少的leo出现null
        linklist=FileToMatrix.fileToString(linkpath);
        updownlist=FileToMatrix.fileToString("AS_up_down.txt");

        FileWriter fileWriter=new FileWriter(topopath);
        System.out.println("in func make topo");
        //找出每个卫星对应的星地接口的地址，并存入表中
        Map<Integer, List<String>> se_if_map=new HashMap<>();
        for(int a=0;a<ethlist.length;++a)
        {
            for(int b=3;b<ethlist[a].length;b+=3)
            {
                if(ethlist[a][b]!=null)
                {
                    if(ethlist[a][b].toCharArray()[0]=='S')
                    {
                        System.out.println("se_if_map add <"+a+","+ethlist[a][b-1]+">");
                        List<String> tmpList=new ArrayList<>();
                        tmpList.add(0,ethlist[a][b-1]);
                        tmpList.add(1,ethlist[a][b-2]);
                        tmpList.add(2,String.valueOf(2000+a));
                        se_if_map.put(a,tmpList);
                        break;
                    }
                }
            }
        }

        List<tc_info_help> tc_info_list=new ArrayList<>();
        //此处为了找出相邻的两个网卡以及其时隙信息，方便写入tc信息
        IpUtils172 ipUtils172=new IpUtils172();
        for(int a=0;a<P-1;++a)
        {
            for(int b=0;b<n;++b)
            {
                int num1=a*n+b;
                int num2=num1+n;
                int ip2 = 0,ip3=0,x;
                //找出一号对应
                for(x=1;x<updownlist.length;x+=2)
                {
                    if(Integer.valueOf(updownlist[x][0])==num1)
                    {
                        ip2=Integer.valueOf(updownlist[x][3]);
                        ip3=Integer.valueOf(updownlist[x][4]);
                        break;
                    }
                }
                String linkinfo="";
                for(int y=0;y<updownlist[x+1].length-1;++y)
                {
                    linkinfo+=updownlist[x+1][y]+",";
                }
                linkinfo+=updownlist[x+1][updownlist[x+1].length-1];
                ipUtils172.setIp2Ip3(ip2,ip3);
                String ip01str=ipUtils172.ipStr01;
                String ethname1="";
                String ethname2="";
                for(int y=0;y<linklist.length;++y)
                {
                    if(linklist[y][3].split("/")[0].equals(ip01str))
                    {
                        ethname1=linklist[y][2];
                        ethname2=linklist[y][5];
                    }
                }
                System.out.println(num1+","+num2+","+ethname1+","+ethname2+","+linkinfo);
                tc_info_help tcInfoHelp=new tc_info_help(num1,num2,ethname1,ethname2,linkinfo);
                tc_info_list.add(tcInfoHelp);
            }
        }
        String apiDir = "";
        if(Config.isServer == 1){
            apiDir = "/home/test";
        }
        else{
            apiDir = "/home/wyc";
        }
        fileWriter.write("import os\n");
        fileWriter.write("import time\n");
        fileWriter.write("from mininet.net import MininetE\n");
        fileWriter.write("from mininet.net import Mininet\n");
        fileWriter.write("from mininet.node import Node,ContainerHost\n");
        fileWriter.write("from mininet.topo import Topo\n");
        fileWriter.write("from mininet.node import Controller,RemoteController\n");
        fileWriter.write("from mininet.cli import CLI\n");
        fileWriter.write("from mininet.link import TCLink\n");
        fileWriter.write("from mininet.log import info, setLogLevel\n");
        fileWriter.write("setLogLevel('info')\n\n\n");
        fileWriter.write("class LinuxRouter( ContainerHost ):\n");
        fileWriter.write("    \"A Node with IP forwarding enabled.\"\n");
        fileWriter.write("    def config( self, **params ):\n");
        fileWriter.write("        super( LinuxRouter, self).config( **params )\n");
        fileWriter.write("        # Enable forwarding on the router\n");
        fileWriter.write("        self.cmd( 'sysctl net.ipv4.ip_forward=1' )\n");
        fileWriter.write("        self.cmd( 'ulimit -s unlimited' )\n");
        fileWriter.write("        self.cmd( 'sysctl net.ipv4.conf.all.rp_filter=2' )\n\n");
        fileWriter.write("    def terminate( self ):\n");
        fileWriter.write("        self.cmd( 'sysctl net.ipv4.ip_forward=0' )\n");
        fileWriter.write("        super( LinuxRouter, self ).terminate()\n\n\n");
        fileWriter.write("class NetworkTopo( Topo ):\n");
        fileWriter.write("    def build( self, **_opts ):\n");
        for(int i=0;i<ethlist.length;++i){
            fileWriter.write("        defaultIp" + ethlist[i][0] + " = '" + ethlist[i][2] + "'\n" );
        }
        fileWriter.write("\n");
        for(int i=0;i<ethlist.length;++i){
            fileWriter.write("        " + ethlist[i][0] + "= self.addNode('" +  ethlist[i][0] + "', cls=LinuxRouter, ip=defaultIp" + ethlist[i][0]+ ")\n");

        }
        fileWriter.write("        s1=self.addSwitch('s1')\n");
        fileWriter.write("\n");
        for(int i=0;i<linklist.length;++i) {
            if (Config.hasDelay == 1) {
                DecimalFormat decimalFormat = new DecimalFormat("#.######"); // 设置要显示的小数位数为6位
                String delayStr = decimalFormat.format(Config.delayInterStar);
                if (Config.lossInterStar >= 1e-4) {
                    String lossStr = decimalFormat.format(Config.lossInterStar);
                    fileWriter.write("        self.addLink(" + linklist[i][1] + "," + linklist[i][4] + ",infName1='" + linklist[i][2] + "',params1={'ip':'" + linklist[i][3] + "'},infName2='" + linklist[i][5] + "',params2={'ip':'" + linklist[i][6] + "'}, delay = '"+delayStr+"ms', loss = "+lossStr+")\n");
                }
                else{
                    fileWriter.write("        self.addLink(" + linklist[i][1] + "," + linklist[i][4] + ",infName1='" + linklist[i][2] + "',params1={'ip':'" + linklist[i][3] + "'},infName2='" + linklist[i][5] + "',params2={'ip':'" + linklist[i][6] + "'}, delay = '"+delayStr+"ms')\n");
                }
            } else {
                fileWriter.write("        self.addLink(" + linklist[i][1] + "," + linklist[i][4] + ",infName1='" + linklist[i][2] + "',params1={'ip':'" + linklist[i][3] + "'},infName2='" + linklist[i][5] + "',params2={'ip':'" + linklist[i][6] + "'})\n");
            }
        }
        fileWriter.write("\n");
        //增加星地网关之间的连接
        for(int i=0;i<se_if_map.size();++i) {
            List<String> tmpList = se_if_map.get(i);
            if (Config.hasDelay == 1) {
                DecimalFormat decimalFormat = new DecimalFormat("#.######"); // 设置要显示的小数位数为6位
                String delayStr = decimalFormat.format(Config.delayStarEarth);
                if (Config.lossStarEarth >= 1e-4) {
                    String lossStr = decimalFormat.format(Config.lossStarEarth);
                    fileWriter.write("        self.addLink(leo" + i + ",s1,intfName1='" + tmpList.get(1) + "',params1={'ip' : '" + tmpList.get(0) + "'}, port2=" + tmpList.get(2) + ", delay = '"+delayStr+"ms', loss = "+lossStr+")\n");
                }
                else{
                    fileWriter.write("        self.addLink(leo" + i + ",s1,intfName1='" + tmpList.get(1) + "',params1={'ip' : '" + tmpList.get(0) + "'}, port2=" + tmpList.get(2) + ", delay = '"+delayStr+"ms')\n");
                }
            } else {
                fileWriter.write("        self.addLink(leo" + i + ",s1,intfName1='" + tmpList.get(1) + "',params1={'ip' : '" + tmpList.get(0) + "'}, port2=" + tmpList.get(2) + ")\n");
            }
        }
        //添加地面站的连接
        fileWriter.write("\n\n\n");

        String[][] stationInfo = FileToMatrix.fileToString("station.txt");
        int port_base = se_if_map.size();
        for(int i=0; i<Integer.valueOf(stationInfo[0][0]);++i)
        {
            String ip = "10."+stationInfo[i+1][0]+"."+stationInfo[i+1][1]+"."+stationInfo[i+1][2]+"/24";
            fileWriter.write("        station"+i+" = self.addNode('station"+i+"', cls = LinuxRouter, ip = '"+ip+"')\n");
            fileWriter.write("        self.addLink(station"+i+", s1, intfName1 = 'station"+i+"-eth0', params1 = {'ip' : '"+ip+"'}, port2="+(port_base+i)+")\n");
        }

        fileWriter.write("\n");
        port_base += Integer.valueOf(stationInfo[0][0]);

        for(int i=0; i<Integer.valueOf(stationInfo[0][0]);++i)
        {
            fileWriter.write("        self.addLink(station"+i+", s1, intfName1 = 'station"+i+"-eth1', params1 = {'ip' : '114.114.114."+ (i+1) +"/24'}, port2="+(port_base+i)+")\n");
        }
        fileWriter.write("\n");
        port_base += Integer.valueOf(stationInfo[0][0]);
        fileWriter.write("        stationNAT = self.addNode('stationNAT', cls = LinuxRouter, ip = '114.114.114.114/24')\n");
        fileWriter.write("        self.addLink(stationNAT, s1, intfName1 = 'stationNAT-eth0', params1 = {'ip' : '114.114.114.114/24'}, port2 = "+port_base+")\n");

        fileWriter.write("\n\n\n");
        fileWriter.write("class tc_info(object):\n");
        fileWriter.write("    num1=0\n");
        fileWriter.write("    num2=0\n");
        fileWriter.write("    ethname1=''\n");
        fileWriter.write("    ethname2=''\n");
        fileWriter.write("    linkinfo=[]\n");
        fileWriter.write("    def __init__(self,num1,num2,ethname1,ethname2,linkinfo):\n");
        fileWriter.write("        self.num1=num1\n");
        fileWriter.write("        self.num2=num2\n");
        fileWriter.write("        self.ethname1=ethname1\n");
        fileWriter.write("        self.ethname2=ethname2\n");
        fileWriter.write("        self.linkinfo=linkinfo\n");
        fileWriter.write("\n\n\n");

        fileWriter.write("class TestMininet(Mininet):\n");
        fileWriter.write("    def __init__(self,controller,topo):\n");
        fileWriter.write("        Mininet.__init__(self,controller=controller, topo=topo, link=TCLink)\n");
        for(int i=0;i<ethlist.length;++i)
        {
            fileWriter.write("        self.leo"+i+"=self.getNodeByName('leo"+i+"')\n");
        }
        fileWriter.write("\n\n");
        //写入星地接口相关
        fileWriter.write("        self.n="+this.leo_per_orbit+"\n");
        fileWriter.write("        self.P="+this.orbit_all+"\n");
        fileWriter.write("        self.k="+k+"\n");
        fileWriter.write("        self.phase=0\n");
        fileWriter.write("        self.phaseAll="+phaseAll+"\n");
        fileWriter.write("\n");
        //写入四个信息列表
        fileWriter.write("        self.leodic={}\n");
        for(int i=0;i<ethlist.length;++i)
        {
            fileWriter.write("        self.leodic["+i+"]=self.leo"+i+"\n");
        }
        fileWriter.write("\n");
        fileWriter.write("        self.se_addr={}\n");
        for(int i=0;i<ethlist.length;++i)
        {
            List<String> tmpList=se_if_map.get(i);
            fileWriter.write("        self.se_addr["+i+"]=\'"+tmpList.get(0)+"\'\n");
        }
        fileWriter.write("\n");
        fileWriter.write("        self.se_ethname={}\n");
        for(int i=0;i<ethlist.length;++i)
        {
            List<String> tmpList=se_if_map.get(i);
            fileWriter.write("        self.se_ethname["+i+"]=\'"+tmpList.get(1)+"\'\n");
        }
        fileWriter.write("\n");
        fileWriter.write("        self.orbit_k={}\n");
        for(int i=0;i<this.orbit_all;++i)
        {
            fileWriter.write("        self.orbit_k["+i+"]="+(i%k)+"\n");
        }
        fileWriter.write("\n\n");
        //写入tc_info信息
        fileWriter.write("        self.tc_info_array={}\n");
        for(int i=0;i<tc_info_list.size();++i)
        {
            fileWriter.write("        self.tc_info_array["+i+"]=tc_info("+tc_info_list.get(i).num1+","+tc_info_list.get(i).num2+",'"+tc_info_list.get(i).ethname1+"','"+tc_info_list.get(i).ethname2+"',["+tc_info_list.get(i).linkinfo+"])\n");
        }
        fileWriter.write("\n\n\n");
        //写入星地接口转换相关函数
        fileWriter.write("    def ipaddr_sub_ip3(self,ipaddr):\n");
        fileWriter.write("        ipaddr_arr=ipaddr.split('.')\n");
        fileWriter.write("        tmp= int(ipaddr_arr[2])-1\n");
        fileWriter.write("        if tmp<0:\n");
        fileWriter.write("            tmp+=self.n\n");
        fileWriter.write("        return ipaddr_arr[0]+'.'+ipaddr_arr[1]+'.'+str(tmp)+'.'+ipaddr_arr[3]\n\n");
        fileWriter.write("    def ipaddr_add_ip2(self,ipaddr):\n");
        fileWriter.write("        ipaddr_arr=ipaddr.split('.')\n");
        fileWriter.write("        tmp= int(ipaddr_arr[1])+1\n");
        fileWriter.write("        if tmp>=self.P:\n");
        fileWriter.write("            tmp-=self.P\n");
        fileWriter.write("        return ipaddr_arr[0]+'.'+ str(tmp) + '.' + ipaddr_arr[2]+'.'+ipaddr_arr[3]\n\n");
        fileWriter.write("    def add_y(self):\n");
        fileWriter.write("        for i in range(0,self.P):\n");
        fileWriter.write("            self.orbit_k[i]+=1\n");
        fileWriter.write("            if self.orbit_k[i] >= self.k:\n");
        fileWriter.write("                self.orbit_k[i]=0\n");
        fileWriter.write("                for j in range(0,self.n):\n");
        fileWriter.write("                    self.se_addr[i*self.n+j]=self.ipaddr_sub_ip3(self.se_addr[i*self.n+j])\n");
        fileWriter.write("                    cmd_y='ifconfig ' + self.se_ethname[i*self.n+j]+' '+self.se_addr[i*self.n+j]\n");
        // 在ospfd中进行ifconfig,此处不再需要调整地址
//        fileWriter.write("                    self.leodic[i*self.n+j].cmd(cmd_y)\n");
        fileWriter.write("                    print(cmd_y)\n");
        fileWriter.write("            for j in range(0,self.n):\n");
        fileWriter.write("                cmd_y = 'vtysh -f "+running_dir+"cmd/se_add_y.conf -w "+apiDir+"/vtyzebra'+ str(i*self.n+j) +'.api -q "+apiDir+"/vtyospfd'+ str(i*self.n+j)  +'.api -r'\n");
        fileWriter.write("                self.leodic[i*self.n+j].cmd(cmd_y)\n");
        fileWriter.write("                print(cmd_y)\n\n\n");
        fileWriter.write("    def add_x(self):\n");
        fileWriter.write("        for i in range(0,self.P):\n");
        fileWriter.write("            for j in range(0,self.n):\n");
        fileWriter.write("                leo_num=i*self.n+j\n");
        fileWriter.write("                self.se_addr[leo_num]=self.ipaddr_add_ip2(self.se_addr[leo_num])\n");
        fileWriter.write("                cmd_x='ifconfig '+self.se_ethname[leo_num]+' '+self.se_addr[leo_num]\n");
        // 在ospfd中进行ifconfig,此处不再需要调整地址
//        fileWriter.write("                self.leodic[leo_num].cmd(cmd_x)\n");
        fileWriter.write("                print(cmd_x)\n");
        fileWriter.write("                cmd_x = 'vtysh -f "+running_dir+"cmd/se_add_x.conf -w "+apiDir+"/vtyzebra'+ str(leo_num) +'.api -q "+apiDir+"/vtyospfd'+ str(leo_num)  +'.api -r'\n");
        fileWriter.write("                self.leodic[leo_num].cmd(cmd_x)\n");
        fileWriter.write("                print(cmd_x)\n\n\n");

        //写入6个操作函数
        fileWriter.write("    def oa(self):\n");
        for(int i=0;i<ethlist.length;++i)
        {
            fileWriter.write("        self.leo"+i+".cmd(\"vtysh -f "+running_dir+"inter_oa/inter_oa"+i+".conf -w "+apiDir+"/vtyzebra"+i+".api -q "+apiDir+"/vtyospfd"+i+".api -r\")\n");
        }
        fileWriter.write("\n\n");
        fileWriter.write("    def load(self):\n");
        for(int i=0;i<ethlist.length;++i)
        {
            fileWriter.write("        self.leo"+i+".cmd(\"vtysh -f "+running_dir+"cmd/loadlsdb.conf -w "+apiDir+"/vtyzebra"+i+".api -q "+apiDir+"/vtyospfd"+i+".api -r\")\n");
        }
        fileWriter.write("\n\n");
        fileWriter.write("    def add_phase(self):\n");
        fileWriter.write("        last_phase=self.phase\n");
        fileWriter.write("        self.phase+=1\n");

        fileWriter.write("        if self.phase>=self.phaseAll:\n");
        fileWriter.write("            self.phase=0\n");
        fileWriter.write("        print(str(self.phase)+\",\"+str(last_phase))\n");
        if(Config.interStarTC == 1)
        {
            fileWriter.write("        for i in range(0,len(self.tc_info_array)):\n");
            fileWriter.write("            if self.tc_info_array[i].linkinfo[self.phase]==0 and self.tc_info_array[i].linkinfo[last_phase]==1:\n");
            fileWriter.write("                print(str(self.tc_info_array[i].num1)+\":\"+\"tc qdisc del dev \"+str(self.tc_info_array[i].ethname1)+\" root netem loss 100%\")\n");
            fileWriter.write("                print(str(self.tc_info_array[i].num2)+\":\"+\"tc qdisc del dev \"+str(self.tc_info_array[i].ethname2)+\" root netem loss 100%\")\n");
            fileWriter.write("                self.leodic[self.tc_info_array[i].num1].cmd(\"tc qdisc del dev \"+self.tc_info_array[i].ethname1+\" root netem loss 100%\")\n");
            fileWriter.write("                self.leodic[self.tc_info_array[i].num2].cmd(\"tc qdisc del dev \"+self.tc_info_array[i].ethname2+\" root netem loss 100%\")\n\n");
        }


        for(int i=0;i<ethlist.length;++i)
        {
            fileWriter.write("        self.leo"+i+".cmd(\"vtysh -f "+running_dir+"cmd/add_phase.conf -w "+apiDir+"/vtyzebra"+i+".api -q "+apiDir+"/vtyospfd"+i+".api -r\")\n");
        }
        fileWriter.write("        time.sleep(10)\n");
        if(Config.interStarTC == 1) {
            fileWriter.write("        for i in range(0,len(self.tc_info_array)):\n");
            fileWriter.write("            if self.tc_info_array[i].linkinfo[self.phase]==1 and self.tc_info_array[i].linkinfo[last_phase]==0:\n");
            fileWriter.write("                print(str(self.tc_info_array[i].num1)+\":\"+\"tc qdisc add dev \"+str(self.tc_info_array[i].ethname1)+\" root netem loss 100%\")\n");
            fileWriter.write("                print(str(self.tc_info_array[i].num2)+\":\"+\"tc qdisc add dev \"+str(self.tc_info_array[i].ethname2)+\" root netem loss 100%\")\n");
            fileWriter.write("                self.leodic[self.tc_info_array[i].num1].cmd(\"tc qdisc add dev \"+self.tc_info_array[i].ethname1+\" root netem loss 100%\")\n");
            fileWriter.write("                self.leodic[self.tc_info_array[i].num2].cmd(\"tc qdisc add dev \"+self.tc_info_array[i].ethname2+\" root netem loss 100%\")\n");
        }
        fileWriter.write("\n\n");
        fileWriter.write("    def begin_running(self):\n");
        for(int i=0;i<ethlist.length;++i)
        {
            fileWriter.write("        self.leo"+i+".cmd(\"vtysh -f "+running_dir+"cmd/begin_running.conf -w "+apiDir+"/vtyzebra"+i+".api -q "+apiDir+"/vtyospfd"+i+".api -r\")\n");
        }
        fileWriter.write("        time.sleep(10)\n");
        if(Config.interStarTC == 1) {
            fileWriter.write("        for i in range(0,len(self.tc_info_array)):\n");
            fileWriter.write("            if self.tc_info_array[i].linkinfo[0]==1:\n");
            fileWriter.write("                print(str(self.tc_info_array[i].num1)+\":\"+\"tc qdisc add dev \"+str(self.tc_info_array[i].ethname1)+\" root netem loss 100%\")\n");
            fileWriter.write("                print(str(self.tc_info_array[i].num2)+\":\"+\"tc qdisc add dev \"+str(self.tc_info_array[i].ethname2)+\" root netem loss 100%\")\n");
            fileWriter.write("                self.leodic[self.tc_info_array[i].num1].cmd(\"tc qdisc add dev \"+self.tc_info_array[i].ethname1+\" root netem loss 100%\")\n");
            fileWriter.write("                self.leodic[self.tc_info_array[i].num2].cmd(\"tc qdisc add dev \"+self.tc_info_array[i].ethname2+\" root netem loss 100%\")\n");
            fileWriter.write("\n\n");
        }

        fileWriter.write("def run():\n");
        fileWriter.write("    topo = NetworkTopo()\n");
        fileWriter.write("    net = TestMininet(controller=RemoteController,topo=topo)\n");
        fileWriter.write("    #c = net.addController('c0',controller=RemoteController,port=6633)\n");
        fileWriter.write("    net.start()\n");
        fileWriter.write("    info( '*** Routing Table on Router:\\n' )\n");
        for(int i=0;i<ethlist.length;++i){
            fileWriter.write("    "+ethlist[i][0]+"=net.getNodeByName('"+ ethlist[i][0]+"')\n");
        }
        for(int i=0; i<Integer.valueOf(stationInfo[0][0]);++i)
        {
            fileWriter.write("    station"+i+"=net.getNodeByName('station"+i+"')\n");
        }
        for(int i=0;i<ethlist.length;++i){
            fileWriter.write("    "+ethlist[i][0]+".cmd('zebra -f "+running_dir+"ospf_conf/"+ethlist[i][0]+"zebra.conf -d -z "+apiDir+"/"+ethlist[i][0]+"zebra.api -i "+apiDir+"/"+ethlist[i][0]+"zebra.interface -w "+apiDir+"/vtyzebra"+i+".api')\n");
        }
        fileWriter.write("    time.sleep(2)\n");
        for(int i=0;i<ethlist.length;++i){
            fileWriter.write("    "+ethlist[i][0]+".cmd('ospfd -f "+running_dir+"ospf_conf/"+ethlist[i][0]+"ospfd.conf -d -z "+apiDir+"/"+ethlist[i][0]+"zebra.api -i "+apiDir+"/"+ethlist[i][0]+"ospfd.interface -q "+apiDir+"/vtyospfd"+i+".api')\n");
        }
        fileWriter.write("\n");
        for(int i=0; i<Integer.valueOf(stationInfo[0][0]);++i)
        {
            String ip = "10."+stationInfo[i+1][0]+"."+stationInfo[i+1][1]+".1";
            fileWriter.write("    station" + i + ".cmd('ip route add 172.16.0.0/12 via " + ip + "')\n");
            fileWriter.write("    station" + i + ".cmd('ip route add 10.0.0.0/8 via " + ip + "')\n");
            fileWriter.write("    station" + i + ".cmd('iptables -t nat -I POSTROUTING -o station" + i + "-eth1 -s 172.16.0.0/12 -j SNAT --to-source 114.114.114."+(i+1)+"')\n");
            fileWriter.write("    station" + i + ".cmd('iptables -t nat -I POSTROUTING -o station" + i + "-eth1 -s 10.0.0.0/8 -j SNAT --to-source 114.114.114."+(i+1)+"')\n");
        }
        fileWriter.write("    os.system(\"ovs-ofctl add-flow s1 actions=NORMAL\")");
        fileWriter.write("\n");
        fileWriter.write("    leo0.cmd('wireshark -i leo0-eth0 -k &')\n");
        fileWriter.write("    os.system(\"ovs-ofctl add-flow s1 actions=NORMAL\")\n");
        fileWriter.write("    CLI( net )\n");
        fileWriter.write("    net.stop()\n");
        fileWriter.write("    os.system(\"killall -9 ospfd zebra\")\n");
        fileWriter.write("    os.system(\"cd "+apiDir+" && rm -f *api*\")\n");
        fileWriter.write("    os.system(\"cd "+apiDir+" && rm -f *interface*\")\n");
        fileWriter.write("\n");
        fileWriter.write("if __name__ == '__main__':\n");
        fileWriter.write("    setLogLevel( 'info' )\n");
        fileWriter.write("    run()\n");
        fileWriter.close();

    }

}
