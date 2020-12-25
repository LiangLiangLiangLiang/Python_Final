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

class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)            
        tk.Button(self, text="綜合大樓",command=lambda: master.switch_frame(Multi)).pack()
        tk.Button(self, text="水源宿舍",command=lambda: master.switch_frame(Dorm)).pack()
        tk.Button(self, text="社科圖",command=lambda: master.switch_frame(Social_Science_Library)).pack()
        tk.Button(self, text="行政大樓",command=lambda: master.switch_frame(Administration)).pack()
        tk.Button(self, text="心輔中心",command=lambda: master.switch_frame(Counsel)).pack()
        tk.Button(self, text="公車站",command=lambda: master.switch_frame(Bus)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus)).pack()

class Social_Science_Library(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="社科圖", font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Social_Science_Library_Move)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus_Move)).pack()

class Dorm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="水源宿舍", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Dorm_Move)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus_Move)).pack()

class Social_Science(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Social_Science", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Social_Science_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Social_Science_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Social_Science_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Social_Science_Use)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus_Move)).pack()

class Administration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Administration", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Administration_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Administration_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Administration_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Administration_Use)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus_Move)).pack()

class Counsel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Counsel", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Counsel_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Counsel_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Counsel_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Counsel_Use)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus_Move)).pack()

class Bus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Bus", font=('Helvetica', 18, "bold"),bg='yellow').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Look",command=lambda: master.switch_frame(Bus_Look)).pack()
        tk.Button(self, text="Move",command=lambda: master.switch_frame(Bus_Move)).pack()
        tk.Button(self, text="Talk",command=lambda: master.switch_frame(Bus_Talk)).pack()
        tk.Button(self, text="Use",command=lambda: master.switch_frame(Bus_Use)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Campus_Move)).pack()


class Dorm_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="要去哪裡?", font=('Helvetica', 18, "bold"), bg = "yellow").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="房間",command=lambda: master.switch_frame(Dorm_Room)).pack()
        tk.Button(self, text="舍監的辦公室",command=lambda: master.switch_frame(Dorm_Janitor)).pack()
        tk.Button(self, text="洗衣間",command=lambda: master.switch_frame(Dorm_Laundry)).pack()
        tk.Button(self, text="後門",command=lambda: master.switch_frame(Dorm_BackDoor)).pack()
        tk.Button(self, text="Cancel",command=lambda: master.switch_frame(Dorm)).pack()
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
d1_Dorm_Janitor = {1:"(咳咳咳)"  + "\n我當了71年的舍監，從來沒遇過沒校長的狀況", 2:"(電話突然響了!!!)" + "\n恩，恩，好，好，沒問題...", 3:"有同學請我處理事情，但我好懶喔，你可以幫我嗎?",
        4:"請你幫我到xxx房間換一下燈泡",5:"(換完燈泡)" + "\n那再麻煩你去洗衣間修一下洗衣機壞掉的門好不好",6:"(發現洗衣機門可以開了)",
        7:"歹勢，最後一件事麻煩你了" + "\n這個印章給你，請你幫到後門領一個包裹，感謝你!",8:"(遇見一個郵差好像在等人)",9:"ㄟˊ同學你出現了!幫我在這裡蓋個章吧", 10:"回去找舍監吧!",
        11:"哇真的很謝謝你^_^" + "\n感謝你今天的幫忙" + "\n願上帝保佑你",
        12:"Next", 13:"Next", 14:"好挖", 15:"前往xxx房間換燈泡",16:"好!" + "(前往洗衣間)",17:"ㄘㄟˊ我根本不用來啊" + "\n回去找舍監",
        18:"(OS:哪來這麼多事可以做)" + "\n好~~~" + "(前往後門)", 19:"跟他說話", 20:"", 21:"Let's Go!!", 22:"助人為快樂之本......吧" + "\n印章又能做甚麼..." + "\n(Back to Campus)"}
