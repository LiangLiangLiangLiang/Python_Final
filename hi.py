from tkinter import *
my_window = Tk()
my_window.title('遊戲')
my_window.geometry('800x400')

label_var = StringVar()
label_var.set('新生進入台大，發現這學校少了校長，於是要展開一連串旅程來找到管中閔。')

my_label = Label(my_window, textvariable = label_var, width = 80, bg = 'yellow')
my_label.pack()

alist = ["b","c","d"]
def click_next1():
    try:
        label_var.set(alist[0])
        alist.pop(0)
    except IndexError as index_error:
        label_var.set("Game Over!")

blist = ["e","f","g"]
def click_next2():
    try:
        label_var.set(blist[0])
        blist.pop(0)
    except IndexError as index_error:
        label_var.set("Game Over!")

clist = ["h","j","k"]
def click_next3():
    try:
        label_var.set(clist[0])
        clist.pop(0)
    except IndexError as index_error:
        label_var.set("Game Over!")

label_var1 = StringVar()
label_var1.set("使用")
my_button1 = Button(my_window, textvariable = label_var1, command = click_next1)
my_button1.pack()

label_var2 = StringVar()
label_var2.set("移動至")
my_button2 = Button(my_window, textvariable = label_var2, command = click_next2)
my_button2.pack()

label_var3 = StringVar()
label_var3.set("查看")
my_button3 = Button(my_window, textvariable = label_var3, command = click_next3)
my_button3.pack()

my_window.mainloop()

class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)        
        tk.Button(self, text="綜合大樓").pack()
        tk.Button(self, text="社科院").pack()
        tk.Button(self, text="水源宿舍").pack()
        tk.Button(self, text="心輔中心").pack()
        tk.Button(self, text="行政大樓").pack()
        tk.Button(self, text="公車站").pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()
