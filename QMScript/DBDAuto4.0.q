[General]
SyntaxVersion=2
BeginHotkey=120
BeginHotkeyMod=0
PauseHotkey=80
PauseHotkeyMod=1
StopHotkey=121
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=06b1f4a4-179e-4508-a5a5-47e6cf33bf0f
Description=DBDautoscript
Enable=1
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]
此脚本开源免费
项目地址：https://github.com/maskrs/DBD_AFK_TOOL

[Script]
/////////////////////////////////////////////
//                                         //
//此脚本开源免费，项目地址：                 //
//https://github.com/maskrs/DBD_AFK_TOOL   //
//                                         //
/////////////////////////////////////////////


//Goto 载入//调试
//Call CheckTime()//检测当前时间.1
Global i,jni,dxi,ejnX,ejnY,yjnX,yjnY,inX,inY,zy,xdi//定义需要的变量
i = 0
jni = 0
dxi = 0
xdi = 0
//Rem 调试
zy = MsgBox("是否使用人类阵营，选择‘否’则为屠夫", 4, "选择阵营")
NUM = InputBox("输入轮换人类/屠夫的数量：                                                                     选择单独角色模式输入0                                                                        '取消'退出","选择挂机模式")
//查找窗口类名(0)或者标题("DeadByDaylight  "),返回找到的句柄Hwnd
Hwnd = Plugin.Window.Find(0, "DeadByDaylight  ")
//Call Plugin.Window.Show(Hwnd)
Call Plugin.Window.Top(Hwnd, 0)
Call Plugin.Window.Top(Hwnd, 1)
If   IsEmpty(NUM) = True Then
    ExitScript
End If
num = CInt(NUM)
If zy = 6 Then //判断输入数量是否超过最大值
    If num > 31 Then //人类最大角色数量
        MessageBox ("参数错误，请重启脚本。")
        EndScript
    ElseIf num = 0 Then
        Goto  匹配
    End If
ElseIf zy = 7 Then
    If num > 29 Then //屠夫最大角色数量
        MessageBox ("参数错误，请重启脚本。")
        EndScript
    ElseIf num = 0 Then
        Goto  匹配
    End If
End If 
Rem 选择
FindColorEx 105,873,178,149,"7F7F7F",0,0.9,intX,intY//检测图标灰白色
If intX > 0 And intY > 0 Then 
    Delay 3000
    Call change()
Else 
    Call dx()//检测断线
    If dxi = 1 Then 
        Goto 重连  
    End If
    Goto 选择
End If
Rem 匹配
//Call CheckTime()//再次检测当前时间.2
//检测血点,是否进入匹配界面
Call xd()
If xdi = 1 Then 
    If num = 0 Then 
        Delay 5000
    End If
    MoveTo 1, 1
    Delay 500
    LeftClick 1
    Delay 1000
    MoveTo 1758, 1003
    Delay 1000
    LeftClick 1
    Delay 500
    MoveTo 139, 689
    Delay 1500
    Call dx()//检测断线
    If dxi = 1 Then 
        Goto 重连  
    End If
    Delay 1500
    FindColor 292,978,341,1032,"7F7F7F",intX,intY//检测左下角设置
    If intX > 0 And intY > 0 Then 
        Goto 匹配
    End If
Else 
    Call dx()//检测断线
    If dxi = 1 Then 
        Goto 重连  
    End If
    Goto 匹配
