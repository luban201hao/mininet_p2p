package com.mininet.JavaTest;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Paint007 extends JFrame implements MouseListener , MouseMotionListener, ComponentListener {

    //    行数(高）
    int height=8;
    //    列数（宽）
    int width=12;
    //    格子的大小
    int size=100;
    //    标题栏的高度
    int title=50;


    //    0表示矩形 1表示圆形 2表示直线 3表示铅笔 4表示橡皮擦
    int zhuangtai=0;


    //    记录最后一个鼠标按下的位置
    int x_last=0;
    int y_last=0;

    //    记录鼠标最后移动的位置
    int x_move=0;
    int y_move=0;

    //    定义图形颜色
    Color color=Color.black;

    //这是创建了一个按钮数组，Button[5+4+1] 5表示前面几个形状的按钮 4表示颜色按钮 1表示清空按钮
    int begin_xingzhuang=0;
    int sum_xingzhuang=5;
    int begin_yanse=5;
    int sum_yanse=4;
    int begin_qita=9;
    int sum_qita=1;
    Button[] button=new Button[sum_xingzhuang+sum_yanse+sum_qita];



    //    设置图片1
    private Image image=null;
    Graphics gf=null;
    //    设置图片2
    private Image imageBack=null;
    Graphics gfBack=null;


    public void Tian(){
        String [] a={"矩形","圆形","直线","铅笔","橡皮","黑色","红色","绿色","蓝色","清空"};
        for (int i = begin_xingzhuang; i < begin_xingzhuang+sum_xingzhuang; i++) {
            button[i]=new Button(new Rect(110*i,title,100,50),a[i]);
            button[i].groupName="形状";

        }
        for (int i = begin_yanse; i < begin_yanse+sum_yanse; i++) {
            button[i]=new Button(new Rect(110*i,title,100,50),a[i]);
            button[i].groupName="颜色";
        }
        for (int i = begin_qita; i < begin_qita+sum_qita; i++) {
            button[i]=new Button(new Rect(110*i,title,100,50),a[i]);
        }

        //设置窗口的宽高
        this.setSize(width*size ,height*size+title);
//        设置标题
        this.setTitle("画板");
        //设置窗口能看见
        this.setVisible(true);
//        设置窗口顶点坐标的位置
        this.setLocation(100,100);
//         设置鼠标监听事件
        this.addMouseListener(this);
//        加强版的鼠标监听事件（也就是监听鼠标拖拽和鼠标移动事件）
        this.addMouseMotionListener(this);
//        监听窗口大小改变
        this.addComponentListener(this);

    }

    @Override
    public void paint(Graphics g){
        //初始化临时图片//解决闪烁问题
        if(image==null){
            image=this.createImage(2000,2000);
        }
        if(this.gf ==null){
            this.gf =image.getGraphics();
        }

        if(imageBack==null){
            imageBack=this.createImage(2000,2000);
        }
        if(this.gfBack ==null){
            this.gfBack =imageBack.getGraphics();
        }


//        绘制按钮
        for (int i = 0; i < button.length; i++) {
//            绘制按钮选中颜色
            if (button[i].bXuanzhong==true){
                gf.setColor(Color.pink);
                gf.fillRect(button[i].rect.x,button[i].rect.y,button[i].rect.width,button[i].rect.height);

//                绘制按钮为选中时的颜色
            }else {
                gf.setColor(Color.gray);
                gf.fillRect(button[i].rect.x,button[i].rect.y,button[i].rect.width,button[i].rect.height);

            }
//           当按钮是悬停状态时，字体颜色设置为白色
            if(button[i].bXuanTing==true){
                gf.setColor(Color.white);

                //           当按钮是非悬停状态时，字体颜色设置为黑色
            }else{
                gf.setColor(Color.black);
            }
            gf.setFont(new Font("华文新魏", 10, 35)); //设置字体
            gf.drawString(button[i].name,button[i].rect.x+(button[i].rect.width-2*35)/2,button[i].rect.y+(button[i].rect.height+35/2)/2);

        }

        g.drawImage(image,0,0,getWidth(),getHeight(),0,0,getWidth(),getHeight(),null);
    }

    @Override
    public void mouseClicked(MouseEvent e) {
    }
    //    鼠标按压事件
    @Override
    public void mousePressed(MouseEvent e) {
//        处理鼠标左键
        if(e.getButton()==e.BUTTON1) {
//            鼠标点击的像素坐标
//            鼠标点击的x坐标位置
            x_last = e.getX();
//            鼠标点击的y坐标位置
            y_last = e.getY();

//            被点击的按钮， 空表示没有按钮被点击， 如果点击了某个按钮， 那么name就记录按钮的名字
            String name="";

//            判断鼠标左键按压的地方在不在按钮内部
            for (int i = 0; i < button.length; i++) {
                if(button[i].isInButton(x_last,y_last)==true){
//                    记录鼠标左键按压按钮的名字
                    name=button[i].name;
                    break;
                }
            }

            System.out.println(name);

//            处理各种按钮的按压事件
            if ("矩形".equals(name)) {
                zhuangtai=0;
            }else if ("圆形".equals(name)) {
                zhuangtai=1;
            }else if ("直线".equals(name)) {
                zhuangtai=2;
            }else if ("铅笔".equals(name)) {
                zhuangtai=3;
            }else if ("橡皮".equals(name)) {
                zhuangtai=4;
            }else if ("黑色".equals(name)){
                color=Color.black;
            }else if ("红色".equals(name)){
                color=Color.red;
            }else if ("绿色".equals(name)){
                color=Color.green;
            }else if ("蓝色".equals(name)){
                color=Color.blue;
            }else if("清空".equals(name)){
                gfBack.setColor(new Color(238,238,238));
                gfBack.fillRect(0,0,2000,2000);
                gf.drawImage(imageBack,0,0,null);
                repaint();
            }


            //处理按钮被选中的逻辑
            if("".equals(name)==false){

//                记录选中按钮的分组名
                String groupname="";

//                遍历所有的按钮
                for (int i = 0; i < button.length; i++) {
//                    记录被选中按钮的分组名
                    if (button[i].name.equals(name)==true){
                        groupname=button[i].groupName;
                        break;
                    }
                }

//                有分组的才会被选中
                if(groupname.equals("")==false){
                    //                设置选中状态
                    for (int i = 0; i < button.length; i++) {

//                    选中该按钮
                        if (button[i].name.equals(name)==true){
                            button[i].bXuanzhong=true;

//                        同分组的其他按钮取消选中
                        }else {
                            if(groupname.equals(button[i].groupName)==true){
                                button[i].bXuanzhong=false;
                            }
                        }
                    }

                    repaint();
                }
            }


//          重置鼠标移动的位置，—1表示无效位置
            x_move=-1;
            y_move=-1;
        }else if(e.getButton()==e.BUTTON3){
            //            鼠标点击的像素坐标
//            鼠标点击的x坐标位置
            x_last = e.getX();
//            鼠标点击的y坐标位置
            y_last = e.getY();
        }
    }
    //    鼠标弹起事件
    @Override
    public void mouseReleased(MouseEvent e) {
        //        处理鼠标左键
        if(e.getButton()==e.BUTTON1) {
//            鼠标点击的像素坐标
//            鼠标点击的x坐标位置
            int x = e.getX();
//            鼠标点击的y坐标位置
            int y = e.getY();


//    0表示矩形 1表示圆形 2表示直线 3表示铅笔 4表示橡皮擦
            //    0表示矩形
            if(zhuangtai==0){

                Rect rect = new Rect(x_last,y_last,x,y,true);
//                先绘制到背景图片
                gfBack.setColor(color);
                gfBack.drawRect(rect.getX(),rect.getY(),rect.getWidth(),rect.getHeight());
//                将背景图片拷贝到临时图片中
                gf.drawImage(imageBack,0,0,null);
                repaint();

//                1表示圆形
            }else if(zhuangtai==1){
                //            1.找到左上角 2.取宽高的绝对值
                Rect rect = new Rect(x_last,y_last,x,y,true);
                gfBack.setColor(color);
                gfBack.drawOval(rect.getX(),rect.getY(),rect.getWidth(),rect.getHeight());
                //                将背景图片拷贝到临时图片中
                gf.drawImage(imageBack,0,0,null);
                repaint();

//                2表示直线
            }else if(zhuangtai==2){
                gfBack.setColor(color);
                gfBack.drawLine(x_last,y_last,x,y);
                //                将背景图片拷贝到临时图片中
                gf.drawImage(imageBack,0,0,null);
                repaint();
//                3表示铅笔
            }else if(zhuangtai==3){
//                4表示橡皮擦
            }else if(zhuangtai==4){
                gf.drawImage(imageBack,0,0,null);
                repaint();
            }else if(zhuangtai==5){
            }

        }else if(e.getButton()==e.BUTTON3){
            //            鼠标点击的像素坐标
//            鼠标点击的x坐标位置
            int x = e.getX();
//            鼠标点击的y坐标位置
            int y = e.getY();
        }
    }

    //    鼠标拖拽的移动监听事件
//    左键被按下是鼠标的移动
    @Override
    public void mouseDragged(MouseEvent e) {
        System.out.println("鼠标移动");
        //            鼠标点击的x坐标位置
        int x = e.getX();
//            鼠标点击的y坐标位置
        int y = e.getY();
//        铅笔
        if(zhuangtai==3){
            //            鼠标点击的像素坐标
            if(x_move!=-1&&y_move!=-1){
                gfBack.setColor(color);
                gfBack.drawLine(x_move,y_move,x,y);

                //把背景图片复制到临时图片上
                gf.drawImage(imageBack,0,0,null);
                repaint();
            }
//            橡皮
        }else if(zhuangtai==4){

            int size_rubber=50;
            // 画到背景图片上
            gfBack.setColor(new Color(238,238,238));
            gfBack.fillOval(x-size_rubber/2,y-size_rubber/2,size_rubber,size_rubber);

            //把背景图片复制到临时图片上
            gf.drawImage(imageBack,0,0,null);
            gfBack.setColor(Color.black);
            gf.drawOval(x-size_rubber/2,y-size_rubber/2,size_rubber,size_rubber);

            repaint();
//            绘制矩形过程中
        }else if(zhuangtai==0){
            Rect rect = new Rect(x_last,y_last,x,y,true);

            //把背景图片复制到临时图片上，擦除临时图片上的内容
            gf.drawImage(imageBack,0,0,null);

//            在临时图片上绘制矩形
            gf.setColor(color);
            gf.drawRect(rect.getX(),rect.getY(),rect.getWidth(),rect.getHeight());

            repaint();
//            绘制圆形过程中
        }else if(zhuangtai==1){
            Rect rect = new Rect(x_last,y_last,x,y,true);

            //把背景图片复制到临时图片上，擦除临时图片上的内容
            gf.drawImage(imageBack,0,0,null);
//            在临时图片上绘制圆形
            gf.setColor(color);
            gf.drawOval(rect.getX(),rect.getY(),rect.getWidth(),rect.getHeight());
            repaint();
//            绘制直线过程中
        }else if (zhuangtai==2){
            //把背景图片复制到临时图片上，擦除临时图片上的内容
            gf.drawImage(imageBack,0,0,null);

            gf.setColor(color);
            gf.drawLine(x_last,y_last,x,y);
            repaint();
        }
        x_move=x;
        y_move=y;
    }
    //    鼠标移动时的监听事件
    @Override
    public void mouseMoved(MouseEvent e){
        //            鼠标点击的x坐标位置
        int x = e.getX();
//            鼠标点击的y坐标位置
        int y = e.getY();

        for (int i = 0; i < button.length; i++) {
            if(button[i].isInButton(x,y)==true){
                button[i].bXuanTing=true;
            }else{
                button[i].bXuanTing=false;
            }
        }
        repaint();
    }
    //      鼠标进入窗口的处理函数事件
    @Override
    public void mouseEntered(MouseEvent e) {
    }
    @Override
    public void mouseExited(MouseEvent e) {
    }
    //    窗口大小发生改变的监听事件
    @Override
    public void componentResized(ComponentEvent e){
    }
    @Override
    public void componentMoved(ComponentEvent e) {
    }
    @Override
    public void componentShown(ComponentEvent e) {
    }
    @Override
    public void componentHidden(ComponentEvent e) {
    }
    public static void main(String[] args) {
        Paint007 paint = new Paint007();
        paint.Tian();
    }
}
