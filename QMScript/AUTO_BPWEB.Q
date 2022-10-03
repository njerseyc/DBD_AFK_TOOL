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
MacroID=9a94b1db-ea3e-4699-9d5e-2568b4a3d4f1
Description=AUTO_BPWEB
Enable=0
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

[Script]
/////////////////////////////////////////////
//                                         //
//此脚本开源免费，项目地址：                 //
//https://github.com/maskrs/DBD_AFK_TOOL   //
//                                         //
/////////////////////////////////////////////

////////////////////////
//需要全屏游戏并关闭滤镜/
///////////////////////

Dim buy, wait,i,colors1,colors2
colors1 = array("39495F","344357","303E50","384A62")/*白配、白祭品、枭祭环、白礼盒*/
colors2 = array("32879E","256E2D","175213","79326A","4015AB")/*黄物品、绿物品、绿警局、紫物品、红物品*/
buy = 455
wait = 385
i = 0
Rem bpweb
MoveTo 630, 140//避免遮挡
FindColorEx 250, 200, 1100,982, colors1(i), 2,1.0, intX, intY//普通配件 73929C
If intX > 0 and intY > 0 Then 
    MoveTo intX+1, intY+1
    Delay 50
    LeftDown 1
    Delay buy
    LeftUp 1
    Delay wait
    i = 0
    Goto bpweb
Else 
    i = i + 1
    If i > UBound (colors1) Then /*低级别数组遍历结束，跳转到高级别*/
        i = 0
        Goto highgrade
    End If
    Goto bpweb
End If
Rem highgrade
FindColorEx 250, 200, 1100,982, colors2(i), 2,0.9, intX, intY//高级配件 73929C
If intX > 0 and intY > 0 Then 
    MoveTo intX+1, intY+1
    Delay 50
    LeftDown 1
    Delay buy
    LeftUp 1
    Delay wait
    i = 0
    Goto bpweb
Else 
    i = i + 1
    If i > UBound (colors2) Then /*数组遍历结束，回到起点*/
        i = 0
        Goto bpweb
    End If 
    Goto highgrade
End If
//TracePrint colors(i)
//FindColorEx 250, 209, 1100, 982, "FFFFFF", 2,0.9, intX, intY//白 73929C
//If intX > 0 And intY > 0 Then 
//    MoveTo intX-1, intY-1
//    Delay 50
//    LeftDown 1
//    Delay buy
//    LeftUp 1
//    Delay wait
//    Goto bpweb
//End If
//Goto bpweb
