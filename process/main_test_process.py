import os.path
import random
import time
import threading
import multiprocessing
from multiprocessing.managers import BaseManager
import webbrowser
import pyautogui as py
import requests, re
import ctypes
import win32api, win32gui
from keyboard_operation import key_down, key_up
from operator import lt, eq, gt, ge, ne, floordiv, mod
import pynput
import sys
import psutil
import json
from win32api import MessageBox
import win32con
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import PyQt5.QtCore as qc
from DBDAutoScriptUI import Ui_MainWindow
from selec_killerUI import Ui_Dialog
from Coord import *


def exit_program():
    global AFK_pid, hotkey_pid
    psutil.Process(hotkey_pid).terminate()
    psutil.Process(AFK_pid).terminate()
    psutil.Process(os.getpid()).kill()

def begin():
    global AFK_pid
    save_cfg()
    begin = multiprocessing.Process(target=AFK, daemon=True)
    begin.start()
    AFK_pid = begin.pid



class DbdWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = Ui_MainWindow()
        self.sel_dialog = SelectWindow()
        qss_style = '''
            QPushButton:hover {
                background-color: #EEF1F2;
                border: 1px solid #D0D3D4;
                border-radius: 5px;
            }
            QPushButton:pressed, QPushButton:checked {
                border: 1px solid #BEC9CA;
                background-color: #EDEEEF;
                border-radius: 5px;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
            }
            QCheckBox::indicator:unchecked {
                border-image: url(picture/checkbox_unchecked.png);
            }
            QCheckBox::indicator:checked{
                border-image: url(picture/checkbox_checked_border.png);
            }
            QCheckBox::indicator:unchecked:hover {
                border-image: url(picture/checkbox_hover.png);
            }
            QRadioButton::indicator {
                width: 15px;
                height: 15px;
            }
            QRadioButton::indicator:checked {
                border-image: url(picture/radiobutton_checked.png);
            }
            QRadioButton::indicator:unchecked {
                border-image: url(picture/radiobutton_unchecked.png);
            }
            QRadioButton::indicator:unchecked:hover {
            border-image: url(picture/radiobutton_hover_border.png);
            }
        '''
        # self.sel_dialog.setStyleSheet(qss_style)
        self.main_ui.setupUi(self)
        # self.main_ui.sb_input_count.setMaximum(30)
        self.main_ui.pb_select_cfg.clicked.connect(self.pb_select_cfg_click)
        # self.main_ui.cb_rotate_solo.clicked.connect(self.cb_rotate_solo_click)
        # self.main_ui.cb_rotate_order.clicked.connect(self.cb_rotate_order_click)
        # self.main_ui.cb_select_killer.clicked.connect(self.cb_select_killer_click)
        self.main_ui.pb_research.clicked.connect(self.pb_research_click)
        self.main_ui.pb_start.clicked.connect(begin)
        self.main_ui.pb_stop.clicked.connect(exit_program)
        self.main_ui.pb_github.clicked.connect(self.github)

    def pb_research_click(self):
        lw.SetDict(0, "DbdKillerNames.txt")  # 设置字库
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        moveclick(141, 109, 1, 1)  # 打开角色按钮
        back_first()
        custom_select.search_killer_name(30)

    def github(self):
        webbrowser.open("https://github.com/maskrs/DBD_AFK_TOOL/releases")

    def pb_select_cfg_click(self):
        self.sel_dialog.exec()
    #
    # def cb_rotate_solo_click(self):
    #     self.main_ui.cb_rotate_order.setChecked(False)
    #     self.main_ui.cb_select_killer.setChecked(False)
    #
    # def cb_rotate_order_click(self):
    #     self.main_ui.cb_rotate_solo.setChecked(False)
    #     self.main_ui.cb_select_killer.setChecked(False)
    #
    # def cb_select_killer_click(self):
    #     self.main_ui.cb_rotate_solo.setChecked(False)
    #     self.main_ui.cb_rotate_order.setChecked(False)

class SelectWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.select_ui = Ui_Dialog()
        self.select_ui.setupUi(self)
        self.select_ui.pb_all.clicked.connect(self.pb_select_all_click)
        self.select_ui.pb_invert.clicked.connect(self.pb_invert_click)
        self.select_ui.pb_save.clicked.connect(self.pb_save_click)

    def pb_select_all_click(self):
        """全选点击槽"""
        self.select_ui.cb_jiage.setChecked(True)
        self.select_ui.cb_dingdang.setChecked(True)
        self.select_ui.cb_dianjv.setChecked(True)
        self.select_ui.cb_hushi.setChecked(True)
        self.select_ui.cb_tuzi.setChecked(True)
        self.select_ui.cb_maishu.setChecked(True)
        self.select_ui.cb_linainai.setChecked(True)
        self.select_ui.cb_laoyang.setChecked(True)
        self.select_ui.cb_babu.setChecked(True)
        self.select_ui.cb_fulaidi.setChecked(True)
        self.select_ui.cb_zhuzhu.setChecked(True)
        self.select_ui.cb_xiaochou.setChecked(True)
        self.select_ui.cb_lingmei.setChecked(True)
        self.select_ui.cb_juntuan.setChecked(True)
        self.select_ui.cb_wenyi.setChecked(True)
        self.select_ui.cb_guimian.setChecked(True)
        self.select_ui.cb_mowang.setChecked(True)
        self.select_ui.cb_guiwushi.setChecked(True)
        self.select_ui.cb_qiangshou.setChecked(True)
        self.select_ui.cb_sanjiaotou.setChecked(True)
        self.select_ui.cb_kumo.setChecked(True)
        self.select_ui.cb_liantiying.setChecked(True)
        self.select_ui.cb_gege.setChecked(True)
        self.select_ui.cb_zhuizhui.setChecked(True)
        self.select_ui.cb_dingzitou.setChecked(True)
        self.select_ui.cb_niaojie.setChecked(True)
        self.select_ui.cb_zhenzi.setChecked(True)
        self.select_ui.cb_yingmo.setChecked(True)
        self.select_ui.cb_weishu.setChecked(True)
        self.select_ui.cb_eqishi.setChecked(True)

    def pb_invert_click(self):
        self.select_ui.cb_jiage.toggle()
        self.select_ui.cb_dingdang.toggle()
        self.select_ui.cb_dianjv.toggle()
        self.select_ui.cb_hushi.toggle()
        self.select_ui.cb_tuzi.toggle()
        self.select_ui.cb_maishu.toggle()
        self.select_ui.cb_linainai.toggle()
        self.select_ui.cb_laoyang.toggle()
        self.select_ui.cb_babu.toggle()
        self.select_ui.cb_fulaidi.toggle()
        self.select_ui.cb_zhuzhu.toggle()
        self.select_ui.cb_xiaochou.toggle()
        self.select_ui.cb_lingmei.toggle()
        self.select_ui.cb_juntuan.toggle()
        self.select_ui.cb_wenyi.toggle()
        self.select_ui.cb_guimian.toggle()
        self.select_ui.cb_mowang.toggle()
        self.select_ui.cb_guiwushi.toggle()
        self.select_ui.cb_qiangshou.toggle()
        self.select_ui.cb_sanjiaotou.toggle()
        self.select_ui.cb_kumo.toggle()
        self.select_ui.cb_liantiying.toggle()
        self.select_ui.cb_gege.toggle()
        self.select_ui.cb_zhuizhui.toggle()
        self.select_ui.cb_dingzitou.toggle()
        self.select_ui.cb_niaojie.toggle()
        self.select_ui.cb_zhenzi.toggle()
        self.select_ui.cb_yingmo.toggle()
        self.select_ui.cb_weishu.toggle()
        self.select_ui.cb_eqishi.toggle()

    def pb_save_click(self):
        save_cfg()

