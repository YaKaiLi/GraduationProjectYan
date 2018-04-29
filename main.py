# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.messagebox
import os

class MainWindow:

    def buttonListener1(self, event):
        os.system("python3 deleteAllData.py")
        os.system("python3 "+self.jClass+"/getListOfJournal.py")
        tkinter.messagebox.showinfo("获取期刊列表", "获取期刊列表完毕")

    def buttonListener2(self, event):
        os.system("python3 getBaiduSInfo.py")
        tkinter.messagebox.showinfo("获取期刊信息", "获取期刊信息完毕")

    def buttonListener3(self, event):
        os.system("python3 PCAanalysis.py")
        tkinter.messagebox.showinfo("开始评估", "评估完毕")

    def buttonListener4(self, event):
        os.system("python3 resultGui.py")

    def __init__(self):
        self.frame = Tk()

        ###菜单栏开始
        self.menubar = Menu(self.frame)
        vLang = StringVar()
        self.jClass = "zhexue"
        # 每次打印出当前选中的语言
        def printItem():
            if vLang.get() == "哲学":
                self.jClass = "zhexue"
            elif vLang.get() == "教育学":
                self.jClass = "jiaoyuxue"
            elif vLang.get() == "经济学":
                self.jClass = "jingjixue"
            elif vLang.get() == "法学":
                self.jClass = "faxue"
            elif vLang.get() == "军事学":
                self.jClass = "junshixue"
            elif vLang.get() == "文学":
                self.jClass = "wenxue"
            elif vLang.get() == "艺术学":
                self.jClass = "yishuxue"
            elif vLang.get() == "信息工程":
                self.jClass = "xinxigongcheng"
            else:
                self.jClass = "zhexue"
            print(vLang.get())
        filemenu = Menu(self.menubar, tearoff=0)
        for k in ['哲学', '教育学', '经济学', '法学', '军事学', '文学', '艺术学', '信息工程']:
            # 绑定变量与回调函数，指定的变量vLang将这几项划为一组
            filemenu.add_radiobutton(label=k, command=printItem, variable=vLang)
        # 将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
        self.menubar.add_cascade(label='期刊类别', menu=filemenu)
        self.frame['menu'] = self.menubar
        ###菜单栏结束


        self.frame.title('期刊评估系统')

        self.button1 = Button(self.frame, text="获取期刊列表", width=50, height=5)
        self.button2 = Button(self.frame, text="获取期刊信息", width=50, height=5)
        self.button3 = Button(self.frame, text="开始评估", width=50, height=5)
        self.button4 = Button(self.frame, text="展示评估结果", width=50, height=5)

        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=0, padx=5, pady=5)
        self.button3.grid(row=2, column=0, padx=5, pady=5)
        self.button4.grid(row=3, column=0, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>",self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
        self.button3.bind("<ButtonRelease-1>",self.buttonListener3)
        self.button4.bind("<ButtonRelease-1>",self.buttonListener4)

        self.frame.mainloop()


window = MainWindow()