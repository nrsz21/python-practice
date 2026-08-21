import tkinter as tk
from tkinter import messagebox
# from flask import Flask
#
#
#
class todo_list:

    def __init__(self):

        self.todolist = {}
        self.root = tk.Tk()
        self.root.geometry('300x500')
        self.root.title('待办事项清单')
        self.labeltitle = tk.Label(self.root,text='以下是待办清单')
        self.listbox = tk.Listbox(self.root)
        self.entry = tk.Entry(self.root)
        self.adButton = tk.Button(self.root, text='添加', command=self.add)
        self.delButton = tk.Button(self.root, text='删除', command=self.delt)
        self.labeltitle.pack(pady=5,padx=8)
        self.entry.pack()
        for item in self.todolist:
            self.listbox.insert(tk.END, item)#将列表里的内容插入到Listbox里面
        self.listbox.pack()
        self.adButton.pack(pady=5)
        self.delButton.pack(pady=5)
        self.root.mainloop()

    def add(self):
        val = self.entry.get()
        if val:
            if val in self.todolist:#键存在
                messagebox.showinfo('提示','清单已有该事项')
            else:
                self.todolist[val] = False
                self.listbox.insert(tk.END,val)
            self.entry.delete(0,tk.END)#清楚输入框的内容
        else:
            return
    def delt(self):
        # 获取索引选中的事件
        select_index = self.listbox.curselection()
        if not select_index:
            return
        idx = select_index[0]#
        val = self.listbox.get(idx)#从界面取到事项名
        del self.todolist[val]#从字典中删除掉数据
        self.listbox.delete(idx)#从界面删掉显示

if __name__ == '__main__':
    todo_list()