class CustomSelectKiller:
    def __init__(self):
        self.ocr_error = 0
        self.killer_name_array = []
        self.own_number = 0
        self.select_killer_lst = []
        self.match_select_killer_lst = []
        self.all_killer_name = ["设陷者", "幽灵", "农场主", "护士", "女猎手", "迈克尔迈尔斯", "妖巫", "医生",
                                "食人魔", "梦魇", "门徒", "小丑", "怨灵", "军团", "瘟疫", "鬼面", "魔王", "鬼武士",
                                "死亡枪手", "处刑者", "枯萎者", "连体婴", "骗术师", "NEMESIS", "地狱修士", "艺术家",
                                "贞子", "影魔", "操纵者", "恶骑士"]

    def read_search_killer_name(self):
        with open(SEARCH_PATH, "r", encoding='UTF-8') as search_file:
            self.killer_name_array = search_file.readlines()
            self.killer_name_array = [c.strip() for c in self.killer_name_array]


    def killer_name_ocr(self):
        killername = Coord(408, 61, 629, 99)
        killername.processed_coord()
        killername.area_check()
        self.killer_name = lw.Ocr(killername.x1_coor, killername.y1_coor, killername.x2_coor, killername.y2_coor, "#95", 0.75)
        if self.killer_name in self.all_killer_name:
            self.write_killer_name()
            if self.killer_name == "恶骑士": # 随版本更改
                self.ocr_error = 1
                back_first()
                moveclick(387, 300, 1, 1)
                moveclick(141, 109, 1, 1)  # 关闭角色按钮
                id = win32gui.FindWindow(None, u"DBD_AFK_TOOL")
                win32gui.SetWindowPos(id, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                      win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
                win32gui.SetWindowPos(id, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                      win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
                MessageBox(0, "角色检索已完成", "提醒", win32con.MB_ICONASTERISK)
                with open(SEARCH_PATH, "w", encoding='UTF-8') as search_file:
                    search_file.write("\n".join(self.killer_name_array))

        else:
            back_first()
            moveclick(387, 300, 1, 1)
            moveclick(141, 109, 1, 1)  # 关闭角色按钮
            id = win32gui.FindWindow(None, u"DBD_AFK_TOOL")
            win32gui.SetWindowPos(id, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            win32gui.SetWindowPos(id, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            MessageBox(0, "检索完成\n" + str(self.killer_name_array) + "\n有错误或乱码请重新检索", "提醒", win32con.MB_ICONASTERISK)
            with open(SEARCH_PATH, "w") as search_file:
                search_file.write("\n".join(self.killer_name_array))
            self.ocr_error = 1
            self.killer_name_array.clear()
    def write_killer_name(self):
        self.killer_name_array.append(self.killer_name)

    def search_killer_name(self, ownnumber):
        self.ocr_error = 0
        choice_last_x = [546, 708, 847, 395, 551, 705, 855]
        choice_last_y = [497, 495, 486, 724, 717, 717, 710]
        change_x = 387
        change_y = 300
        changecount_x = 0
        changecount_y = 0
        count = 0
        n = 0
        self.own_number = ownnumber  # 拥有的角色数量
        result_integer = self.own_number // 4  # 取整
        result_remainder = self.own_number % 4  # 取余数

        if result_remainder == 0:
            result_integer = result_integer - 1
            result_remainder = 4

        timetypeone = result_integer
        timetypetwo = result_remainder
        # 随版本更新
        if result_integer >= 7:
            timetypeone = 6

        while True:
            if self.ocr_error == 1:
                break
            if count == timetypeone:
                moveclick(387, 530, 1, 1)
                self.killer_name_ocr()
                if self.ocr_error == 1:
                    break
                if result_integer > 5:
                    break
                change_x = 387
                change_y = 300
                change = Coord(change_x, change_y)
                change.processed_coord()
                for i in range(timetypetwo):
                    py.moveTo(change.x1_coor, change.y1_coor)
                    if n != 0:
                        time.sleep(1)
                        py.click()
                        time.sleep(1)
                        self.killer_name_ocr()
                        if self.ocr_error == 1:
                            break
                    n += 1
                    change_x += 158
                break
            while True:
                if self.ocr_error == 1:
                    break
                change = Coord(change_x, change_y)
                change.processed_coord()
                moveclick(change.x1_coor, change.y1_coor, 1, 1)
                self.killer_name_ocr()
                if self.ocr_error == 1:
                    break
                change_y = 300
                change_x += 158
                changecount_x += 1
                if changecount_x == 4:
                    break
            change_x = 387
            changecount_x = 0
            changecount_y += 1
            change_y += 225
            count += 1
            if changecount_y == 2:
                changecount_y = 0
            if self.ocr_error == 1:
                break
                ###
        if result_integer > 5:
            if result_integer <= 6:
                timetypetwo = timetypetwo - 1
            elif result_integer >= 7:
                timetypetwo += 3
            n = 0
            for i in range(timetypetwo):
                if self.ocr_error == 1:
                    break
                linex = choice_last_x[n]
                liney = choice_last_y[n]
                line = Coord(linex, liney)
                line.processed_coord()
                moveclick(line.x1_coor, line.y1_coor, 1, 1)
                self.killer_name_ocr()
                # if self.ocr_error == 1:
                #     break
                n += 1

    def select_killer_name(self):
        if settings.value("CUSSEC/cb_jiage"):
            self.select_killer_lst.append("设陷者")
        if settings.value("CUSSEC/cb_dingdang"):
            self.select_killer_lst.append("幽灵")
        if settings.value("CUSSEC/cb_dianjv"):
            self.select_killer_lst.append("农场主")
        if settings.value("CUSSEC/cb_hushi"):
            self.select_killer_lst.append("护士")
        if settings.value("CUSSEC/cb_tuzi"):
            self.select_killer_lst.append("女猎手")
        if settings.value("CUSSEC/cb_maishu"):
            self.select_killer_lst.append("迈克尔迈尔斯")
        if settings.value("CUSSEC/cb_linainai"):
            self.select_killer_lst.append("妖巫")
        if settings.value("CUSSEC/cb_laoyang"):
            self.select_killer_lst.append("医生")
        if settings.value("CUSSEC/cb_babu"):
            self.select_killer_lst.append("食人魔")
        if settings.value("CUSSEC/cb_fulaidi"):
            self.select_killer_lst.append("梦魇")
        if settings.value("CUSSEC/cb_zhuzhu"):
            self.select_killer_lst.append("门徒")
        if settings.value("CUSSEC/cb_xiaochou"):
            self.select_killer_lst.append("小丑")
        if settings.value("CUSSEC/cb_lingmei"):
            self.select_killer_lst.append("怨灵")
        if settings.value("CUSSEC/cb_juntuan"):
            self.select_killer_lst.append("军团")
        if settings.value("CUSSEC/cb_wenyi"):
            self.select_killer_lst.append("瘟疫")
        if settings.value("CUSSEC/cb_guimian"):
            self.select_killer_lst.append("鬼面")
        if settings.value("CUSSEC/cb_mowang"):
            self.select_killer_lst.append("魔王")
        if settings.value("CUSSEC/cb_guiwushi"):
            self.select_killer_lst.append("鬼武士")
        if settings.value("CUSSEC/cb_qiangshou"):
            self.select_killer_lst.append("死亡枪手")
        if settings.value("CUSSEC/cb_sanjiaotou"):
            self.select_killer_lst.append("处刑者")
        if settings.value("CUSSEC/cb_kumo"):
            self.select_killer_lst.append("枯萎者")
        if settings.value("CUSSEC/cb_liantiying"):
            self.select_killer_lst.append("连体婴")
        if settings.value("CUSSEC/cb_gege"):
            self.select_killer_lst.append("骗术师")
        if settings.value("CUSSEC/cb_zhuizhui"):
            self.select_killer_lst.append("NEMESIS")
        if settings.value("CUSSEC/cb_dingzitou"):
            self.select_killer_lst.append("地狱修士")
        if settings.value("CUSSEC/cb_niaojie"):
            self.select_killer_lst.append("艺术家")
        if settings.value("CUSSEC/cb_zhenzi"):
            self.select_killer_lst.append("贞子")
        if settings.value("CUSSEC/cb_yingmo"):
            self.select_killer_lst.append("影魔")
        if settings.value("CUSSEC/cb_weishu"):
            self.select_killer_lst.append("操纵者")
        if settings.value("CUSSEC/cb_eqishi"):
            self.select_killer_lst.append("恶骑士")

    def match_select_killer_name(self):
        for i in self.select_killer_lst:
            self.match_select_killer_lst.append(self.killer_name_array.index(i)+1)

    def debug_traverse(self):  # 遍历调试
        killer_name_array_len = len(self.killer_name_array)
        print(*self.killer_name_array, sep=",")
        for i in range(0, killer_name_array_len):
            print(self.killer_name_array[i])


def initialize():
    """ 程序初始化 """
    # if not os.path.exists(DBDAS_PATH):
    #     os.makedirs(DBDAS_PATH)
    global CFG_PATH, custom_select, dbd_window

    if not os.path.exists(CFG_PATH):
        with open(CFG_PATH, 'w') as configfile:
            configfile.write("")
        settings.setValue("CPCI/rb_survivor", False)
        settings.setValue("CPCI/cb_survivor_do", False)
        settings.setValue("CPCI/rb_killer", False)
        settings.setValue("CPCI/cb_killer_do", False)
        settings.setValue("CPCI/rb_fixed_mode", False)
        settings.setValue("CPCI/rb_random_mode", False)
        # settings.setValue("CPCI/rb_single_mode", False)
        # settings.setValue("CPCI/rb_rotate_mode", False)
        # settings.setValue("CPCI/cb_select_killer", False)
        # settings.setValue("CPCI/cb_rotate_solo", False)
        # settings.setValue("CPCI/cb_rotate_order", False)
        settings.setValue("UPDATE/cb_autocheck", True)
        settings.setValue("CUSSEC/cb_jiage", False)
        settings.setValue("CUSSEC/cb_dingdang", False)
        settings.setValue("CUSSEC/cb_dianjv", False)
        settings.setValue("CUSSEC/cb_hushi", False)
        settings.setValue("CUSSEC/cb_tuzi", False)
        settings.setValue("CUSSEC/cb_maishu", False)
        settings.setValue("CUSSEC/cb_linainai", False)
        settings.setValue("CUSSEC/cb_laoyang", False)
        settings.setValue("CUSSEC/cb_babu", False)
        settings.setValue("CUSSEC/cb_fulaidi", False)
        settings.setValue("CUSSEC/cb_zhuzhu", False)
        settings.setValue("CUSSEC/cb_xiaochou", False)
        settings.setValue("CUSSEC/cb_lingmei", False)
        settings.setValue("CUSSEC/cb_juntuan", False)
        settings.setValue("CUSSEC/cb_wenyi", False)
        settings.setValue("CUSSEC/cb_guimian", False)
        settings.setValue("CUSSEC/cb_mowang", False)
        settings.setValue("CUSSEC/cb_guiwushi", False)
        settings.setValue("CUSSEC/cb_qiangshou", False)
        settings.setValue("CUSSEC/cb_sanjiaotou", False)
        settings.setValue("CUSSEC/cb_kumo", False)
        settings.setValue("CUSSEC/cb_liantiying", False)
        settings.setValue("CUSSEC/cb_gege", False)
        settings.setValue("CUSSEC/cb_zhuizhui", False)
        settings.setValue("CUSSEC/cb_dingzitou", False)
        settings.setValue("CUSSEC/cb_niaojie", False)
        settings.setValue("CUSSEC/cb_zhenzi", False)
        settings.setValue("CUSSEC/cb_yingmo", False)
        settings.setValue("CUSSEC/cb_weishu", False)
        settings.setValue("CUSSEC/cb_eqishi", False)

def save_cfg():
    """ 保存配置文件 """
    global CFG_PATH, custom_select, dbd_window
    # BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
    # CFG_PATH = os.path.join(BASE_DIR, "cfg.ini")
    # settings = qc.QSettings(CFG_PATH, qc.QSettings.IniFormat)
    settings.setValue("CPCI/rb_survivor", dbd_window.main_ui.rb_survivor.isChecked())
    settings.setValue("CPCI/cb_survivor_do", dbd_window.main_ui.cb_survivor_do.isChecked())
    settings.setValue("CPCI/rb_killer", dbd_window.main_ui.rb_killer.isChecked())
    settings.setValue("CPCI/cb_killer_do", dbd_window.main_ui.cb_killer_do.isChecked())
    settings.setValue("CPCI/rb_fixed_mode", dbd_window.main_ui.rb_fixed_mode.isChecked())
    settings.setValue("CPCI/rb_random_mode", dbd_window.main_ui.rb_random_mode.isChecked())
    # settings.setValue("CPCI/rb_single_mode", dbd_window.main_ui.rb_single_mode.isChecked())
    # settings.setValue("CPCI/rb_rotate_mode", dbd_window.main_ui.rb_rotate_mode.isChecked())
    # settings.setValue("CPCI/cb_select_killer", dbd_window.main_ui.cb_select_killer.isChecked())
    # settings.setValue("CPCI/cb_rotate_solo", dbd_window.main_ui.cb_rotate_solo.isChecked())
    # settings.setValue("CPCI/cb_rotate_order", dbd_window.main_ui.cb_rotate_order.isChecked())
    settings.setValue("UPDATE/cb_autocheck", dbd_window.main_ui.cb_autocheck.isChecked())
    settings.setValue("CUSSEC/cb_jiage", dbd_window.sel_dialog.select_ui.cb_jiage.isChecked())
    settings.setValue("CUSSEC/cb_dingdang", dbd_window.sel_dialog.select_ui.cb_dingdang.isChecked())
    settings.setValue("CUSSEC/cb_dianjv", dbd_window.sel_dialog.select_ui.cb_dianjv.isChecked())
    settings.setValue("CUSSEC/cb_hushi", dbd_window.sel_dialog.select_ui.cb_hushi.isChecked())
    settings.setValue("CUSSEC/cb_tuzi", dbd_window.sel_dialog.select_ui.cb_tuzi.isChecked())
    settings.setValue("CUSSEC/cb_maishu", dbd_window.sel_dialog.select_ui.cb_maishu.isChecked())
    settings.setValue("CUSSEC/cb_linainai", dbd_window.sel_dialog.select_ui.cb_linainai.isChecked())
    settings.setValue("CUSSEC/cb_laoyang", dbd_window.sel_dialog.select_ui.cb_laoyang.isChecked())
    settings.setValue("CUSSEC/cb_babu", dbd_window.sel_dialog.select_ui.cb_babu.isChecked())
    settings.setValue("CUSSEC/cb_fulaidi", dbd_window.sel_dialog.select_ui.cb_fulaidi.isChecked())
    settings.setValue("CUSSEC/cb_zhuzhu", dbd_window.sel_dialog.select_ui.cb_zhuzhu.isChecked())
    settings.setValue("CUSSEC/cb_xiaochou", dbd_window.sel_dialog.select_ui.cb_xiaochou.isChecked())
    settings.setValue("CUSSEC/cb_lingmei", dbd_window.sel_dialog.select_ui.cb_lingmei.isChecked())
    settings.setValue("CUSSEC/cb_juntuan", dbd_window.sel_dialog.select_ui.cb_juntuan.isChecked())
    settings.setValue("CUSSEC/cb_wenyi", dbd_window.sel_dialog.select_ui.cb_wenyi.isChecked())
    settings.setValue("CUSSEC/cb_guimian", dbd_window.sel_dialog.select_ui.cb_guimian.isChecked())
    settings.setValue("CUSSEC/cb_mowang", dbd_window.sel_dialog.select_ui.cb_mowang.isChecked())
    settings.setValue("CUSSEC/cb_guiwushi", dbd_window.sel_dialog.select_ui.cb_guiwushi.isChecked())
    settings.setValue("CUSSEC/cb_qiangshou", dbd_window.sel_dialog.select_ui.cb_qiangshou.isChecked())
    settings.setValue("CUSSEC/cb_sanjiaotou", dbd_window.sel_dialog.select_ui.cb_sanjiaotou.isChecked())
    settings.setValue("CUSSEC/cb_kumo", dbd_window.sel_dialog.select_ui.cb_kumo.isChecked())
    settings.setValue("CUSSEC/cb_liantiying", dbd_window.sel_dialog.select_ui.cb_liantiying.isChecked())
    settings.setValue("CUSSEC/cb_gege", dbd_window.sel_dialog.select_ui.cb_gege.isChecked())
    settings.setValue("CUSSEC/cb_zhuizhui", dbd_window.sel_dialog.select_ui.cb_zhuizhui.isChecked())
    settings.setValue("CUSSEC/cb_dingzitou", dbd_window.sel_dialog.select_ui.cb_dingzitou.isChecked())
    settings.setValue("CUSSEC/cb_niaojie", dbd_window.sel_dialog.select_ui.cb_niaojie.isChecked())
    settings.setValue("CUSSEC/cb_zhenzi", dbd_window.sel_dialog.select_ui.cb_zhenzi.isChecked())
    settings.setValue("CUSSEC/cb_yingmo", dbd_window.sel_dialog.select_ui.cb_yingmo.isChecked())
    settings.setValue("CUSSEC/cb_weishu", dbd_window.sel_dialog.select_ui.cb_weishu.isChecked())
    settings.setValue("CUSSEC/cb_eqishi", dbd_window.sel_dialog.select_ui.cb_eqishi.isChecked())

def read_cfg():
    """读取配置文件"""
    global CFG_PATH, custom_select, dbd_window
    # BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
    # CFG_PATH = os.path.join(BASE_DIR, "cfg.ini")
    # settings = qc.QSettings(CFG_PATH, qc.QSettings.IniFormat)
    dbd_window.main_ui.rb_survivor.setChecked(json.loads(settings.value("CPCI/rb_survivor")))
    dbd_window.main_ui.cb_survivor_do.setChecked(json.loads(settings.value("CPCI/cb_survivor_do")))
    dbd_window.main_ui.rb_killer.setChecked(json.loads(settings.value("CPCI/rb_killer")))
    dbd_window.main_ui.cb_killer_do.setChecked(json.loads(settings.value("CPCI/cb_killer_do")))
    dbd_window.main_ui.rb_fixed_mode.setChecked(json.loads(settings.value("CPCI/rb_fixed_mode")))
    dbd_window.main_ui.rb_random_mode.setChecked(json.loads(settings.value("CPCI/rb_random_mode")))
    # dbd_window.main_ui.rb_single_mode.setChecked(json.loads(settings.value("CPCI/rb_single_mode")))
    # dbd_window.main_ui.rb_rotate_mode.setChecked(json.loads(settings.value("CPCI/rb_rotate_mode")))
    # dbd_window.main_ui.cb_select_killer.setChecked(json.loads(settings.value("CPCI/cb_select_killer")))
    # dbd_window.main_ui.cb_rotate_solo.setChecked(json.loads(settings.value("CPCI/cb_rotate_solo")))
    # dbd_window.main_ui.cb_rotate_order.setChecked(json.loads(settings.value("CPCI/cb_rotate_order")))
    dbd_window.main_ui.cb_autocheck.setChecked(json.loads(settings.value("UPDATE/cb_autocheck")))
    dbd_window.sel_dialog.select_ui.cb_jiage.setChecked(json.loads(settings.value("CUSSEC/cb_jiage")))
    dbd_window.sel_dialog.select_ui.cb_dingdang.setChecked(json.loads(settings.value("CUSSEC/cb_dingdang")))
    dbd_window.sel_dialog.select_ui.cb_dianjv.setChecked(json.loads(settings.value("CUSSEC/cb_dianjv")))
    dbd_window.sel_dialog.select_ui.cb_hushi.setChecked(json.loads(settings.value("CUSSEC/cb_hushi")))
    dbd_window.sel_dialog.select_ui.cb_tuzi.setChecked(json.loads(settings.value("CUSSEC/cb_tuzi")))
    dbd_window.sel_dialog.select_ui.cb_maishu.setChecked(json.loads(settings.value("CUSSEC/cb_maishu")))
    dbd_window.sel_dialog.select_ui.cb_linainai.setChecked(json.loads(settings.value("CUSSEC/cb_linainai")))
    dbd_window.sel_dialog.select_ui.cb_laoyang.setChecked(json.loads(settings.value("CUSSEC/cb_laoyang")))
    dbd_window.sel_dialog.select_ui.cb_babu.setChecked(json.loads(settings.value("CUSSEC/cb_babu")))
    dbd_window.sel_dialog.select_ui.cb_fulaidi.setChecked(json.loads(settings.value("CUSSEC/cb_fulaidi")))
    dbd_window.sel_dialog.select_ui.cb_zhuzhu.setChecked(json.loads(settings.value("CUSSEC/cb_zhuzhu")))
    dbd_window.sel_dialog.select_ui.cb_xiaochou.setChecked(json.loads(settings.value("CUSSEC/cb_xiaochou")))
    dbd_window.sel_dialog.select_ui.cb_lingmei.setChecked(json.loads(settings.value("CUSSEC/cb_lingmei")))
    dbd_window.sel_dialog.select_ui.cb_juntuan.setChecked(json.loads(settings.value("CUSSEC/cb_juntuan")))
    dbd_window.sel_dialog.select_ui.cb_wenyi.setChecked(json.loads(settings.value("CUSSEC/cb_wenyi")))
    dbd_window.sel_dialog.select_ui.cb_guimian.setChecked(json.loads(settings.value("CUSSEC/cb_guimian")))
    dbd_window.sel_dialog.select_ui.cb_mowang.setChecked(json.loads(settings.value("CUSSEC/cb_mowang")))
    dbd_window.sel_dialog.select_ui.cb_guiwushi.setChecked(json.loads(settings.value("CUSSEC/cb_guiwushi")))
    dbd_window.sel_dialog.select_ui.cb_qiangshou.setChecked(json.loads(settings.value("CUSSEC/cb_qiangshou")))
    dbd_window.sel_dialog.select_ui.cb_sanjiaotou.setChecked(json.loads(settings.value("CUSSEC/cb_sanjiaotou")))
    dbd_window.sel_dialog.select_ui.cb_kumo.setChecked(json.loads(settings.value("CUSSEC/cb_kumo")))
    dbd_window.sel_dialog.select_ui.cb_liantiying.setChecked(json.loads(settings.value("CUSSEC/cb_liantiying")))
    dbd_window.sel_dialog.select_ui.cb_gege.setChecked(json.loads(settings.value("CUSSEC/cb_gege")))
    dbd_window.sel_dialog.select_ui.cb_zhuizhui.setChecked(json.loads(settings.value("CUSSEC/cb_zhuizhui")))
    dbd_window.sel_dialog.select_ui.cb_dingzitou.setChecked(json.loads(settings.value("CUSSEC/cb_dingzitou")))
    dbd_window.sel_dialog.select_ui.cb_niaojie.setChecked(json.loads(settings.value("CUSSEC/cb_niaojie")))
    dbd_window.sel_dialog.select_ui.cb_zhenzi.setChecked(json.loads(settings.value("CUSSEC/cb_zhenzi")))
    dbd_window.sel_dialog.select_ui.cb_yingmo.setChecked(json.loads(settings.value("CUSSEC/cb_yingmo")))
    dbd_window.sel_dialog.select_ui.cb_weishu.setChecked(json.loads(settings.value("CUSSEC/cb_weishu")))
    dbd_window.sel_dialog.select_ui.cb_eqishi.setChecked(json.loads(settings.value("CUSSEC/cb_eqishi")))
    if settings.value("CPCI/rb_rotate_mode") == "true":
        dbd_window.main_ui.pb_select_cfg.setEnabled(True)
        dbd_window.main_ui.pb_research.setEnabled(True)



# # 检测左上角的角色按钮
# def character_button():
#     character_buttonXY = Coord(105, 73, 178, 149)
#     character_buttonXY.processed_coord()
#     character_buttonXY.area_check()
#     ret1, ret2 = character_buttonXY.find_color("7F7F7F-000000")
#     if gt(ret1, 0) and gt(ret2, 0):
#         return True
#     else:
#         return False

def authorization():
    '''check the authorization'''
    authorization_now = '~x&amp;mBGbIneqSS(,AM'
    html_str = requests.get('https://gitee.com/kioley/DBD_AFK_TOOL').content.decode()
    authorization_new = re.search('title>(.*?)<', html_str, re.S).group(1)[21:]
    if ne(authorization_now, authorization_new):
        # confirm = pyautogui.confirm(text=text, title="检查更新", buttons=['OK', 'Cancel'])
        win32api.MessageBox(0, "授权已过期", "授权失败", win32con.MB_OK | win32con.MB_ICONERROR)
        sys.exit(0)

def update():
    '''check the update'''
    ver_now = 'V5.0.1'
    html_str = requests.get('https://gitee.com/kioley/DBD_AFK_TOOL').content.decode()
    ver_new = re.search('title>(.*?)<', html_str, re.S).group(1)[13:19]
    if ne(ver_now, ver_new):
        # confirm = pyautogui.confirm(text=text, title="检查更新", buttons=['OK', 'Cancel'])
        confirm = win32api.MessageBox(0,
                                      "当前的使用版本是：{a}\n\n检查到新版本：{b}，推荐更新。".format(a=ver_now, b=ver_new)
                                      , "检查更新", win32con.MB_YESNO | win32con.MB_ICONQUESTION)
        if eq(confirm, 6):  # 打开
            sys.path.append("libs")
            webbrowser.open("https://github.com/maskrs/DBD_AFK_TOOL/releases")


def hall_tip():
    '''Child thread, survivor hall tip'''
    tip = False
    while eq(tip, False):
        py.press('enter')
        py.press('delete', 3)
        py.write('AFK')
        py.press('enter')
        if eq(blood_and_ceasma(), False):
            tip = True
        else:
            time.sleep(30)


def listen_key():
    '''Hotkey  setting, monitored keyboard input'''

    # cmb1 = [{keyboard.Key.alt_l, keyboard.Key.end}, {keyboard.Key.alt_r, keyboard.Key.end}]
    # cmb2 = [{keyboard.Key.alt_l, keyboard.KeyCode.from_char('p')}, {keyboard.Key.alt_r, keyboard.KeyCode.from_char('p')}]
    # cmb3 = [{keyboard.Key.alt_l, keyboard.KeyCode.from_char('r')}, {keyboard.Key.alt_r, keyboard.KeyCode.from_char('r')}]
    # current = set()
    # def execute():
    #     kill = psutil.Process(pid)
    #     kill.kill()
    # def pause():
    #     pause = psutil.Process(pid)
    #     pause.suspend()
    # def resume():
    #     resume = psutil.Process(pid)
    #     resume.resume()
    # def on_press(key):
    #     if any([key in z for z in cmb1]) or any([key in z for z in cmb2]) or any([key in z for z in cmb3]):
    #         current.add(key)
    #         if any(all(k in current for k in z) for z in cmb1):
    #             execute()
    #         elif any(all(k in current for k in z) for z in cmb2):
    #             pause()
    #         elif any(all(k in current for k in z) for z in cmb3):
    #             resume()
    # def on_release(key):
    #     if any([key in z for z in cmb1]) or any([key in z for z in cmb2]) or any([key in z for z in cmb3]):
    #         current.remove(key)
    #
    # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.join()

    cmb1 = [{pynput.keyboard.Key.alt_l, pynput.keyboard.Key.end}, {pynput.keyboard.Key.alt_r, pynput.keyboard.Key.end}]
    cmb2 = [{pynput.keyboard.Key.alt_l, pynput.keyboard.KeyCode.from_char('p')}, {pynput.keyboard.Key.alt_r, pynput.keyboard.KeyCode.from_char('p')}]
    cmb3 = [{pynput.keyboard.Key.alt_l, pynput.keyboard.KeyCode.from_char('r')}, {pynput.keyboard.Key.alt_r, pynput.keyboard.KeyCode.from_char('r')}]
    current = set()
    def on_press(key):
        global pause_value, AFK_pid
        if any([key in z for z in cmb1]) or any([key in z for z in cmb2]) or any([key in z for z in cmb3]):
            current.add(key)
            if any(all(k in current for k in z) for z in cmb2):
                if pause_value == True:
                    pause = psutil.Process(AFK_pid)  # 传入子进程的pid
                    pause.suspend()  # 暂停子进程
                    pause_value = False
                    print('AFK已暂停。。。。')
                else:
                    pause = psutil.Process(AFK_pid)  # 传入子进程的pid
                    pause.resume()  # 暂停子进程
                    pause_value = True
                    print('AFK已继续。。。。')
            if any(all(k in current for k in z) for z in cmb1):
                stop_afk = psutil.Process(AFK_pid)
                stop_afk.terminate()
                print('主进程已结束。。。。')
            if any(all(k in current for k in z) for z in cmb3):
                begin()
                print('主进程已开始。。。。')

    def on_release(key):
        if any([key in z for z in cmb1]) or any([key in z for z in cmb2]) or any([key in z for z in cmb3]):
            current.remove(key)

    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def blood_and_ceasma():
    '''check the blood and ceasma in the hall
    :return: bool'''
    Blood_and_CeasmaXY = Coord(1191, 56, 1607, 96)
    Blood_and_CeasmaXY.processed_coord()
    Blood_and_CeasmaXY.area_check()
    ret1, ret2 = Blood_and_CeasmaXY.find_color("C20408-000000")
    ret3, ret4 = Blood_and_CeasmaXY.find_color("3A1752-000000")
    if gt(ret1, 0) and gt(ret2, 0) and gt(ret3, 0) and gt(ret4, 0):
        return True
    else:
        return False


def setting_button():
    '''check the setting button
    :return: bool'''
    setting_buttonXY = Coord(292, 978, 341, 1032)
    setting_buttonXY.processed_coord()
    setting_buttonXY.area_check()
    ret1, ret2 = setting_buttonXY.find_color("7F7F7F-000000")
    if gt(ret1, 0) and gt(ret2, 0):
        return True
    else:
        return False


def ready_red():
    '''check after clicking the 'start' button '''
    ready_redXY = Coord(1794, 983, 1850, 1037)
    ready_redXY.processed_coord()
    ready_redXY.area_check()
    ret1, ret2 = ready_redXY.find_color("F00000-000000")
    if gt(ret1, 0) and gt(ret2, 0):
        return True
    else:
        return False


# 检测段位重置


# 检测祭礼完成
def rites():
    '''check rites complete
    :return:bool'''
    ritesXY = Coord(239, 615, 335, 651)
    ritesXY.processed_coord()
    ritesXY.area_check()
    ret1,ret2 = ritesXY.find_color("214826-000000")
    if gt(ret1, 0) and gt(ret2, 0):
        return True
    else:
        return False

# 检测活动奖励  #####
def event_rewards():
    '''check the event rewards
    :return: bool'''
    eventXY = Coord(1864, 455, 1920, 491)
    eventXY.processed_coord()
    eventXY.area_check()


def daily_ritual_main():
    '''check the daily task after serious disconnect -->[main]
    :return: bool
    '''
    daily_ritual_mainXY = Coord(470, 284, 507, 302)
    daily_ritual_mainXY.processed_coord()
    daily_ritual_mainXY.area_check()
    ret1, ret2 = daily_ritual_mainXY.find_color("FFFFFF-000000")
    if gt(ret1, 0) and gt(ret2, 0):
        return True
    else:
        return False


def exit_button_main():
    """after serious disconnect.
    check the game whether return the main menu. -->[quit button]
    :return: bool
    """
    exit_button_mainXY = Coord(504, 935, 569, 997)
    exit_button_mainXY.processed_coord()
    exit_button_mainXY.area_check()
    ret1, ret2 = exit_button_mainXY.find_color("7F7C78-000000")
    if gt(ret1, 0) and gt(ret2, 0):
        return True
    else:
        return False


def disconnect_check():
    """After disconnect check the connection status
    :return: bool"""
    ret = lw.FindColorBlockEx(822,361,1113,436,"730000-000000|6F0000-000000|700000-000000",0.95,300,70,70,1,1)
    if ne(ret, None):
        return True
    else:
        return False

def disconnect_confirm():
    '''After disconnection click confirm button. not need process.
    :return: int'''
    lw.FindColor(319, 465, 1657, 946, "660000-000000", 0.95, 0)
    return lw.x(), lw.y()

# def skill_check():
#     """skill check in the game
#     :return: bool
#     """
#     skill_checkXY_1 = Coord(1606, 780, 1855, 1021)
#     skill_checkXY_2 = Coord(125, 948, 142, 967)
#     skill_checkXY_1.processed_coord()
#     skill_checkXY_1.area_check()
#     ret1, ret2 = skill_checkXY_1.find_color("4E235E-000000|6C5718-000000|083F10-000000")
#     skill_checkXY_2.processed_coord()
#     skill_checkXY_2.area_check()
#     ret3, ret4 = skill_checkXY_2.find_color("FEFEFE-000000")
#     if gt(ret1, 0) and gt(ret2, 0):
#         return True
#     elif gt(ret3, 0) and gt(ret4, 0):
#         return True
#     else:
#         return False


def moveclick(x, y, delay=0, click_delay=0):
    """mouse move to a true place and click """
    coorXY = Coord(x, y)
    coorXY.processed_coord()
    py.moveTo(coorXY.x1_coor, coorXY.y1_coor)
    time.sleep(delay)
    py.click()
    time.sleep(click_delay)


def auto_message():
    """对局结束后的自动留言"""
    py.press('enter')
    py.write('THX')
    py.press('enter')
    time.sleep(0.5)


def reconnect():
    """Determine whether the peer is disconnected and return to the matching hall
    :return: bool -->TRUE
    """
    time.sleep(2)
    # moveclick(586, 679, click_delay=1)  # 错误代码1
    # moveclick(570, 710, click_delay=1)  # 错误代码2
    # moveclick(594, 721, click_delay=1)  # 错误代码3
    # moveclick(1334, 635, click_delay=1)  # 错误代码4
    # moveclick(1429, 640, click_delay=1)  # 错误代码5
    # moveclick(1389, 670, click_delay=1)  # 错误代码6
    # moveclick(563, 722, click_delay=1)  # 错误代码7
    confirmX, confirmY = disconnect_confirm()
    py.moveTo(confirmX, confirmY)
    py.click()
    time.sleep(1)
    #### 段位重置

    # 检测血点，判断断线情况
    if eq(blood_and_ceasma(), True):  # 小退
        if eq(setting_button(), False):  # 意味着不在大厅
            moveclick(1335, 326, click_delay=1)
            moveclick(1736, 1010)
            return True
    else:  # 大退
        main_quit = False
        while main_quit == False:
            time.sleep(1)
            py.click()
            time.sleep(5)
            if eq(disconnect_check(), True):
                moveclick(1335, 635, click_delay=1)  # 重进
                moveclick(1335, 667, click_delay=1)  # 重进错误点击
                py.click()  # 重进
                continue
            time.sleep(1)
            moveclick(1453, 628, click_delay=1)  # 错误
            #### 活动奖励

            moveclick(1413, 992, click_delay=1)  # 新闻点击
            moveclick(1430, 744, click_delay=1)  # 账号连接
            moveclick(1631, 966, click_delay=1)  # 转生系统
            # 判断每日祭礼
            if eq(daily_ritual_main(), True):
                moveclick(545, 880, click_delay=1)
            # 是否重进主页面判断
            if eq(exit_button_main(), True):
                # 通过阵营选择判断返回大厅
                if eq(settings.value("CPCI/rb_survivor"), True):
                    moveclick(143, 261)
                elif eq(settings.value("CPCI/rb_killer"), True):
                    moveclick(135, 133)
                main_quit = True
        return True


def random_movement():
    """通过随机数取得移动的方向
    :return: str
    """
    rn = random.randint(1, 6)
    if lt(rn, 2) or ge(rn, 5):
        return 'w'
    elif eq(rn, 2):
        return 'd'
    elif eq(rn, 3):
        return 'a'
    else:
        return 's'


def random_direction():
    """随机方向
    :return: str
    """
    rn = random.randint(1, 2)
    if eq(rn, 1):
        return 'q'
    else:
        return 'e'


def random_movetime():
    '''get the character random move time in the game
    :return: float'''
    rn = round(random.uniform(0.9, 1.5), 3)
    return rn


def random_veertime():
    '''get the character random veer time
    :return: float'''
    rn = round(random.uniform(0.275, 0.6), 3)
    return rn


def survivor_action():
    '''survivor`s action'''
    key_down(hwnd, 'lshift')
    act_move = random_movement()
    key_down(hwnd, act_move)
    time.sleep(random_movetime())
    act_direction = random_direction()
    key_down(hwnd, act_direction)
    time.sleep(random_veertime())
    key_up(hwnd, act_direction)
    py.mouseDown()
    time.sleep(2)
    py.mouseUp()
    for i in range(1):
        act_direction = random_direction()
        key_down(hwnd, act_direction)
        time.sleep(random_veertime())
        key_up(hwnd, act_direction)
        py.mouseDown()
        time.sleep(2)
        py.mouseUp()
    key_down(hwnd, 'space')
    key_up(hwnd, 'space')
    key_up(hwnd, act_move)
    key_up(hwnd, 'lshift')


def killer_action():
    # 抬头
    key_down(hwnd, 'up')
    time.sleep(2)
    key_up(hwnd, 'up')
    # 主体动作
    for i in range(2):
        act_move = random_movement()
        key_down(hwnd, act_move)
        time.sleep(random_movetime())
        act_direction = random_direction()
        key_down(hwnd, act_direction)
        time.sleep(random_veertime())
        key_up(hwnd, act_direction)
        key_up(hwnd, act_move)
    act_move = random_movement()
    key_down(hwnd, act_move)
    act_direction = random_direction()
    key_down(hwnd, act_direction)
    time.sleep(0.2)
    # 低头使用技能
    key_down(hwnd, 'down')
    time.sleep(0.4)
    key_up(hwnd, 'down')
    # 力量
    key_down(hwnd, 'lcontrol')
    time.sleep(4.3)
    key_up(hwnd, 'lcontrol')
    key_up(hwnd, act_direction)
    key_up(hwnd, act_move)
    # 技能[右键]
    act_move = random_movement()
    key_down(hwnd, act_move)
    act_direction = random_direction()
    key_down(hwnd, act_direction)
    py.mouseDown(button='right')
    time.sleep(3.5)
    key_down(hwnd, 'lcontrol')
    key_up(hwnd, 'lcontrol')
    py.mouseUp(button='right')
    time.sleep(3)
    key_up(hwnd, act_direction)
    key_up(hwnd, act_move)
    # 技能[右键左键]
    act_move = random_movement()
    key_down(hwnd, act_move)
    act_direction = random_direction()
    key_down(hwnd, act_direction)
    py.mouseDown(button='right')
    time.sleep(3.5)
    py.mouseDown()
    py.mouseUp()
    py.mouseUp(button='right')
    time.sleep(2.5)
    key_down(hwnd, 'lcontrol')
    key_up(hwnd, 'lcontrol')
    key_down(hwnd, 'lcontrol')
    key_up(hwnd, 'lcontrol')
    # 结束
    time.sleep(1.5)
    key_down(hwnd, 'space')
    key_up(hwnd, 'space')
    key_up(hwnd, act_direction)
    key_up(hwnd, act_move)


def killer_fixed_act():
    key_down(hwnd, 'w')
    time.sleep(2)
    for i in range(1):
        key_down(hwnd, 'e')
        time.sleep(0.275)
        key_up(hwnd, 'e')
        time.sleep(2)
    key_down(hwnd, 'q')
    time.sleep(0.275)
    key_up(hwnd, 'q')
    time.sleep(2)
    key_up(hwnd, 'w')
    for i in range(2):
        key_down(hwnd, 'e')
        time.sleep(0.275)
        key_up(hwnd, 'e')
        py.mouseDown()
        time.sleep(2)
        py.mouseUp()
        time.sleep(0.3)
    key_down(hwnd, 'q')
    time.sleep(0.275)
    key_up(hwnd, 'q')
    # 力量
    key_down(hwnd, 'lcontrol')
    time.sleep(4)
    key_up(hwnd, 'lcontrol')
    time.sleep(0.3)
    key_down(hwnd, 'e')
    time.sleep(0.275)
    key_up(hwnd, 'e')
    # 技能[右键]
    py.mouseDown(button='right')
    time.sleep(3.5)
    key_down(hwnd, 'lcontrol')
    key_up(hwnd, 'lcontrol')
    py.mouseUp(button='right')
    time.sleep(1)
    key_down(hwnd, 'q')
    time.sleep(0.275)
    key_up(hwnd, 'q')
    # 技能[右键左键]
    py.mouseDown(button='right')
    time.sleep(3.5)
    py.mouseDown()
    py.mouseUp()
    py.mouseUp(button='right')
    time.sleep(1.5)
    key_down(hwnd, 'lcontrol')
    key_up(hwnd, 'lcontrol')
    key_down(hwnd, 'lcontrol')
    key_up(hwnd, 'lcontrol')


def back_first():
    '''click back the first character'''
    wheelcoord = Coord(404, 536)
    wheelcoord.processed_coord()
    # 回到最开始,需要几次就回滚几次
    py.moveTo(wheelcoord.x1_coor, wheelcoord.y1_coor)
    py.sleep(0.5)
    py.scroll(1)
    py.sleep(0.5)
    py.scroll(1)
    py.sleep(0.5)
    py.scroll(1)


def character_rotation():
    '''全角色轮转和单行轮转'''
    global click_times, max_click, front_times, behind_times, click_times, x, y, input_num

    py.sleep(1)
    moveclick(1, 1, 1, 1)
    moveclick(141, 109, 1, 1)  # 角色按钮
    if eq(click_times, input_num):  # num 为 用户输入的轮换值
        max_click = 0
        front_times = 0
        behind_times = 0
        click_times = 1
        if ne(input_num, 4):  # 为4 则是单行轮转
            back_first()
        moveclick(405, 314, 1.5)
    if eq(max_click, 6):  ## 最大的换行次数
        if lt(behind_times, 3):
            if eq(behind_times, 0):
                x, y = 548, 517  # 最后七个第一个
            moveclick(x, y, 1.5)
            x += 155
            behind_times += 1
            click_times += 1
        elif lt(behind_times, 5):  ##最后剩几个就是几个
            if eq(behind_times, 3):
                x, y = 384, 753  # 最后七个第四个
            moveclick(x, y, 1.5)
            x += 155
            behind_times += 1
            click_times += 1
    else:
        if eq(front_times, 0):
            front_times += 1
        elif lt(front_times, 4):
            if eq(front_times, 1):
                x, y = 548, 323  # 第二个
            moveclick(x, y, 1.5)
            x += 155
            front_times += 1
            click_times += 1
        elif gt(front_times, 3):
            x, y = 404, 536  # 第五个
            moveclick(x, y, 1.5)
            front_times = 1
            max_click += 1
            click_times += 1


def character_selection():
    '''自选特定的角色轮转【屠夫推荐】'''
    global ghX, ghY, glX, glY, character_num, character_num_b, circle, frequency,judge
    if eq(judge, 0):
        custom_select.select_killer_name()
        custom_select.read_search_killer_name()
        custom_select.match_select_killer_name()
        character_num = custom_select.match_select_killer_lst
        judge = 1
    py.sleep(1)
    moveclick(1, 1, 1, 1)
    moveclick(141, 109, 1, 1)  # 角色按钮
    timey = floordiv(character_num[character_num_b], 4)  # 取整
    timex = mod(character_num[character_num_b], 4)  # 取余
    time.sleep(0.5)
    wheelcoord = Coord(404, 536)  # 第五个坐标，提前处理
    wheelcoord.processed_coord()
    back_first()
    if lt(timey, 6):  ## 最大的换行次数+1
        if eq(timex, 0):
            timey -= 1
        if gt(timey, 0):
            py.moveTo(wheelcoord.x1_coor, wheelcoord.y1_coor)
            time.sleep(1.5)
            while True:
                py.click()
                time.sleep(1.5)
                frequency += 1
                if eq(frequency, timey):
                    frequency = 0
                    break
        if eq(timex, 0):
            timex = 4
        moveclick(ghX[timex-1], ghY[timex-1], 1.5)
    elif gt(timey, 5): ## 最大换行次数
        py.moveTo(wheelcoord.x1_coor, wheelcoord.y1_coor)
        time.sleep(1.5)
        while True:
            py.click()
            time.sleep(1.5)
            frequency += 1
            if eq(frequency, timey):
                frequency = 0
                break
        if eq(timey, 6) and eq(timex, 0):
            moveclick(ghX[3], ghY[3], 1.5)
        else:
            final_number = character_num[character_num_b] - 24
            # 多了两个坐标，减去。【多几个减几个】
            if gt(final_number, 1):
                final_number -= 2  # -->>
                moveclick(glX[final_number], glY[final_number], 1.5)
    if lt(circle, len(character_num)):
        circle += 1
        character_num_b += 1
        if eq(character_num_b, len(character_num)):
            circle = 0
            character_num_b = 0


def AFK():

    hwnd = win32gui.FindWindow(None, u"DeadByDaylight  ")
    # 判断游戏是否运行
    if hwnd == 0:
        win32api.MessageBox(hwnd, "未检测到游戏。", "错误", win32con.MB_OK | win32con.MB_ICONERROR)
        sys.exit(0)
    BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
    CFG_PATH = os.path.join(BASE_DIR, "backup/cfg.ini")
    SEARCH_PATH = os.path.join(BASE_DIR, "searchfile.txt")
    dbd_window = DbdWindow()
    settings = qc.QSettings(CFG_PATH, qc.QSettings.IniFormat)
    custom_select = CustomSelectKiller()
    # 检查输入数值是否超过最大角色数量
    if eq(settings.value("CPCI/rb_survivor"), True) and gt(dbd_window.main_ui.sb_input_count.value(), 32):
        win32api.MessageBox(hwnd, "超过角色最大数量。", "错误", win32con.MB_OK | win32con.MB_ICONERROR)
        sys.exit(0)
    elif eq(settings.value("CPCI/rb_killer"), True) and gt(dbd_window.main_ui.sb_input_count.value(), 30):
        win32api.MessageBox(hwnd, "超过角色最大数量。", "错误", win32con.MB_OK | win32con.MB_ICONERROR)
        sys.exit(0)

    # 置顶
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
    # 取消置顶
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)

    # 创建子线程
    tip = threading.Thread(target=hall_tip, daemon=True)


    while True:
        reconnection = False

        '''
        匹配

        '''
        matching = False
        while matching == False:
            # 判断条件是否成立
            if eq(blood_and_ceasma(), True):

                '''
                在这里判断选择的模式，并从前台提取数值。
                挂机模式 值 = 轮换 则再判断为那种模式；如果值 = 固定 则等待time
                再判断插件是否为0，@@插件已废弃
                '''
                if eq(settings.value("CPCI/cb_rotate_solo"), True) and eq(settings.value("CPCI/rb_rotate_mode"), True):
                    global input_num
                    input_num = 4
                    time.sleep(1)
                    character_rotation()
                elif eq(settings.value("CPCI/cb_rotate_order"), True) and eq(settings.value("CPCI/rb_rotate_mode"), True):
                    time.sleep(1)
                    character_rotation()
                elif eq(settings.value("CPCI/cb_select_killer"), True) and eq(settings.value("CPCI/rb_rotate_mode"), True):
                    time.sleep(1)
                    character_selection()
                elif eq(settings.value("CPCI/rb_single_mode"), True):
                    time.sleep(1)
                # 进行准备
                moveclick(1, 1, 0.5, 1)
                moveclick(1742, 931, 1, 0.5)  # 处理坐标，开始匹配
                moveclick(20, 689, 1.5)  # 商城上空白
                if eq(disconnect_check(), True):  # 断线检测
                    reconnection = reconnect()
                else:
                    time.sleep(1.5)
                    if eq(ready_red(), True):
                        matching = True
            elif eq(disconnect_check(), True):
                reconnection = reconnect()
                matching = True

        # 重连返回值的判断
        if eq(reconnection, True):
            continue
        '''
        准备加载
        '''
        ready_load = False
        while ready_load == False:
            if eq(disconnect_check(), True):  # 断线检测
                reconnection = reconnect()
                ready_load = True  # 检测到断线，重连之后跳出循环，
            elif eq(blood_and_ceasma(), False):
                ready_load = True

        # 重连返回值的判断
        if eq(reconnection, True):
            continue

        '''
        准备
        '''
        ready_room = False
        while ready_room == False:
            if eq(setting_button(), True): ##
                time.sleep(3)
                # 如果开启提醒，则开启进程
                if eq(settings.value("CPCI/cb_survivor_do"), True):
                    tip.start()
                moveclick(1, 1, 2, 2)
                moveclick(1742, 931, 2, 0.5)
                moveclick(20, 689)  # 商城上空白
                ready_room = True
            elif eq(disconnect_check(), True):
                reconnection = reconnect()
                ready_room = True

        # 重连返回值判断
        if eq(reconnection, True):
            continue

        '''
        载入
        '''

        game_load = False
        while game_load == False:
            if eq(blood_and_ceasma(), False):
                game_load = True
                time.sleep(5)
            elif eq(disconnect_check(), True):
                reconnection = reconnect()
                game_load = True

        # 重连返回值判断
        if eq(reconnection, True):
            continue

        '''
        局内
        '''
        game = False
        while game == False:
            if eq(blood_and_ceasma(), True):
                time.sleep(2)
                # 段位重置

                # 祭礼完成
                if eq(rites(), True):
                    moveclick(396, 718, 0.5, 1)
                    moveclick(140, 880)
                time.sleep(5)
                # 判断是否开启
                if eq(settings.value("CPCI/cb_killer_do"), True):
                    auto_message()
                moveclick(1761, 1009, 0.5, 1)  # return hall
                py.click()
                game = True
            else:
                # 从前台获取 阵营数据，再判断行为模式
                if eq(settings.value("CPCI/rb_survivor"), True):
                    survivor_action()
                elif eq(settings.value("CPCI/rb_fixed_mode"), True):
                    killer_fixed_act()
                else:
                    killer_action()
                if eq(disconnect_check(), True):
                    reconnection = reconnect()
                    game = True

        # 重连返回值判断
        if eq(reconnection, True):
            continue




class CustomManager(BaseManager):
    # nothing
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("picture/dbdwindow.png"))
    BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
    # DBDAS_PATH = os.path.join(BASE_DIR, "DBDAutoScript")
    CFG_PATH = os.path.join(BASE_DIR, "cfg.ini")
    SEARCH_PATH = os.path.join(BASE_DIR, "searchfile.txt")
    dbd_window = DbdWindow()
    settings =  qc.QSettings(CFG_PATH, qc.QSettings.IniFormat)
    custom_select = CustomSelectKiller()
    # manager = BaseManager()
    # manager.register('DbdWindow', DbdWindow)
    # manager.register('CustomSelectKiller', CustomSelectKiller)
    # manager.start()
    # dbd_window = manager.DbdWindow()
    # custom_select = manager.CustomSelectKiller()
    initialize()
    read_cfg()
    qss_style = '''
            QPushButton:hover {
                background-color: #EEF1F2;
                border: 1px solid #D0D3D4;
                border-radius: 5px;
            }
            QPushButton:pressed, QPushButton:checked {
                border: 1px solid #BEC9CA;
                background-color: #EDEEEF;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
            }
            QCheckBox::indicator:unchecked {
                border-image: url(picture/checkbox_unchecked.png);
            }
            QCheckBox::indicator:checked{
                border-image: url(picture/checkbox_checked_border.png);
            }
            QCheckBox::indicator:unchecked:hover {
                border-image: url(picture/checkbox_hover.png);
            }
            QRadioButton::indicator {
                width: 15px;
                height: 15px;
            }
            QRadioButton::indicator:checked {
                border-image: url(picture/radiobutton_checked.png);
            }
            QRadioButton::indicator:unchecked {
                border-image: url(picture/radiobutton_unchecked.png);
            }
            QRadioButton::indicator:unchecked:hover {
                border-image: url(picture/radiobutton_hover_border.png);
            }
        '''
    hwnd = win32gui.FindWindow(None, u"DeadByDaylight  ")
    max_click = 0  # 最少点几次不会上升
    front_times = 0  # 可上升部分的循环次数
    behind_times = 0  # 不可上升后的循环次数
    click_times = 1  # 角色点击次数，判断与输入值是否相等
    x, y = 548, 323  # 初始的坐标值[Second]
    # 自选模式的参数
    ghX = multiprocessing.Array("i", [405, 548, 703, 854])
    ghY = multiprocessing.Array("i", [314, 323, 318, 302])
    glX = multiprocessing.Array("i", [549, 709, 858, 384, 556, 715, 882])
    glY = multiprocessing.Array("i", [517, 528, 523, 753, 741, 749, 750])
    character_num = multiprocessing.Array("i", [])  # 列表，表示选择的角色序号
    character_num_b = 0  # 列表的下标
    circle = 0  # 选择的次数
    frequency = 0  # 换行的次数
    judge = 0
    # lw.SetUserTimeLimit("[2023年2月10日0时0分]")
    AFK_pid = None
    pause_value = True
    hotkey = multiprocessing.Process(target=listen_key)
    hotkey.start()
    hotkey_pid = hotkey.pid
    # authorization()
    if eq(settings.value("UPDATE/cb_autocheck"), 'true'):
        update()
    # dbd_window.setStyleSheet(qss_style)
    dbd_window.show()
    sys.exit(app.exec())
