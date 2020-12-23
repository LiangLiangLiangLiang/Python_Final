try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter.messagebox
state = 1

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Campus)
        self.geometry("900x400")
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Campus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Campus", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Campus_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Campus_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Campus_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Campus_Use)).pack()

class Multi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Multi", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Multi_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Multi_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Multi_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Multi_Use)).pack()

class Dorm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="水源宿舍", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Dorm_Move)).pack()

class Social_Science(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Social_Science", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Social_Science_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Social_Science_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Social_Science_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Social_Science_Use)).pack()

class Administration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Administration", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Administration_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Administration_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Administration_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Administration_Use)).pack()

class Counsel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Counsel", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Counsel_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Counsel_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Counsel_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Counsel_Use)).pack()

class Bus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Bus", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Bus_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Bus_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Bus_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Bus_Use)).pack()

class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)            
        tk.Button(self, text="綜合大樓",command=lambda: master.switch_frame(Multi)).pack()
        tk.Button(self, text="水源宿舍",command=lambda: master.switch_frame(Dorm)).pack()
        tk.Button(self, text="社科院",command=lambda: master.switch_frame(Social_Science)).pack()
        tk.Button(self, text="行政大樓",command=lambda: master.switch_frame(Administration)).pack()
        tk.Button(self, text="心輔中心",command=lambda: master.switch_frame(Counsel)).pack()
        tk.Button(self, text="公車站",command=lambda: master.switch_frame(Bus)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus)).pack()


class Dorm_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="要去哪裡?", font=('Helvetica', 18, "bold"), bg = "yellow").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="房間",command=lambda: master.switch_frame(Dorm_Room)).pack()
        tk.Button(self, text="舍監的辦公室",command=lambda: master.switch_frame(Dorm_Janitor)).pack()
        tk.Button(self, text="洗衣間",command=lambda: master.switch_frame(Dorm_Laundry)).pack()
        tk.Button(self, text="後門",command=lambda: master.switch_frame(Dorm_BackDoor)).pack()
d1_Dorm_Room = dict()
d1_Dorm_Room = {1:"(" + "看到室友站在梯子上弄著燈泡" + ")", 2:"燈泡壞掉了，叫舍監好久了都沒來"}
class Dorm_Room(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 1:
            tk.Label(self, text = d1_Dorm_Room[state], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "問他怎麼了",command=lambda: master.switch_frame(Dorm_Room)).pack()
        else:
            tk.Label(self, text = d1_Dorm_Room[state], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Dorm",command=lambda: master.switch_frame(Dorm_Move)).pack()
            state = 0
        state += 1
class Dorm_Janitor(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="舍監",command=lambda: master.switch_frame(Dorm_Janitor_Talk)).pack()
d1_Dorm_Janitor = dict()
d1_Dorm_Janitor = {1:"(" + "咳咳咳" + ")"  + "\n我當了71年的舍監，從來沒遇過沒校長的狀況", 2:"(" + "電話突然響了!!!" + ")" + "\n恩，恩，好，好，沒問題...", 3:"有同學請我處理事情，但我好懶喔，你可以幫我嗎?",
        4:"請你幫我到xxx房間換一下燈泡",5:"(" + "換完燈泡" + ")" + "\n那再麻煩你去洗衣間看一下有甚麼情況好不好",6:"(" + "發現洗衣機門可以開了" + ")",
        7:"歹勢，最後一件事麻煩你了" + "\n請你幫到後門領一個包裹，感謝你!",8:"(" + "遇見一個郵差好像在等人" + ")",9:"ㄟˊ同學你出現了!幫我在這裡簽個名吧", 10:"回去找舍監吧!",
        11:"哇真的很謝謝你^_^" + "\n為了表達我的謝意，這個印章給你!" + "\n相信你以後應該會用到的~", 12:"助人為快樂之本......吧" + "\n印章又能做甚麼...", 
        13:"Next", 14:"Next", 15:"好挖", 16:"前往xxx房間換燈泡",17:"好!" + "(" + "前往洗衣間" + ")",18:"ㄘㄟˊ我根本不用來啊" + "\n回去找舍監",
        19:"(" + "OS:哪來這麼多事可以做" + ")" + "\n好~~~" + "(" + "前往後門" + ")", 20:"跟他說話", 22:"Let's Go!!", 23:"從舍監手中接過印章", 24:"Back to Campus"}
alist = []
class Dorm_Janitor_Talk(tk.Frame):
    def __init__(self, master):
        global state
        global alist
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d1_Dorm_Janitor[state], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
        if state == 9:
            tk.Button(self, text = "心不甘情不願的簽名了",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_Janitor_Talk)]).pack()
            tk.Button(self, text = "管他三七二十一簽就對了",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_Janitor_Talk)]).pack()
        elif state == 11:
            tk.Button(self, text = d1_Dorm_Janitor[state + 12],command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "獲得了印章!"), master.switch_frame(Dorm_Janitor_Talk)]).pack()
        elif state == 12:
            tk.Button(self, text = d1_Dorm_Janitor[state + 12],command=lambda: master.switch_frame(Campus)).pack()
            state = 0
            alist.append("1")
        else:
            tk.Button(self, text = d1_Dorm_Janitor[state + 12],command=lambda: master.switch_frame(Dorm_Janitor_Talk)).pack()
        state += 1
