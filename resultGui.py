# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.messagebox
import os

class MainWindow:

    def buttonListener1(self, event):
        os.system("python3 resultGui/showTheList.py")

    def buttonListener2(self, event):
        os.system("python3 resultGui/showValueLineChart.py")

    def buttonListener3(self, event):
        os.system("python3 resultGui/showAllLineChart.py")

    def __init__(self):
        self.frame = Tk()
        self.frame.title('评估结果展示')

        self.button1 = Button(self.frame, text="显示期刊评估列表", width=35, height=3)
        self.button2 = Button(self.frame, text="显示期刊评估折线图", width=35, height=3)
        self.button3 = Button(self.frame, text="显示期刊评估指标折线图", width=35, height=3)

        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=0, padx=5, pady=5)
        self.button3.grid(row=2, column=0, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>",self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
        self.button3.bind("<ButtonRelease-1>",self.buttonListener3)

        self.frame.mainloop()


window = MainWindow()