aline = ""
class Dorm_Janitor_Talk(tk.Frame):
    def __init__(self, master):
        global state
        global aline
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d1_Dorm_Janitor[state], font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
        if state == 9:
            tk.Button(self, text = "心不甘情不願的蓋下去",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_Janitor_Talk)]).pack()
            tk.Button(self, text = "管他三七二十一蓋就對了",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_Janitor_Talk)]).pack()
        elif state == 7:
            tk.Button(self, text = d1_Dorm_Janitor[state + 11],command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "獲得了印章!"), master.switch_frame(Dorm_Janitor_Talk)]).pack()
        elif state == 11:
            tk.Button(self, text = d1_Dorm_Janitor[state + 11],command=lambda: master.switch_frame(Dorm_Move)).pack()
            state = 0
            aline += "1"
        else:
            tk.Button(self, text = d1_Dorm_Janitor[state + 11],command=lambda: master.switch_frame(Dorm_Janitor_Talk)).pack()
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
x = 1
class Dorm_BackDoor(tk.Frame):
    def __init__(self, master):
        global state
        global aline
        global x
        tk.Frame.__init__(self, master)
        if aline.find("1") == -1 and state == x:
            tk.Label(self, text = "(" + "看見一個郵差" + ")", font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "跟他說話",command=lambda: master.switch_frame(Dorm_BackDoor)).pack()
            x = state
            state += 1
        elif aline.find("1") == -1 and state == x + 1:
            tk.Label(self, text = "..........(" + "一片安靜" + ")", font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "真無聊，回到宿舍大廳好了",command=lambda: master.switch_frame(Dorm_Move)).pack()
            x = 1
            state = 1
        elif aline.find("1") != -1:
            tk.Label(self, text = "這裡沒有人了", font=('Helvetica', 18, "bold"), bg='yellow').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Dorm",command=lambda: master.switch_frame(Dorm_Move)).pack()
        
class Social_Science_Library_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="管理員:「你有學生證嗎」", font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
        if aline.find("2") != -1:
            tk.Button(self, text="有",command=lambda: master.switch_frame(Social_Science_Library_Yes)).pack()
            tk.Button(self, text="沒有",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "你明明就有!"), master.switch_frame(Social_Science_Library_Yes)]).pack()
        else:
            tk.Button(self, text="有",command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "你明明就沒有!"), master.switch_frame(Social_Science_Library_No)]).pack()
            tk.Button(self, text="沒有",command=lambda: master.switch_frame(Social_Science_Library_No)).pack()
d1_SS_Library_Yes = dict()
d1_SS_Library_Yes = {1:"進入社科圖", 2:"(" + "腦中一閃而過" + ")" + "\n來寫程式設計作業好了", 3:"class是甚麼東東啊要麼用...",
        4:"(" + "再過一陣子" + ")" + "好無聊ㄛ想去玩貓~~", 5:"ㄟˊ有貓貓耶:)好可愛XD", 6:"貓:「喵喵喵」",
        7:"(" + "突然!!!" + ")" + "\n貓嘔吐出管中閔的畢業證書",8:"矮額為甚麼有這種東西...",
        9:"Go!", 10:"打開電腦", 11:"(" + "停在同一個地方很久" + ")", 12:"去社科院玩貓", 13:"莫名其妙開始跟貓貓說起話", 14:"我:「喵喵喵」",
        15:"把它撿起來",16:"算了先收起來" + "\n(" + "Back to Campus" + ")"}
d1_SS_Library_No = dict()
d1_SS_Library_No = {1:"進入社科圖", 2:"管理員:「同學你沒有刷卡，不能進來ㄛ」", 3:"(" + "等了30秒" + ")" + "有人要進去了!我可以偷偷跟著進去吧",
        4:"管理員:「你又來!沒有學生證就出去!」", 5:"Go!", 6:"好吧...", 7:"跟在那個人後面偷偷進去嘻嘻嘻", 8:"又失敗了...還是乖乖回去社科院上課吧"}
