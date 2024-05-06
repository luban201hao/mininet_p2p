package com.mininet.utils;
import com.sun.xml.internal.fastinfoset.tools.FI_DOM_Or_XML_DOM_SAX_SAXEvent;

import javax.swing.*;
import java.awt.*;

class Mypanel extends JPanel {
    private int n;
    private int P;
    private String ethList;
    private int Xm;
    private int Ym;
    private String[][] eths;
    private String[][] upDown;
    private int phase;

    public Mypanel(int _n,int _p,String _ethList,int Xm,int Ym)
    {
        super();
        this.n=_n;
        this.P=_p;
        this.Xm=Xm;
        this.Ym=Ym;
        this.ethList=_ethList;
        try {
            this.eths = FileToMatrix.fileToString(this.ethList);
            this.upDown= FileToMatrix.fileToString("AS_up_down.txt");
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        this.phase=0;
    }
    public void addPhase()
    {
        this.phase++;
    }
    public void MyPaint(Graphics g)
    {

    }

    @Override
    public void paint(Graphics g) {
        System.out.println(n+","+P+","+ethList);
        Graphics2D g2d = (Graphics2D) g;
//        g2d.setColor(new Color(0xffd633)); // 设置填充颜色
//        g2d.setStroke(new BasicStroke(20)); // 设置边框宽度
//        g2d.fillOval(getWidth() - 600, getHeight() - 600, 450, 450); // 填充圆形
//        g2d.setColor(Color.BLACK); // 设置边框颜色
//        g2d.drawOval(getWidth() - 600, getHeight() - 600, 450, 450); // 绘制边框
//
//        g2d.drawOval(getWidth() - 350, getHeight() - 500, 100, 125); // 绘制边框
//        g2d.drawOval(getWidth() - 500, getHeight() - 500, 100, 125); // 绘制边框
//        g2d.setColor(Color.WHITE);
//        g2d.fillOval(getWidth() - 335, getHeight() - 490, 70, 95); // 填充圆形
//        g2d.fillOval(getWidth() - 485, getHeight() - 490, 70, 95); // 填充圆形
//
//        g2d.setColor(Color.RED);
//        g2d.fillOval(getWidth() - 550, getHeight() - 350, 100, 100); // 填充圆形
//        g2d.fillOval(getWidth() - 300, getHeight() - 350, 100, 100); // 填充圆形
//
//        g2d.setColor(Color.GRAY); // 设置线条颜色为灰色
//        g2d.drawLine(150, 350, 400, 110); // 画一条从左下角到右上角的线条
//        g2d.drawLine(650, 350, 400, 110); // 画一条从左下角到右上角的线条

//        g2d.setColor(Color.BLACK); // 设置边框颜色
        g2d.clearRect(0,0,this.Xm,this.Ym);
        Font Song16=new Font("宋体", Font.PLAIN, 10);
        g2d.setFont(Song16);
        System.out.println("phase="+this.phase);
        g2d.drawString("phase="+this.phase,10,10);
//        g2d.drawString("this is a string",100,100);
        int baseX=Xm/(P+1);
        int baseY=Ym/(n+1);
        int dx=baseX;
        int dy=baseY;
        g2d.setColor(Color.GRAY);
        for(int i=0;i<P;++i)
        {
            for(int j=0;j<=n-2;++j)
            {
                int xPos=baseX+i*dx;
                int yPos=baseY+j*dy;
                g2d.drawLine(xPos+5,yPos+5,xPos+5,yPos+dy+5);
            }
        }
        for(int i=0;i<=P-2;++i)
        {
            for(int j=0;j<=n-1;++j)
            {
                int xPos=baseX+i*dx;
                int yPos=baseY+j*dy;


                int leoNum=i*n+j;
                g2d.setColor(Color.BLACK);
                for(int x=1;x<upDown.length;x+=2)
                {
                    int a=Integer.valueOf(upDown[x][0]);
                    int b=Integer.valueOf(upDown[x][1]);
                    int add=0;
                    if(a==leoNum && b==leoNum+n) {
                        String info = "";
                        for (int y = 0; y < upDown[x + 1].length; ++y) {
                            info += upDown[x + 1][y] + ",";
                            if (y % 10 == 9) {
                                g2d.drawString(info, xPos + 20, yPos - 20 + 10 * add);
                                info = "";
                                add++;
                            }
                        }
                        if (!info.equals("")) {
                            g2d.drawString(info, xPos + 20, yPos - 20 + 10 * add);
                        }

                        if (upDown[x + 1][phase].equals("1")) {
                            g2d.setColor(Color.RED);
                        } else {
                            g2d.setColor(Color.GRAY);
                        }
                        break;
                    }
                }
                g2d.drawLine(xPos+5,yPos+5,xPos+dx+5,yPos+5);
            }
        }

        g2d.setColor(Color.BLACK);
        for(int i=0;i<P;++i)
        {
            for(int j=0;j<n;++j)
            {
                String info="";
                int leoNum=i*n+j;
                int k=1;
                int xPos=baseX+i*dx;
                int yPos=baseY+j*dy;

                int add=0;
                while(k<eths[leoNum].length)
                {
                    if(eths[leoNum][k]==null)
                        break;
                    info=eths[leoNum][k]+":"+eths[leoNum][k+1];
                    k+=3;
                    g2d.drawString(info,xPos,yPos+20+10*add);
                    add++;
                }

                g2d.fillOval(xPos,yPos,10,10);
                g2d.drawString("leo"+leoNum,xPos-10,yPos-10);


            }
        }
    }
}