End If
Rem 准备
//Rem 调试
//是否进入房间
FindColor 292,978,341,1032,"7F7F7F",intX,intY//检测左下角设置
If intX > 0  And intY > 0  Then 
    Delay 3000
    MoveTo 1, 1
    Delay 1000
    LeftClick 1
    Delay 2000
    MoveTo 1758, 1003
    Delay 1000
    LeftClick 1
    Delay 500
    MoveTo 105, 660
    Delay 2000
    If zy = 6 Then //人类提示
        KeyPress "Enter", 1
        Delay 500
        //        KeyPress "T", 1
        //        KeyPress "H", 1
        //        KeyPress "I", 1
        //        KeyPress "S", 1
        //        KeyPress "Space", 1
        //        KeyPress "I", 1
        //        KeyPress "S", 1
        //        KeyPress "Space", 1
        KeyDown 16, 1
        KeyPress 65, 1
        KeyUp 16, 1
        KeyDown 16, 1
        KeyPress 70, 1
        KeyUp 16, 1
        KeyDown 16, 1
        KeyPress 75, 1
        KeyUp 16, 1
        //        KeyPress "Space", 1
        //        KeyPress "S", 1
        //        KeyPress "C", 1
        //        KeyPress "R", 1
        //        KeyPress "I", 1
        //        KeyPress "P", 1
        //        KeyPress "T", 1
        //        KeyPress "Enter", 1
    End If
Else
    Call dx()//检测断线
    If dxi = 1 Then 
        Goto 重连  
    End If
    Goto 准备
End If
Rem 载入
//Rem 调试
//是否出现技能图标
Call jn()
If jni = 1 Then
    Delay 3000
Else 
    FindColorEx 231,1,335,46,"84847D",0,0.9,intA,intB//祭品燃烧界面，以防误查断线
    Call dx()
    If intA > 0 and intB > 0  Then 
        Goto 载入
    ElseIf  dxi = 1 Then
        Goto 重连
    End If
    Goto 载入
End If
Rem 局内
Call jn()
If jni = 1 Then 
    If zy = 6 Then 
        Call human()
        Goto 局内
    ElseIf zy = 7 Then
        Call killer()
        Goto 局内
    End If	
Else 
    Delay  2000
    Call dx()//是否断线
    If dxi = 1 Then 
        Goto 重连
    End If
    /*检测血点，确保对局确实结束*/
    Call xd()
    If xdi = 0 Then 
        Goto 局内
    Else 
        Delay 5000
        MoveTo 200, 867
        Delay 1000
        LeftClick 1
        MoveTo 1736, 1010
        LeftClick 1
        Delay 1000
        LeftClick 1
        If num < 1  Then 
            Goto 匹配
        ElseIf num > 0 Then
            Goto 选择
        End If
    End If
End If
Rem 重连
Delay 2000
MoveTo 586, 679  //错误代码1
LeftClick 1
Delay 1000
MoveTo 570, 710  //错误代码2
LeftClick 1
Delay 1000
MoveTo 1335, 635 //错误代码3
LeftClick 1
Delay 1000
MoveTo 1430, 640 //错误代码4
LeftClick 1
Delay 1000
MoveTo 563,722 //错误代码5
LeftClick 1
Delay 2000
//检测血点,判断断线情况
Call xd()
If xdi = 1 Then     //小退
    FindColorEx 292,978,341,1032,"7F7F7F",0,0.9,intX,intY//检测左下角设置
    If intX > 0 And intY > 0 Then 
        Goto 匹配
    End If
    MoveTo 1335, 635
    LeftClick 1
    Delay 1000
    MoveTo 1736, 1010
    LeftClick 1
    Delay 1000
    LeftClick 1
    Goto 匹配
Else
    //大退
    Rem 大退
    Delay 1000
    LeftClick 1
    Delay 1000
    Call dx()/*检测断线*/
    If dxi = 1 Then
        MoveTo 1335, 635  //重进
        LeftClick 1
        Delay 1000
        MoveTo 1335, 667  //重进错误点击
        LeftClick 1
        Delay 1000
        LeftClick 1//重进
        Goto 大退
    End If
    Delay 1000
    MoveTo 1453, 628  //错误
    LeftClick 1
    Delay 1000
    MoveTo 1413, 992 //新闻点击
    LeftClick 1
    Delay 1000
    MoveTo 1430, 744 //账号链接
    LeftClick 1
    Delay 1000
    MoveTo 1631, 966//转生系统
    LeftClick 1
    Delay 1000
    //Rem 调试
    //每日祭礼判断
    FindColor 448,271,512,301,"FFFFFF",intX,intY
    If intX> 0 And intY> 0 Then
        MoveTo 483, 896
        LeftClick 1
        Delay 1000
    End If
    FindColorEx 504,935,569,997,"7F7F7F",2,0.9,intX,intY//是否重进主页面判断
    If intX > 0 And intY > 0 Then 
        If zy = 6 Then 
            MoveTo 143, 261//回到人类
            LeftClick 1
        ElseIf zy = 7 Then
            MoveTo 135, 133 //回到屠夫
            LeftClick 1
        End If
    Else
        Goto 大退
    End If
    Goto 匹配
