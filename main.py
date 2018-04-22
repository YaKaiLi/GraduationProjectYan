# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.messagebox
import os

class MainWindow:

    def buttonListener1(self, event):
        os.system("python3 ReptilePart/getListOfJournal/getListOfJournalOne.py")
        os.system("python3 ReptilePart/getListOfJournal/getListOfJournalTwo.py")
        os.system("python3 ReptilePart/getListOfJournal/getListOfJournalThree.py")
        os.system("python3 ReptilePart/getListOfJournal/getListOfJournalFour.py")
        os.system("python3 ReptilePart/getListOfJournal/getListOfJournalFive.py")
        os.system("python3 ReptilePart/getListOfJournal/getListOfJournalSix.py")
        tkinter.messagebox.showinfo("获取期刊列表", "获取期刊列表成功")

    def buttonListener2(self, event):
        os.system("python3 ReptilePart/getBaiduSInfo/getBaiduSInfo.py")
        tkinter.messagebox.showinfo("获取期刊信息", "获取期刊信息成功")

    def buttonListener3(self, event):
        os.system("python3 PCAanalysis/PCAanalysis.py")
        tkinter.messagebox.showinfo("开始评估", "开始评估成功")

    def buttonListener4(self, event):
        tkinter.messagebox.showinfo("展示评估结果", "展示评估结果")

    def __init__(self):
        self.frame = Tk()
        self.frame.title('期刊评估系统')

        self.button1 = Button(self.frame, text="获取期刊列表", width=100, height=5)
        self.button2 = Button(self.frame, text="获取期刊信息", width=100, height=5)
        self.button3 = Button(self.frame, text="开始评估", width=100, height=5)
        self.button4 = Button(self.frame, text="展示评估结果", width=100, height=5)

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