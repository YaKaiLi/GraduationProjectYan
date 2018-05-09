from tkinter import *


class MainWindow:
    def __init__(self):
        self.frame = Tk()

        self.menu_button = Button(self.frame,text="期刊类别", width=30,height = 5)
        self.one_button = Button(self.frame, text="爬虫获取期刊列表", width=30,height = 5)
        self.two_button = Button(self.frame, text="获取期刊信息", width=30,height = 5)
        self.three_button = Button(self.frame, text="开始评估", width=30,height = 5)
        self.four_button = Button(self.frame, text="结果展示", width=30,height = 5)

        self.menu_button.grid(row=0, column=2)
        self.one_button.grid(row=1, column=0)
        self.two_button.grid(row=1, column=1)
        self.three_button.grid(row=1, column=3)
        self.four_button.grid(row=1, column=4)

        self.one_text = Text(self.frame, height="20", width=30)
        self.two_text = Text(self.frame, height="20", width=30)
        self.three_text = Text(self.frame, height="20", width=30)
        self.four_text = Text(self.frame, height="20", width=30)

        self.one_text.grid(row=2, column=0)
        self.two_text.grid(row=2, column=1)
        self.three_text.grid(row=2, column=3)
        self.four_text.grid(row=2, column=4)

        self.frame.mainloop()


frame = MainWindow()