End If
Sub CheckTime()/*检测时间*/
    dim t
    t=lib.网络.获取网络时间_增强版("www.taobao.com")//赋值当前日期时间到变量t
    d = Day(t)
    y = Month(t)
    n = Year(t)
    If y >= 11 And d >= 1 And n >= 2022 Then //2022年10月31日过期
        MessageBox "已失效"
        ExitScript
    End If	
End Sub
Sub change()
    Dim ghX
    ghX = Array(405, 548, 703, 854, 404,548, 703, 854,404, 548, 703, 854,404,548, 703,854,404,548, 703,854,404,548, 703,854,404,549,709,858,384,556,715,882)/*四个一组（548~404），目前32个，增加一个角色在最后七个之前加一组*/
    Dim ghY
    ghy = Array(314, 323, 318, 302, 536,323, 318, 302,536, 323, 318, 302,536,323, 318,302,536,323, 318,302,536,323, 318,302,536,517,528,523,753,741,749,750)
    Delay 1000
    MoveTo 1, 1
    Delay 1000
    LeftClick 1
    Delay 1000
    MoveTo 141,109
    Delay 1000
    LeftClick 1
    Rem 判断
    If i < num  Then
        moveX = ghX(i)
        moveY = ghY(i)
        Delay 1000
        MoveTo moveX, moveY
        Delay 3000
        LeftClick 1
        i = i + 1
    Else
        i = 0
        If num > 4 Then 
            MoveTo 522, 394
            Delay 1000
            MouseWheel 1
            Delay 1000
            MouseWheel 1
        End If
        Goto 判断
    End If
End Sub
Function jn()/*检测技能是否出现*/
    FindColorEx 1605, 780, 1855, 1021, "5E2450", 0, 0.9, intX, intY//三级技能
    FindColorEx 1605, 780, 1855, 1021, "0E3807", 0, 0.9, ejnX, ejnY//二级技能
    FindColorEx 1605, 780, 1855, 1021, "2E9EC3", 0, 0.9, yjnX, yjnY//一级技能
    FindColor 125,948,142,967,"FEFEFE",jntX,jntY//左侧技能图标（维克托专用）
    If intX > 0 or intY > 0 or ejnX > 0 Or ejnY > 0 or yjnX > 0 or yjnY > 0 or jntX > 0 or jntY > 0 Then 
        jni = 1
    Else 
        jni = 0
    End If
End Function
Function dx()/*检测断线，暗红色点*/
    //    FindColor 1882, 412, 1901, 425, "44447C",  intX, intY
    //    FindColor 1869, 405, 1915, 431, "13132E", inX, inY
    XY = Plugin.Color.FindColorBlock(1882, 412, 1915, 425, "13132E", 5, 5, 0, 1)
    iZB = InStr(XY, "|")
    X = CLng(Left(XY, iZB - 1))
    Y = CLng(Right(XY, Len(XY) - iZB))
    If  X>0 or Y>0 Then
        dxi = 1
    Else 
        dxi = 0
    End If
