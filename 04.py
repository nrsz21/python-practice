import tkinter as tk

from tkinter import messagebox
import json
#
#
#
class todo_list:

    def __init__(self):
        try:
            with open('todo.json','r',encoding='utf-8') as f:
                self.todolist = json.load(f)
        except FileNotFoundError:#文件还不存在
            self.todolist = {}
        self.root = tk.Tk()
        self.root.geometry('300x500')
        self.root.title('待办事项清单')
        self.labeltitle = tk.Label(self.root,text='以下是待办清单')
        self.listbox = tk.Listbox(self.root)
        self.entry = tk.Entry(self.root)
        self.adButton = tk.Button(self.root, text='添加', command=self.add)
        self.delButton = tk.Button(self.root, text='删除', command=self.delt)
        self.comButton = tk.Button(self.root,text='完成',command = self.complete)
        self.labeltitle.pack(pady=5,padx=8)
        self.entry.pack()
        self.refresh()
        self.listbox.pack()
        self.adButton.pack(pady=5)
        self.delButton.pack(pady=5)
        self.comButton.pack()
        self.root.mainloop()

    def add(self):
        val = self.entry.get().strip()
        if val:
            if val in self.todolist:#键存在
                messagebox.showinfo('提示','清单已有该事项')
            else:
                self.todolist[val] = False
                self.refresh()
            self.entry.delete(0,tk.END)#清楚输入框的内容
        else:
            return
        self.save()
    def delt(self):
        # 获取索引选中的事件
        select_index = self.listbox.curselection()#获取 Listbox 被选中的项，返回元组(2,0)
        if not select_index:
            return
        idx = select_index[0]#获取select_index的第一个值
        text = self.listbox.get(idx)#从界面取到事项名
        val = text[2:] if text.startswith('√ ') else text
        del self.todolist[val]#从字典中删除掉数据
        self.listbox.delete(idx)#从界面删掉显示
        self.save()
    def complete(self):
        select_index = self.listbox.curselection()
        if not select_index:
            return
        idx = select_index[0]
        text = self.listbox.get(idx)
        val = text[2:] if text.startswith('√ ') else text#切割字符
        self.todolist[val] = not self.todolist[val]
        self.refresh()
        self.save()
    def refresh(self):#刷新整个清单
        self.listbox.delete(0,tk.END)
        for item,done in self.todolist.items():
            text = ('√ 'if done else '') + item
            self.listbox.insert(tk.END,text)

    def save(self):
        with open('todo.json','w',encoding='utf-8') as f:
            json.dump(self.todolist,f,ensure_ascii=False)
if __name__ == '__main__':
    todo_list()

