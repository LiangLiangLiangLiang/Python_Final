# 這邊是在校園裡對話（跟傅斯年）的部分
Fudict = {1:"去綜合上課",2:"回宿舍反省",3:"去社科院上經原",4:"除了讀書也要注意心理健康ㄛ"}
Fu_State = 1
class Campus_Talk(tk.Frame):
    def __init__(self, master):
        global Fu_State
        if Check_Thing("Contract") == 1:
            Fu_State = 2
        if Check_Thing("Seal") == 1:
            Fu_State = 3
        if Check_Thing("Diploma") == 1:
            Fu_State = 4
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

Assistant_Dialogue = {1:"請問要補辦學生證嗎？",2:"好了，這是您的學生證。",3:"請按下Cancel回到上一頁"}
Assistant_Dialogue_State = 1
class Assistant(tk.Frame):
    def __init__(self, master):
        global Assistant_Dialogue_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Assistant_Dialogue[Assistant_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        if Assistant_Dialogue_State < 3:
            tk.Button(self, text="Next",command=lambda: master.switch_frame(Assistant)).pack()
        if Assistant_Dialogue_State >= 3:
            tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Administration_Move)).pack()
        Assistant_Dialogue_State += 1
        if Assistant_Dialogue_State >= 3:
            Assistant_Dialogue_State = 3
        Change_Backpack('ID_Card')

class Counsel_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Secret of the World",
                  command=lambda: master.switch_frame(Counsel_Clock)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel)).pack()

Clock = {1:"你還不了解人生的真諦。",2:'你對人生的真諦似懂非懂。',3:'離真理只有一步之遙了。',4:"這裡已經沒辦法滿足你了，去更遠的地方看看吧！"}
Clock_State = 1
class Counsel_Clock(tk.Frame):
    def __init__(self, master):
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Clock[Clock_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Look)).pack()
 
class Counsel_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='請依序和三位心理學家對話。', font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="佛洛依德",command=lambda: master.switch_frame(Freud)).pack()
        tk.Button(self, text="皮亞傑",command=lambda: master.switch_frame(Piaget)).pack()
        tk.Button(self, text="馬斯洛",command=lambda: master.switch_frame(Maslow)).pack()
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel)).pack()

Freud_Dialogue = {1:"人的精神或人格主要分為三個部分：",2:"分別是本我、超我、自我",3:"當你在街上扶老奶奶過馬路時是哪一個呢？",4:"請按下Cancel回到上一頁"}
Freud_Dialogue_State = 1
class Freud(tk.Frame):
    def __init__(self, master):
        global Freud_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Freud_Dialogue[Freud_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        if Freud_Dialogue_State < 4:
            tk.Button(self, text="Next",command=lambda: master.switch_frame(Freud)).pack()
        if Freud_Dialogue_State >= 4:
            tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()
        Freud_Dialogue_State += 1
        if Freud_Dialogue_State >= 4:
            Freud_Dialogue_State = 4
        if Clock_State < 2:
            Clock_State += 1
Piaget_Dialogue = {1:'我把兒童的認知發展分為四個階段',2:'分別為感知運動階段、前運算階段',3:'具體運算階段和形式運算階段',4:'你玩這麼高級的遊戲是哪個階段呢？',5:"請按下Cancel回到上一頁"}
Piaget_Dialogue_State = 1
class Piaget(tk.Frame):
    def __init__(self, master):
        global Piaget_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Piaget_Dialogue[Piaget_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        if Piaget_Dialogue_State < 5:
            tk.Button(self, text="Next",command=lambda: master.switch_frame(Piaget)).pack()
        if Piaget_Dialogue_State >= 5:
            tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()
        Piaget_Dialogue_State += 1
        if Piaget_Dialogue_State >= 5:
            Piaget_Dialogue_State = 5
        if Clock_State < 3:
            Clock_State += 1

Maslow_Dialogue = {1:'我把人的需求層次分為五等',2:'遊戲開發者們在做的事是自我實踐層次的！',3:"請按下Cancel回到上一頁"}
Maslow_Dialogue_State = 1
class Maslow(tk.Frame):
    def __init__(self, master):
        global Maslow_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Maslow_Dialogue[Maslow_Dialogue_State], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        if Maslow_Dialogue_State < 3:
            tk.Button(self, text="Next",command=lambda: master.switch_frame(Maslow)).pack()
        if Maslow_Dialogue_State >= 3:
            tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(Counsel_Talk)).pack()
        Maslow_Dialogue_State += 1
        if Maslow_Dialogue_State >= 3:
            Maslow_Dialogue_State = 3
        if Clock_State < 4:
            Clock_State += 1
