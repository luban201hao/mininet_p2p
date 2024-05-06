package com.mininet.JavaTest;


public class Button {
    public Rect rect;
    public String name="";
    public String groupName="";//分组名字，选中的时候同一个小组只有一个被选中
    public boolean bXuanzhong=false;
    public boolean bXuanTing=false; //记录按钮是否处于悬停状态

    public Button() {
    }

    public Button(Rect rect, String name) {
        this.rect = rect;
        this.name = name;
    }

    //    判断鼠标是否点击在按钮上
    public boolean isInButton(int x, int y){
        if(x>rect.x&&x<(rect.x+rect.width)&&y>rect.y&&y<(rect.y+rect.height)){
            return true;
        }
        return false;
    }
}