from tkinter import *


def main():
    root = Tk()
    menu_button = Button(root, text="期刊类别", width=30, height=5)
    one_button = Button(root, text="爬虫获取期刊列表", width=30, height=5)
    two_button = Button(root, text="获取期刊信息", width=30, height=5)
    three_button = Button(root, text="开始评估", width=30, height=5)
    four_button = Button(root, text="结果展示", width=30, height=5)

    menu_button.grid(row=0, column=2)
    one_button.grid(row=1, column=0)
    two_button.grid(row=1, column=1)
    three_button.grid(row=1, column=3)
    four_button.grid(row=1, column=4)

    one_text = Text(root, height="20", width=30)
    two_text = Text(root, height="20", width=30)
    three_text = Text(root, height="20", width=30)
    four_text = Text(root, height="20", width=30)

    one_text.grid(row=2, column=0)
    two_text.grid(row=2, column=1)
    three_text.grid(row=2, column=3)
    four_text.grid(row=2, column=4)

    root.mainloop()


if __name__ == '__main__':
    main()