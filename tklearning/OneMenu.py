# -*- coding: cp936 -*-
from tkinter import *
root = Tk()

menubar = Menu(root)
vLang = StringVar()
#ÿ�δ�ӡ����ǰѡ�е�����
def printItem():
    print ('vLang = ',vLang.get())
filemenu = Menu(menubar,tearoff = 0)
for k in ['��ѧ','����ѧ','����ѧ','��ѧ','����ѧ','��ѧ','����ѧ','��Ϣ����']:
    #�󶨱�����ص�������ָ���ı���vLang���⼸�Ϊһ��
    filemenu.add_radiobutton(label = k,command = printItem,variable = vLang)
#��menubar��menu����ָ��Ϊfilemenu����filemenuΪmenubar�������˵�
menubar.add_cascade(label = '�ڿ����',menu = filemenu)
root['menu'] = menubar
root.mainloop()