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
        tk.Label(self, text="Multi", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Multi_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Multi_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Multi_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Multi_Use)).pack()

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

class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)        
        tk.Button(self, text="綜合大樓",command=lambda: master.switch_frame(Multi)).pack()
        tk.Button(self, text="水源宿舍",command=lambda: master.switch_frame(Dorm)).pack()
        tk.Button(self, text="社科院",command=lambda: master.switch_frame(Social_Science)).pack()
        tk.Button(self, text="行政大樓",command=lambda: master.switch_frame(Administration)).pack()
        tk.Button(self, text="心輔中心",command=lambda: master.switch_frame(Counsel)).pack()
        tk.Button(self, text="公車站",command=lambda: master.switch_frame(Bus)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
