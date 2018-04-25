# -*- coding: cp936 -*-
from tkinter import *
root = Tk()

menubar = Menu(root)
vLang = StringVar()
#每次打印出当前选中的语言
def printItem():
    print ('vLang = ',vLang.get())
filemenu = Menu(menubar,tearoff = 0)
for k in ['哲学','教育学','经济学','法学','军事学','文学','艺术学','信息工程']:
    #绑定变量与回调函数，指定的变量vLang将这几项划为一组
    filemenu.add_radiobutton(label = k,command = printItem,variable = vLang)
#将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label = '期刊类别',menu = filemenu)
root['menu'] = menubar
root.mainloop()