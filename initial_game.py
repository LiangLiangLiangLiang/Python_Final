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
        tk.Label(self, text="校園", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
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
        tk.Button(self, text="Look").pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Multi_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Multi_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Multi_Use)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

class Dorm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="水源宿舍", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Dorm_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Dorm_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Dorm_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Dorm_Use)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

class Social_Science(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="社科院", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Social_Science_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Social_Science_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Social_Science_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Social_Science_Use)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

class Administration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="行政大樓", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Administration_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Administration_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Administration_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Administration_Use)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

class Counsel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="心輔中心", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",
                  command=lambda: master.switch_frame(Counsel_Look)).pack()
        tk.Button(self, text="Move",
                  command=lambda: master.switch_frame(Counsel_Move)).pack()
        tk.Button(self, text="Talk",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()
        tk.Button(self, text="Use",
                  command=lambda: master.switch_frame(Counsel_Use)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

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
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

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

# 這邊是在校園裡對話（跟傅斯年）的部分
Fudict = {1:"去上課",2:"去反省"}
Fu_State = 1
'''
以下這段要再更改寫法、決定要放在哪個函數裡
Fudict = {1:"去上課",2:"去反省"}
Fu_State = 1
'''
class Campus_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)        
        tk.Label(self, text=Fudict[Fu_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Campus)).pack()

# 此行後為行政大樓和心輔中心
class Administration_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="校長室",command=lambda: master.switch_frame(Principal_Office)).pack()
        tk.Button(self, text="教務處",command=lambda: master.switch_frame(Academic_Office)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Administration)).pack()

class Principal_Office(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="這裡什麼都沒有。", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Administration_Move)).pack()

class Academic_Office(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Assistant)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Administration_Move)).pack()

Assistant_Dialogue = {1:"請問要補辦學生證嗎？",2:"好了，這是您的學生證。",3:"請按下Cancel回到上一頁",4:"請按下Cancel回到上一頁",5:"請按下Cancel回到上一頁",6:"請按下Cancel回到上一頁",7:"請按下Cancel回到上一頁"}
Assistant_Dialogue_State = 1
class Assistant(tk.Frame):
    def __init__(self, master):
        global Assistant_Dialogue_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Assistant_Dialogue[Assistant_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Next",command=lambda: master.switch_frame(Assistant)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Administration_Move)).pack()
        Assistant_Dialogue_State += 1

class Counsel_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="時鐘",
                  command=lambda: master.switch_frame(Counsel_Clock)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel)).pack()

Clock = {1:"0000",2:'0000',3:'0000',4:"0030"}
Clock_State = 1
class Counsel_Clock(tk.Frame):
    def __init__(self, master):
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Clock[Clock_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Look)).pack()

# 未依序對話則無法看到0030，但其實也沒關係，這數字沒有用就跟心輔中心一樣
class Counsel_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='請依序和三位心理學家對話。', font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="佛洛依德",command=lambda: master.switch_frame(Freud)).pack()
        tk.Button(self, text="皮亞傑",command=lambda: master.switch_frame(Piaget)).pack()
        tk.Button(self, text="馬斯洛",command=lambda: master.switch_frame(Maslow)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel)).pack()

Freud_Dialogue = {1:"人的精神或人格主要分為三個部分：",2:"分別是本我、超我、自我",3:"當你在街上扶老奶奶過馬路時是哪一個呢？",4:"請按下Cancel回到上一頁",5:"請按下Cancel回到上一頁",6:"請按下Cancel回到上一頁",7:"請按下Cancel回到上一頁",8:"請按下Cancel回到上一頁"}
Freud_Dialogue_State = 1
class Freud(tk.Frame):
    def __init__(self, master):
        global Freud_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Freud_Dialogue[Freud_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Next",command=lambda: master.switch_frame(Freud)).pack()
        Freud_Dialogue_State += 1
        if Clock_State < 2:
            Clock_State += 1
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()

Piaget_Dialogue = {1:'我把兒童的認知發展分為四個階段',2:'分別為感知運動階段、前運算階段',3:'具體運算階段和形式運算階段',4:'你玩這麼高級的遊戲是哪個階段呢？',5:"請按下Cancel回到上一頁",6:"請按下Cancel回到上一頁",7:"請按下Cancel回到上一頁",8:"請按下Cancel回到上一頁",9:"請按下Cancel回到上一頁"}
Piaget_Dialogue_State = 1
class Piaget(tk.Frame):
    def __init__(self, master):
        global Piaget_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Piaget_Dialogue[Piaget_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Next",command=lambda: master.switch_frame(Piaget)).pack()
        Piaget_Dialogue_State += 1
        if Clock_State < 3:
            Clock_State += 1
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()

Maslow_Dialogue = {1:'我把人的需求層次分為五等',2:'遊戲開發者們在做的事是自我實踐層次的！',3:"請按下Cancel回到上一頁",4:"請按下Cancel回到上一頁",5:"請按下Cancel回到上一頁",6:"請按下Cancel回到上一頁",7:"請按下Cancel回到上一頁"}
Maslow_Dialogue_State = 1
class Maslow(tk.Frame):
    def __init__(self, master):
        global Maslow_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Maslow_Dialogue[Maslow_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Next",command=lambda: master.switch_frame(Maslow)).pack()
        Maslow_Dialogue_State += 1
        if Clock_State < 4:
            Clock_State += 1
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
