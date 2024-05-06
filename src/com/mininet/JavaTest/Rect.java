package com.mininet.JavaTest;

import java.awt.*;

public class Rect {
    int x=0;
    int y=0;
    int width=0;
    int height=0;

    public Rect() {
    }

    public Rect(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }
    public Rect(int x1,int y1,int x2,int y2,boolean bool){
        //   1.找到左上角 2.取宽高的绝对值
        int min_x;
        int min_y;
        int max_x;
        int max_y;
        if(x1<x2){
            min_x=x1;
            max_x=x2;
        }else{
            min_x=x2;
            max_x=x1;
        }
        if(y1<y2){
            min_y=y1;
            max_y=y2;
        }else{
            min_y=y2;
            max_y=y1;
        }
        this.x = min_x;
        this.y = min_y;
        this.width = max_x-min_x;
        this.height = max_y-min_y;
    }
    public int getX() {
        return x;
    }
    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }
    public void setY(int y) {
        this.y = y;
    }
    public int getWidth() {
        return width;
    }
    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }
    public void setHeight(int height) {
        this.height = height;
    }
}