d1_Dorm_Laundry = dict()
d1_Dorm_Laundry = {1:"(" + "看到一個同學站在洗衣機前若有所思的樣子" + ")", 2:"洗衣機的門打不開，這樣明天國企之夜沒有衣服穿QQ，而且舍監不見了0_O"}
class Dorm_Laundry(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 1:
            tk.Label(self, text = d1_Dorm_Laundry[state], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "問他怎麼了",command=lambda: master.switch_frame(Dorm_Laundry)).pack()
        else:
            tk.Label(self, text = d1_Dorm_Laundry[state], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Dorm",command=lambda: master.switch_frame(Dorm_Move)).pack()
            state = 0
        state += 1
state_BackDoor = 1
d1_Dorm_BackDoor = dict()
d1_Dorm_BackDoor = {1:"(" + "遇見一個郵差好像在等人" + ")", 2:"ㄟˊ既然同學你出現了，幫我在這裡簽個名然後交給舍監"}
class Dorm_BackDoor(tk.Frame):
    def __init__(self, master):
        global state_BackDoor
        tk.Frame.__init__(self, master)
        if state_BackDoor == 1:
            tk.Label(self, text = d1_Dorm_BackDoor[state_BackDoor], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "問他找誰",command=lambda: master.switch_frame(Dorm_BackDoor)).pack()
        elif state_BackDoor == 2:
            tk.Label(self, text = d1_Dorm_BackDoor[state_BackDoor], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "心不甘情不願的簽名了",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_BackDoor)]).pack()
            tk.Button(self, text = "管他三七二十一簽就對了",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_BackDoor)]).pack()
        elif state_BackDoor == 3:
            tk.Label(self, text = d1_Dorm_BackDoor[state_BackDoor - 1], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Dorm",command=lambda: master.switch_frame(Dorm_Move)).pack()
        else:
            tk.Label(self, text = "拿到包裹了，去找舍監吧!", font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Dorm",command=lambda: master.switch_frame(Dorm_Move)).pack()
        state_BackDoor += 1
    
class Social_Science_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold"), bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",command=lambda: master.switch_frame(Social_Science)).pack()

class Social_Science_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="王道一的教室",command=lambda: master.switch_frame(Social_Science_Wang)).pack()
        tk.Button(self, text="林明仁的教室",command=lambda: master.switch_frame(Social_Science_Lin)).pack()
        tk.Button(self, text="吳聰敏的教室",command=lambda: master.switch_frame(Social_Science_Wu)).pack()
        tk.Button(self, text="社科圖",command=lambda: master.switch_frame(Social_Science_Library)).pack()
d1_Social_Science = dict()
d2_Social_Science = dict()
d3_Social_Science = dict()
d1_Social_Science = {1:"我是王道一", 2:"", 3:"",
        4:"",5:"",6:"",
        7:"",8:"",9:"", 10:""}
d2_Social_Science = {1:"我是林明仁，啊你們一定要知道芝加哥的經濟學派...", 2:"(" + "拿出他跟一堆不認識但好像很有名的人的合照" + ")", 3:"《自由的窄廊》 與《國家為什麼會失敗》這兩本書你們一定要看",
        4:"在自由民主正處於過去五十年來遭受最多質疑的年代",5:"這兩本書仍然是鼓勵我們思考如何對抗極權、捍衛自由最有力的兩本經典",6:"就讓我以羅賓森在討論此議題時最愛引用的美國開國元勛富蘭克林的名言",
        7:"作為此一導讀的結語",8:"We must, indeed",9:"all hang together, or most assuredly", 10:"we shall all hang separately"}
d3_Social_Science = {1:"我是吳聰敏", 2:"拿出他跟一堆不認識但好像很有名的人的合照", 3:"《自由的窄廊》 與《國家為什麼會失敗》這兩本書你們一定要看",
        4:"在自由民主正處於過去五十年來遭受最多質疑的年代",5:"這兩本書仍然是鼓勵我們思考如何對抗極權、捍衛自由最有力的兩本經典",6:"就讓我以羅賓森在討論此議題時最愛引用的美國開國元勛富蘭克林的名言",
        7:"作為此一導讀的結語",8:"We must, indeed",9:"all hang together, or most assuredly", 10:"we shall all hang separately"}
class Social_Science_Wang(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d1_Social_Science[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        if state != 10:
            tk.Button(self, text = "Next",command = lambda: master.switch_frame(Social_Science_Wang)).pack()
        else:
            tk.Button(self, text = "Back to Social Science",command = lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        state += 1
class Social_Science_Lin(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d2_Social_Science[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        if state != 10:
            tk.Button(self, text = "Next",command = lambda: master.switch_frame(Social_Science_Lin)).pack()
        else:
            tk.Button(self, text = "Back to Social Science",command = lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        state += 1
class Social_Science_Wu(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d3_Social_Science[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        if state != 10:
            tk.Button(self, text = "Next",command = lambda: master.switch_frame(Social_Science_Wu)).pack()
        else:
            tk.Button(self, text = "Back to Social Science",command = lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        state += 1
class Social_Science_Library(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="你有學生證嗎", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="有",command=lambda: master.switch_frame()).pack()
        tk.Button(self, text="沒有",command=lambda: master.switch_frame()).pack()

class Social_Science_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="You cannot use", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="舍監",command=lambda: master.switch_frame(Social_Science)).pack()
        
class Social_Science_Use(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="You cannot use", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",command=lambda: master.switch_frame(Social_Science)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