End Function
Function xd()/*检测血点、暗金、裂片*/
    FindColorEx 1232,53,1371,94,"03A1EA",0,0.9,ajX,ajY//暗金细胞
    FindColorEx 1366,57,1507,93,"C08185",0,0.9,spX,spY//荧红裂片
    FindColorEx 1571,52,1607,92,"0C04BF",0,0.9,xdX,xdY//血点
    If ajX > 0 and ajY > 0 and spX > 0 and spY > 0 and xdX > 0 and xdY > 0 Then 
        xdi = 1
    Else
        xdi = 0
    End  If
End Function
Sub human()//人类动作
    KeyDownH "Shift", 1
    Call n1()
    KeyDown act1, 1
    Call n2()
    KeyDown act2, 1
    Delay Lib.算法.随机数字串(3)
    KeyUp act2, 1
    Delay 500
    LeftDown 1
    Delay 2000
    LeftUp 1
    KeyUp act1,1
    Call n1()
    KeyDown act1,1
    Call n2()
    KeyDown act2, 1
    Delay Lib.算法.随机数字串(3)
    KeyUp act2, 1
    Delay 500
    LeftDown 1
    Delay 2000
    LeftUp 1
    KeyUp act1,1
    Call n1()
    KeyDown act1,1
    Call n2()
    KeyDown act2, 1
    Delay Lib.算法.随机数字串(3)
    KeyUp act2, 1
    Delay 500
    LeftDown 1
    Delay 2000
    LeftUp 1
    KeyPress "Space", 1
    KeyUp act1, 1
    KeyUpH "Shift", 1
End Sub
Sub killer()//屠夫动作
    KeyDown "Up", 1 /**/
    Delay 1000
    KeyUp "Up", 1   /*抬头*/
    Call n1()
    KeyDown act1, 1/**/
    Delay 1500
    Call n2()
    KeyDown act2, 1
    Delay Lib.算法.随机数字串(3)
    KeyUp act2, 1
    Delay 300
    KeyUp act1, 1
    Call n1()
    KeyDown act1,1
    Call n2()
    KeyDown act2, 1
    Delay Lib.算法.随机数字串(3)
    KeyUp act2, 1
    Delay 300
    KeyUp act1, 1
    Call n1()
    KeyDown act1,1
    Call n2()
    KeyDown act2, 1
    Delay Lib.算法.随机数字串(3)
    KeyUp act2, 1
    Delay 300
    KeyUp act1, 1/*主体动作*/
    Call n1()
    KeyDown act1, 1
    Call n2()
    KeyDown act2,1
    Delay 200
    KeyDown "Ctrl", 1/**/
    Delay 4000
    KeyUp "Ctrl", 1/*大招*/
    KeyDown "Down", 1/**/
    Delay 400
    KeyUp "Down", 1/*低头使用技能*/
    KeyUp act2,1
    KeyUp act1, 1
    Call n1()
    KeyDown act1, 1
    Call n2()
    KeyDown act2, 1    
    RightDown 1/**/
    Delay 3000  
    KeyPress "Ctrl", 1
    RightUp 1/*右键能力*/
    Delay 3000
    KeyUp act2, 1
    KeyUp act1,1
    Call n1()
    KeyDown act1, 1
    Call n2()
    KeyDown act2,1
    RightDown 1/**/
    Delay 2500
    LeftClick 20
    RightUp 1
    Delay 1500
    KeyPress "Ctrl", 1/*右键能力左键使用*/
    Delay 1500
    KeyPress "Space", 1
    KeyUp act2, 1
    KeyUp act1, 1//结束动作 
End Sub
Function n1()//随机移动
    n = Int((6 - 1 + 1) * Rnd + 1)
    If n = 1 or n = 5 or n = 6 Then
        act1 = "W"
    End If
    If n = 2 Then
        act1 = "A"
    End If
    If n = 3 Then
        act1 = "D"
    End If
    If n = 4 Then
        act1 = "S"
    End If
End Function
Function n2()//随机转向
    n = Int((2 - 1 + 1) * Rnd + 1)
    If n = 1 Then
        act2 = "Q"
    End If
    If n = 2 Then
        act2 = "E"
    End If
End Function
