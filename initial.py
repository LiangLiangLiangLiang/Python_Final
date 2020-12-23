import tkinter as tk
from tkinter import messagebox


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Campus)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Campus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="台大校園", font=('Helvetica', 20, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Campus_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Campus_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Campus_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Campus_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")


class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="綜合大樓",command=lambda: master.switch_frame(Multi)).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="水源宿舍",command=lambda: master.switch_frame(Dorm)).grid(row=0, column=2, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="社科院",command=lambda: master.switch_frame(Social_Science)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="行政大樓",command=lambda: master.switch_frame(Administration)).grid(row=1, column=2, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="心輔中心",command=lambda: master.switch_frame(Counsel)).grid(row=2, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="公車站",command=lambda: master.switch_frame(Bus)).grid(row=2, column=2, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=3, column=0, columnspan=4, sticky="n"+"e"+"s"+"w")


class Multi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="綜合大樓", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Multi_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Multi_Move1)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Multi_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Multi_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

# 從這裡開始都是討論室的部分
class Multi_Move1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="販賣機", command=lambda: master.switch_frame(Multi_sale)).pack()
        tk.Button(self, text="綜合大講堂", command=lambda: master.switch_frame(Multi_Audi)).pack()
        tk.Button(self, text="討論室", command=lambda: master.switch_frame(Multi_conver)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi)).pack()


class Multi_sale(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="販賣機", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="請輸入商品代碼", font=('Helvetica', 12)).pack(side="top", fill="x", pady=5)
        self.var = tk.IntVar()
        merchan = tk.Entry(self, bg="black", fg="white", textvariable=self.var)
        merchan.pack()
        button = tk.Button(self, text="Enter", command=self.get_item)
        button.pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi)).pack()

    def get_item(self):
        if self.var.get() == 4143:
            messagebox.showinfo("Congrats!", "你獲得一張沒用印的校長聘書")
            self.master.switch_frame(Lead_him_to_next_scene)

        else:
            messagebox.showinfo("像話嗎", "沒認真上課還敢喝飲料啊")


class Lead_him_to_next_scene(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="寫程式真是累人啊，休息是為了走更長遠的路，回去水源宿舍睡覺吧", font=('Helvetica', 12)).pack()
        tk.Button(self, text="confirm", command=lambda: master.switch_frame(Campus)).pack()


class Multi_conver(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="討論室A", command=lambda: master.switch_frame(Multi_converA)).pack()
        tk.Button(self, text="討論室B", command=lambda: master.switch_frame(Multi_converB)).pack()
        tk.Button(self, text="討論室C", command=lambda: master.switch_frame(Multi_converC)).pack()
        tk.Button(self, text="討論室D", command=lambda: master.switch_frame(Multi_converD)).pack()
        tk.Button(self, text="討論室E", command=lambda: master.switch_frame(Multi_converE)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi)).pack()


class Multi_converA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室A", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="桌子A", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子B", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子C", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_converB(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室B", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="桌子A", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子B", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子C", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_converC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室C", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="桌子A", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子B", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子C", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_converD(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室D", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="桌子A", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子B", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子C", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_converE(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室E", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="桌子A", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子B", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="桌子C", command=lambda: master.switch_frame(Multi_table)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_table(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌子", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look", command=lambda: master.switch_frame(Multi_Look_normaltable)).pack()
        tk.Button(self, text="Use", command=lambda: master.switch_frame(Multi_Use_normaltable)).pack()
        tk.Button(self, text="Get", command=lambda: master.switch_frame(Multi_get_normaltable)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_Use_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="電腦", command=lambda: master.switch_frame(Multi_Use_normaltable_computer)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_table)).pack()


class Multi_Look_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌上只有一個別人的電腦和一枚十元硬幣").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_table)).pack()


class Multi_Use_normaltable_computer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="不亂使用別人的禮貌是基本禮貌吧", font=('Helvetica', 80, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_table)).pack()


class Multi_get_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="硬幣", command=lambda: master.switch_frame(self.get_coin)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_table)).pack()

    def get_coin(self):
        messagebox.showinfo("Congrats!", "你獲得了一枚十元硬幣")
    # 但我這裡還沒有寫獲得多次硬幣的情況，只先把畫面寫出來而已

class Multi_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌子", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look", command=lambda: master.switch_frame(Multi_Look_converA_tableC)).pack()
        tk.Button(self, text="Get", command=lambda: master.switch_frame()).pack()
        tk.Button(self, text="Use", command=lambda: master.switch_frame(Multi_Use_converA_tableC)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_Look_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌上只有一個電腦和一枚十元硬幣").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="電腦", command=lambda: master.switch_frame(Multi_Look_computer_converA_tableC)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()


class Multi_Use_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="電腦", command=lambda: master.switch_frame(Multi_Use_converA_tableC_computer)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()


class Multi_Look_computer_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="電腦").pack()
        tk.Label(self, text="一台亮著的電腦，上面的程式似乎是可以使用的").pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()


class Multi_Use_converA_tableC_computer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="文字轉換器", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="剛剛上課夠認真，應該知道答案是什麼吧", font=('Helvetica', 7)).pack(side="top", fill="x")
        self.ord = tk.StringVar()
        ord_content = tk.Entry(self, bg="black", fg="white", textvariable=self.ord)
        ord_content.pack(side="top", fill="x")
        button = tk.Button(self, text="Enter", command=self.ord_correct)
        button.pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()


    def ord_correct(self):
        if self.ord.get() == "AC":
            messagebox.showinfo("文字轉換器", "4143")
            tk.Label(self, text="若覺得渴的話不妨到飲料機看看", font=('Helvetica', 12))
        else:
            messagebox.showinfo("文字轉換器", "錯誤資訊，請稍後再輸入")


b = 0
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
