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
        tk.Label(self, text="台大校園", font=('Helvetica', 20, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Campus_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Campus_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Campus_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Campus_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")

class Multi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="綜合大樓", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Multi_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Multi_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Multi_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Multi_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Dorm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="水源宿舍", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Dorm_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Dorm_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Dorm_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Dorm_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Social_Science(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="社科院", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Social_Science_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Social_Science_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Social_Science_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Social_Science_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Administration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="行政大樓", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Administration_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Administration_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Administration_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Administration_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Counsel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="心輔中心", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Counsel_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Counsel_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Counsel_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Counsel_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Bus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Bus", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Bus_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Bus_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Bus_Talk)).grid(row=3, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Bus_Use)).grid(row=3, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

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

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
