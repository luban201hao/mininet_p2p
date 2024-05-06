package com.mininet.JavaTest;

import java.awt.Color;
import java.awt.Container;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class Demo extends JFrame {
    public Demo() {
        setBounds(100, 100, 450, 200);// 设置窗体坐标和大小
        setDefaultCloseOperation(EXIT_ON_CLOSE);// 设置窗体关闭规则，关闭窗口时关闭程序
        Container c = getContentPane();
        c.setLayout(new GridLayout(3, 2, 5, 5));

        JButton btn[] = new JButton[6];
        for (int i = 0; i < btn.length; i++) {
            btn[i] = new JButton();
            c.add(btn[i]);
        }
        btn[0].setText("不可用");// 设置文本
        btn[0].setEnabled(false);// 设置组件不可用

        btn[1].setText("有背景色");
        btn[1].setBackground(Color.yellow);// 设置背景色

        btn[2].setText("无边框");
        btn[2].setBorder(BorderFactory.createLineBorder(Color.red));// 设置线边框

        btn[3].setText("有边框");
        btn[3].setBorderPainted(false);// 不显示边框

        Icon cion = new ImageIcon("src/imageButt.png");
        btn[4].setIcon(cion);// 给按钮设置图片
        btn[4].setToolTipText("图片按钮");// 鼠标悬停提示

        btn[5].setText("可点击");
        btn[5].addActionListener(new ActionListener() {//添加事件监听
            @Override
            public void actionPerformed(ActionEvent e) {//监听触发事件
                JOptionPane.showMessageDialog(Demo.this, "点击按钮");//弹出小对话框
            }
        });

        setVisible(true);
    }

    public static void main(String[] args) {
        new Demo();
    }
}