y = 0
class Social_Science_Library_Yes(tk.Frame):
    def __init__(self, master):
        global state
        global y
        tk.Frame.__init__(self, master)
        if state == 7 and y == 0:
            tk.Label(self, text = d1_SS_Library_Yes[state], font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_SS_Library_Yes[state + 8],command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了沾滿貓咪口水的管中閔畢業證書!"), master.switch_frame(Social_Science_Library_Yes)]).pack()
        elif state == 8 and y == 0:
            tk.Label(self, text = d1_SS_Library_Yes[state], font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_SS_Library_Yes[state + 8],command=lambda: master.switch_frame(Campus)).pack()
            state = 0
            y = 1
        elif state != 7 and state != 8 and y == 0:
            tk.Label(self, text = d1_SS_Library_Yes[state], font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_SS_Library_Yes[state + 8],command=lambda: master.switch_frame(Social_Science_Library_Yes)).pack()
        elif state != 7 and state != 8 and y == 1:
            tk.Label(self, text = "社科圖關門了!!!", font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Campus",command=lambda: master.switch_frame(Campus)).pack()
        state += 1
class Social_Science_Library_No(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 4 and y == 0:
            tk.Label(self, text = d1_SS_Library_No[state], font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_SS_Library_No[state + 4],command=lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        elif state != 4 and y == 0:
            tk.Label(self, text = d1_SS_Library_No[state], font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_SS_Library_No[state + 4],command=lambda: master.switch_frame(Social_Science_Library_No)).pack()
        elif state != 4 and y == 1:
            tk.Label(self, text = "社科圖關門了!!!", font=('Helvetica', 18, "bold"),bg='aqua').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = "Back to Campus",command=lambda: master.switch_frame(Campus)).pack()
        state += 1
class Social_Science_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "社科院", font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        tk.Label(self, text = "要去哪裡?", font=('Helvetica', 18, "bold"),bg='red').pack(side="top", fill="x", pady=5)
        tk.Button(self, text="王道一的教室",command=lambda: master.switch_frame(Social_Science_Wang)).pack()
        tk.Button(self, text="林明仁的教室",command=lambda: master.switch_frame(Social_Science_Lin)).pack()
        tk.Button(self, text="吳聰敏的教室",command=lambda: master.switch_frame(Social_Science_Wu)).pack()
        tk.Button(self, text="Back to Social Science Library",command=lambda: master.switch_frame(Social_Science_Library)).pack()
bline = ""
cline = ""
d1_Social_Science = dict()
d2_Social_Science = dict()
d3_Social_Science = dict()
d1_Social_Science = {1:"我是王道一", 2:"人們在面對全然陌生的選擇時", 3:"很難第一次就上手、做到最佳化",
        4:"而且除了容易有隨機、不小心的錯誤之外",5:"還會受到認知、先入為主的",6:"成見、文化背景等因素影響而產生「有系統的偏誤」",
        7:"以致於偏離經濟理論上的均衡預測",8:"但是，實驗結果也顯示人們得知做決定所產生的結果之後",9:"會嘗試增進他們的決策品質、「學習」做更好的選擇", 10:"進而逼近經濟理論上的最佳解"}
d2_Social_Science = {1:"我是林明仁，啊你們一定要知道芝加哥的經濟學派...", 2:"(" + "拿出他跟一堆不認識但好像很有名的人的合照" + ")", 3:"《自由的窄廊》 與《國家為什麼會失敗》這兩本書你們一定要看",
        4:"在自由民主正處於過去五十年來遭受最多質疑的年代",5:"這兩本書仍然是鼓勵我們思考如何對抗極權、捍衛自由最有力的兩本經典",6:"就讓我以羅賓森在討論此議題時最愛引用的美國開國元勛富蘭克林的名言",
        7:"作為此一導讀的結語",8:"We must, indeed",9:"all hang together, or most assuredly", 10:"we shall all hang separately"}
d3_Social_Science = {1:"我是吳聰敏", 2:"然後我跟凱因斯不熟!!", 3:"人生是不可能有規劃的",
        4:"必然要親身經歷過",5:"才能認知自己對一件事的喜好",6:"沒有經歷過的",
        7:"都只是你想像中的好惡",8:"鼓勵你們有實際的工作經驗",9:"及早找個實習──實際接觸", 10:"才能真正發掘出自己的興趣"}
class Social_Science_Wang(tk.Frame):
    def __init__(self, master):
        global state
        global bline
        global cline
        bline += "1"
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d1_Social_Science[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        if state != 10:
            tk.Button(self, text = "Next",command = lambda: master.switch_frame(Social_Science_Wang)).pack()
        elif state == 10 and bline.find("1") != -1 and bline.find("2") != -1 and bline.find("3") != -1 and cline.find("4") == -1:
            tk.Button(self, text = "早知道上王道一的課這麼無聊，去玩貓就好了" + "\n想去社科院找貓...",command = lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "恭喜你上完三位老師的課!" + "\n去社科院找貓吧!"), master.switch_frame(No_ID_Cat)]).pack()
            cline += "4"
            state = 0
        else:
            tk.Button(self, text = "早知道上王道一的課這麼無聊，就去上林明仁的課就好了" + "\nBack to Social Science",command = lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        state += 1
class Social_Science_Lin(tk.Frame):
    def __init__(self, master):
        global state
        global bline
        global cline
        bline += "2"
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d2_Social_Science[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        if state != 10:
            tk.Button(self, text = "Next",command = lambda: master.switch_frame(Social_Science_Lin)).pack()
        elif state == 10 and bline.find("1") != -1 and bline.find("2") != -1 and bline.find("3") != -1 and cline.find("4") == -1:
            tk.Button(self, text = "早知道上林明仁的課這麼無聊，去玩貓就好了" + "\n想去社科院找貓...",command = lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "恭喜你上完三位老師的課!" + "\n去社科院找貓吧!"), master.switch_frame(No_ID_Cat)]).pack()
            cline += "4"
            state = 0
        else:
            tk.Button(self, text = "早知道上林明仁的課這麼無聊，就去上吳聰敏的課就好了" + "\nBack to Social Science",command = lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        state += 1
class Social_Science_Wu(tk.Frame):
    def __init__(self, master):
        global state
        global bline
        global cline
        bline += "3"
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d3_Social_Science[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
        if state != 10:
            tk.Button(self, text = "Next",command = lambda: master.switch_frame(Social_Science_Wu)).pack()
        elif state == 10 and bline.find("1") != -1 and bline.find("2") != -1 and bline.find("3") != -1 and cline.find("4") == -1:
            tk.Button(self, text = "早知道上吳聰敏的課這麼無聊，去玩貓就好了" + "\n想去社科院找貓...",command = lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "恭喜你上完三位老師的課!" + "\n去社科院找貓吧!"), master.switch_frame(No_ID_Cat)]).pack()
            cline += "4"
            state = 0
        else:
            tk.Button(self, text = "早知道上吳聰敏的課這麼無聊，就去上王道一的課就好了" + "\nBack to Social Science",command = lambda: master.switch_frame(Social_Science_Move)).pack()
            state = 0
        state += 1
d1_No_ID_Cat = dict()
d1_No_ID_Cat = {1:"ㄟˊ好多貓貓耶:)好可愛XD", 2:"貓:「喵喵喵」",
        3:"(" + "突然!!!" + ")" + "\n貓嘔吐出管中閔的畢業證書",4:"矮額為甚麼有這種東西...",
        5:"莫名其妙開始跟貓貓說起話", 6:"我:「喵喵喵」",
        7:"把它撿起來",8:"算了先收起來" + "\n(" + "Back to Campus" + ")"}
class No_ID_Cat(tk.Frame):
    def __init__(self, master):
        global state
        global y
        tk.Frame.__init__(self, master)
        if state == 3:
            tk.Label(self, text = d1_No_ID_Cat[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_No_ID_Cat[state + 4],command=lambda: [tkinter.messagebox.showinfo(title = "訊息框", message = "拿到了沾滿貓咪口水的管中閔畢業證書!"), master.switch_frame(No_ID_Cat)]).pack()
        elif state == 4:
            tk.Label(self, text = d1_No_ID_Cat[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_No_ID_Cat[state + 4],command=lambda: master.switch_frame(Campus)).pack()
            state = 0
            y = 1
        else:
            tk.Label(self, text = d1_No_ID_Cat[state], font=('Helvetica', 18, "bold"),bg='lawngreen').pack(side="top", fill="x", pady=5)
            tk.Button(self, text = d1_No_ID_Cat[state + 4],command=lambda: master.switch_frame(No_ID_Cat)).pack()
        state += 1

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
