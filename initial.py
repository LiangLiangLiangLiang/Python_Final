try:
    import Tkinter as tk
except:
    import tkinter as tk


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
        tk.Label(self, text="Campus", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Campus_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Campus_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Campus_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Campus_Use)).pack()


class Multi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="綜合大樓", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Multi_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Multi_Move1)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Multi_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Multi_Use)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Campus)).pack()


class Multi_Move1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="販賣機", command=lambda: master.switch_frame(Multi_sale)).pack()
        tk.Button(self, text="綜合大講堂", command=lambda: master.switch_frame(Multi_Audi)).pack()
        tk.Button(self, text="討論室", command=lambda: master.switch_frame(Multi_conver)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi)).pack()


class Multi_sale(tk.Frame):
    def __init__(self, master):
        f = tkFont.Font(size=16, family="Courier New")
        tk.Frame.__init__(self, master)
        self.writeAC = tk.Text(self, height=1, width=40)


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
        tk.Button(self, text="Move").pack()
        tk.Button(self, text="Talk",).pack()
        tk.Button(self, text="Use", command=lambda: master.switch_frame(Multi_Use_normaltable)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_Use_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="電腦", command=lambda: master.switch_frame(Multi_Use_normaltable_computer)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_table)).pack()


class Multi_Use_normaltable_computer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="不亂使用別人的禮貌是基本禮貌吧", font=('Helvetica', 80, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_table)).pack()

class Multi_Look_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌上只有一個別人的電腦和一枚十元硬幣").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌子", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look", command=lambda: master.switch_frame(Multi_Look_converA_tableC)).pack()
        tk.Button(self, text="Move", command=lambda: master.switch_frame()).pack()
        tk.Button(self, text="Talk", command=lambda: master.switch_frame(Multi_Talk)).pack()
        tk.Button(self, text="Use", command=lambda: master.switch_frame(Multi_Use_converA_tableC)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_conver)).pack()


class Multi_Look_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌上只有一個電腦和一枚十元硬幣").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="電腦", command=lambda: master.switch_frame(Multi_Look_computer_converA_tableC)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()


class Multi_Look_computer_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="電腦").pack()
        tk.Label(self, text="一台亮著的電腦，上面的程式似乎是可以使用的").pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Multi_converA_tableC)).pack()


class Multi_Use_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="電腦", command=lambda: master.switch_frame(Multi_Use_converA_tableC_computer)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame()).pack()


class Multi_Use_converA_tableC_computer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Entry(self, height=10, width=20)


class Dorm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Dorm", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Dorm_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Dorm_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Dorm_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Dorm_Use)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Campus)).pack()


class Social_Science(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Social_Science", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Social_Science_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Social_Science_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Social_Science_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Social_Science_Use)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Campus)).pack()


class Administration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Administration", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Administration_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Administration_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Administration_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Administration_Use)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Campus)).pack()


class Counsel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Counsel", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Counsel_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Counsel_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Counsel_Use)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Campus)).pack()


class Bus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Bus", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Bus_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Bus_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Bus_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Bus_Use)).pack()
        tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Campus)).pack()


class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="綜合大樓", command=lambda: master.switch_frame(Multi)).pack()
        tk.Button(self, text="水源宿舍", command=lambda: master.switch_frame(Dorm)).pack()
        tk.Button(self, text="社科院", command=lambda: master.switch_frame(Social_Science)).pack()
        tk.Button(self, text="行政大樓", command=lambda: master.switch_frame(Administration)).pack()
        tk.Button(self, text="心輔中心", command=lambda: master.switch_frame(Counsel)).pack()
        tk.Button(self, text="公車站", command=lambda: master.switch_frame(Bus)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()