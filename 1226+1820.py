try:
    import Tkinter as tk
except:
    import tkinter as tk
from tkinter import messagebox

def Change_Backpack(thing):  # Change_Backpack('Contract');print(Backpack['Contract'])
    global Backpack
    Backpack[thing]=1
    return

def Check_Thing(thing):  # Check_Thing('Contract')
    global Backpack
    return Backpack[thing]

def Use_Thing(thing):  # Use_Thing('Contract')
    global Backpack
    Backpack[thing]=-1
    return

Backpack={'Contract':0,'Coin':0,'Seal':0,'Light_Bulb':0,'Gross':0,'ID_Card':0,'Cat_Stick':0,'Diploma':0}

state = 1

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Campus)
        self.geometry("650x400")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Campus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="台大校園", font=('標楷體', 50, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus_Look)).grid(row=2, column=0, columnspan=3, sticky="nesw")
        tk.Button(self, text="Move", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus_Move)).grid(row=2, column=3, columnspan=3, sticky="nesw")
        tk.Button(self, text="Talk", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus_Talk)).grid(row=3, column=0, columnspan=6, sticky="nesw")
class Multi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="綜合大樓", font=('Helvetica', 50, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2)
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Multi_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move",  font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Multi_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",  font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Social_Science_Library(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="社科圖", font=('Helvetica', 50, "bold"),bg='aqua').grid(row=0, column=0, columnspan=4, sticky="nsew")
        if Backpack["ID_Card"] == 1:
            tk.Button(self, text="Move", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Social_Science_Library_Yes)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Campus_Move)).grid(row=1, column=2, columnspan=2, sticky="nsew")
        else:
            tk.Button(self, text="Move", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Social_Science_Library_No)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Campus_Move)).grid(row=1, column=2, columnspan=2, sticky="nsew")
class Dorm(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="水源宿舍", font=('Helvetica', 50, "bold"),bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Move", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Campus_Move)).grid(row=2, column=0, columnspan=2, sticky="nsew")

class Dorm_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="要去哪裡?", font=('Helvetica', 40, "bold"), bg = "yellow").grid(row=0, column=0, columnspan=4)
        if Backpack["Seal"] == 0:
            tk.Button(self, text="房間", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_Room)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text="舍監的辦公室", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_Janitor)).grid(row=1, column=2, columnspan=2, sticky="nsew")
            tk.Button(self, text="洗衣間", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_Laundry)).grid(row=2, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text="後門", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_BackDoor)).grid(row=2, column=2, columnspan=2, sticky="nsew")
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm)).grid(row=3, column=0, columnspan=4, sticky="nsew")
        else:
            tk.Button(self, text="房間", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_No)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text="舍監的辦公室", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_No)).grid(row=1, column=2, columnspan=2, sticky="nsew")
            tk.Button(self, text="洗衣間", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_No)).grid(row=2, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text="後門", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_BackDoor)).grid(row=2, column=2, columnspan=2, sticky="nsew")
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm)).grid(row=3, column=0, columnspan=4, sticky="nsew")
class Dorm_No(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="門鎖起來了!", font=('Helvetica', 50, "bold"), bg = "red").grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Back to Dorm", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
d1_Dorm_Room = dict()
d1_Dorm_Room = {1:"(" + "看到室友站在梯子上弄著燈泡" + ")", 2:"燈泡壞掉了，叫舍監好久了都沒來"}
class Dorm_Room(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 1:
            tk.Label(self, text = d1_Dorm_Room[state], font=('Helvetica', 20, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "問他怎麼了", font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Dorm_Room)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        else:
            tk.Label(self, text = d1_Dorm_Room[state], font=('Helvetica', 20, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "Back to Dorm", font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Dorm_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
        state += 1
class Dorm_Janitor(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="舍監", font=('Helvetica', 30, "bold"),command=lambda: master.switch_frame(Dorm_Janitor_Talk)).grid(row=0, column=0, columnspan=2, sticky="nsew")
d1_Dorm_Janitor = dict()
d1_Dorm_Janitor = {1:"(咳咳咳)"  + "\n我當了71年的舍監，從來沒遇過沒校長的狀況", 2:"(電話突然響了!!!)" + "\n恩，恩，好，好，沒問題...", 3:"有同學請我處理事情，但我好懶喔，你可以幫我嗎?",
        4:"請你幫我到xxx房間換一下燈泡",5:"(換完燈泡)" + "\n那再麻煩你去洗衣間修一下洗衣機壞掉的門好不好",6:"(發現洗衣機門可以開了)",
        7:"歹勢，最後一件事麻煩你了" + "\n這個印章給你，請你幫到後門領一個包裹，感謝你!",8:"(遇見一個郵差好像在等人)",9:"ㄟˊ同學你出現了!幫我在這裡蓋個章吧", 10:"回去找舍監吧!",
        11:"哇真的很謝謝你^_^" + "\n感謝你今天的幫忙" + "\n願上帝保佑你",
        12:"Next", 13:"Next", 14:"好挖", 15:"前往xxx房間換燈泡",16:"好!" + "(前往洗衣間)",17:"ㄘㄟˊ我根本不用來啊" + "\n回去找舍監",
        18:"(OS:哪來這麼多事可以做)" + "\n好~~~" + "(前往後門)", 19:"跟他說話", 20:"", 21:"Let's Go!!", 22:"助人為快樂之本......吧" + "\n印章又能做甚麼..." + "\n(Back to Campus)"}
class Dorm_Janitor_Talk(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d1_Dorm_Janitor[state], font=('Helvetica', 17, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
        if state == 9:
            tk.Button(self, text = "心不甘情不願的蓋下去", font=('Helvetica', 20, "bold"),command=lambda: [messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_Janitor_Talk)]).grid(row=1, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "管他三七二十一蓋就對了", font=('Helvetica', 20, "bold"),command=lambda: [messagebox.showinfo(title = "訊息框", message = "拿到了包裹!"), master.switch_frame(Dorm_Janitor_Talk)]).grid(row=2, column=0, columnspan=2, sticky="nsew")
        elif state == 7:
            tk.Button(self, text = d1_Dorm_Janitor[state + 11], font=('Helvetica', 20, "bold"), command=lambda: [messagebox.showinfo(title = "訊息框", message = "獲得了印章!"), master.switch_frame(Dorm_Janitor_Talk)]).grid(row=0, column=0, columnspan=2, sticky="nsew")
        elif state == 11:
            tk.Button(self, text = d1_Dorm_Janitor[state + 11], font=('Helvetica', 17, "bold"), command=lambda: master.switch_frame(Campus)).grid(row=0, column=0, columnspan=2, sticky="nsew")
            state = 0
            Change_Backpack('Seal')
        else:
            tk.Button(self, text = d1_Dorm_Janitor[state + 11], font=('Helvetica', 17, "bold"), command=lambda: master.switch_frame(Dorm_Janitor_Talk)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        state += 1
d1_Dorm_Laundry = dict()
d1_Dorm_Laundry = {1:"(" + "看到一個同學站在洗衣機前若有所思的樣子" + ")", 2:"洗衣機的門打不開\n這樣明天國企之夜沒有衣服穿QQ\n而且舍監不見了0_O"}
class Dorm_Laundry(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 1:
            tk.Label(self, text = d1_Dorm_Laundry[state], font=('Helvetica', 17, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "問他怎麼了", font=('Helvetica', 18, "bold"), command=lambda: master.switch_frame(Dorm_Laundry)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        else:
            tk.Label(self, text = d1_Dorm_Laundry[state], font=('Helvetica', 18, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "Back to Dorm", font=('Helvetica', 18, "bold"), command=lambda: master.switch_frame(Dorm_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
        state += 1
x = 1
class Dorm_BackDoor(tk.Frame):
    def __init__(self, master):
        global state
        global Backpack
        global x
        tk.Frame.__init__(self, master)
        if Backpack["Seal"] == 0 and state == x:
            tk.Label(self, text = "(" + "看見一個郵差" + ")", font=('Helvetica', 20, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "跟他說話", font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Dorm_BackDoor)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            x = state
            state += 1
        elif Backpack["Seal"] == 0 and state == x + 1:
            tk.Label(self, text = "..........(" + "一片安靜" + ")", font=('Helvetica', 20, "bold"), bg='yellow').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "真無聊，回到宿舍大廳好了", font=('Helvetica', 20, "bold"), command=lambda: master.switch_frame(Dorm_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            x = 1
            state = 1
        elif Backpack["Seal"] == 1:
            tk.Label(self, text = "這裡沒有人了", font=('Helvetica', 20, "bold"), bg='red').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "Back to Dorm", font=('Helvetica', 20, "bold"), command=lambda: master.switch_frame(Dorm_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        
d1_SS_Library_Yes = dict()
d1_SS_Library_Yes = {1:"進入社科圖", 2:"(" + "腦中一閃而過" + ")" + "\n來寫程式設計作業好了", 3:"class是甚麼東東啊要麼用...",
        4:"(" + "再過一陣子" + ")" + "好無聊ㄛ想去玩貓~~", 5:"ㄟˊ有貓貓耶:)好可愛XD", 6:"貓:「喵喵喵」",
        7:"(" + "突然!!!" + ")" + "\n貓嘔吐出管中閔的畢業證書",8:"矮額為甚麼有這種東西...",
        9:"Go!", 10:"打開電腦", 11:"(" + "停在同一個地方很久" + ")", 12:"去社科院玩貓", 13:"莫名其妙開始跟貓貓說起話", 14:"我:「喵喵喵」",
        15:"把它撿起來",16:"算了先收起來" + "\n(" + "Back to Campus" + ")"}
d1_SS_Library_No = dict()
d1_SS_Library_No = {1:"進入社科圖", 2:"管理員:「同學你沒有刷卡，不能進來ㄛ」", 3:"(" + "等了30秒" + ")" + "有人要進去了!我可以偷偷跟著進去吧",
        4:"管理員:「你又來!沒有學生證就出去!」", 5:"Go!", 6:"好吧...", 7:"跟在那個人後面偷偷進去嘻嘻嘻", 8:"又失敗了...還是乖乖回去社科院上課吧"}
class Social_Science_Library_Yes(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 7 and Backpack["Diploma"] == 0:
            tk.Label(self, text = d1_SS_Library_Yes[state], font=('Helvetica', 20, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_SS_Library_Yes[state + 8], font=('Helvetica', 20, "bold"),command=lambda: [messagebox.showinfo(title = "訊息框", message = "拿到了沾滿貓咪口水的管中閔畢業證書!"), master.switch_frame(Social_Science_Library_Yes)]).grid(row=0, column=0, columnspan=2, sticky="nsew")
        elif state == 8 and Backpack["Diploma"] == 0:
            tk.Label(self, text = d1_SS_Library_Yes[state], font=('Helvetica', 20, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_SS_Library_Yes[state + 8], font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
            Change_Backpack('Diploma')
        elif state != 7 and state != 8 and Backpack["Diploma"] == 0:
            tk.Label(self, text = d1_SS_Library_Yes[state], font=('Helvetica', 20, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_SS_Library_Yes[state + 8], font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Social_Science_Library_Yes)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        elif state != 7 and state != 8 and Backpack["Diploma"] == 1:
            tk.Label(self, text = "社科圖關門了!!!", font=('Helvetica', 30, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "Back to Campus", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        state += 1
class Social_Science_Library_No(tk.Frame):
    def __init__(self, master):
        global state
        tk.Frame.__init__(self, master)
        if state == 4 and Backpack["Diploma"] == 0:
            tk.Label(self, text = d1_SS_Library_No[state], font=('Helvetica', 20, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_SS_Library_No[state + 4], font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Social_Science_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
        elif state != 4 and Backpack["Diploma"] == 0:
            tk.Label(self, text = d1_SS_Library_No[state], font=('Helvetica', 20, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_SS_Library_No[state + 4], font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Social_Science_Library_No)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        elif state != 4 and Backpack["Diploma"] == 1:
            tk.Label(self, text = "社科圖關門了!!!", font=('Helvetica', 30, "bold"),bg='aqua').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = "Back to Campus", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        state += 1
class Social_Science_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "社科院", font=('Helvetica', 40, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Label(self, text = "要去哪裡?", font=('Helvetica', 40, "bold"),bg='red').grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="王道一的教室", font=('Helvetica', 20, "bold"), command=lambda: master.switch_frame(Social_Science_Wang)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="林明仁的教室", font=('Helvetica', 20, "bold"), command=lambda: master.switch_frame(Social_Science_Lin)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="吳聰敏的教室", font=('Helvetica', 20, "bold"), command=lambda: master.switch_frame(Social_Science_Wu)).grid(row=4, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="回到社科圖", font=('Helvetica', 20, "bold"), command=lambda: master.switch_frame(Social_Science_Library)).grid(row=5, column=0, columnspan=2, sticky="nsew")
bline = ""
cline = ""
d1_Social_Science = dict()
d2_Social_Science = dict()
d3_Social_Science = dict()
d1_Social_Science = {1:"我是王道一", 2:"人們在面對全然陌生的選擇時", 3:"很難第一次就上手、做到最佳化",
        4:"而且除了容易有隨機、不小心的錯誤之外",5:"還會受到認知、先入為主的",6:"成見、文化背景等因素影響\n而產生「有系統的偏誤」",
        7:"以致於偏離經濟理論上的均衡預測",8:"但是，實驗結果也顯示人們\n得知做決定所產生的結果之後",9:"會嘗試增進他們的決策品質\n「學習」做更好的選擇", 10:"進而逼近經濟理論上的最佳解"}
d2_Social_Science = {1:"我是林明仁\n啊你們一定要知道芝加哥的經濟學派...", 2:"(" + "拿出他跟一堆不認識但好像很有名的人的合照" + ")", 3:"《自由的窄廊》 與《國家為什麼會失敗》\n這兩本書你們一定要看",
        4:"在自由民主正處於\n過去五十年來遭受最多質疑的年代",5:"這兩本書仍然是鼓勵我們思考如何對抗極權\n捍衛自由最有力的兩本經典",6:"就讓我以羅賓森在討論此議題時最愛引用的\n美國開國元勛富蘭克林的名言",
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
        tk.Label(self, text = d1_Social_Science[state], font=('標楷體', 19, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
        if state != 10:
            tk.Button(self, text = "Next", font=('Helvetica', 25, "bold"), command = lambda: master.switch_frame(Social_Science_Wang)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        elif state == 10 and bline.find("1") != -1 and bline.find("2") != -1 and bline.find("3") != -1 and cline.find("4") == -1:
            tk.Button(self, text = "早知道上王道一的課這麼無聊，去玩貓就好了" + "\n想去社科院找貓...", font=('Helvetica', 18, "bold"),command = lambda: [messagebox.showinfo(title = "訊息框", message = "恭喜你上完三位老師的課!" + "\n去社科院找貓吧!"), master.switch_frame(No_ID_Cat)]).grid(row=1, column=0, columnspan=2, sticky="nsew")
            cline += "4"
            state = 0
        else:
            tk.Button(self, text = "早知道上王道一的課這麼無聊，就去上林明仁的課就好了" + "\nBack to Social Science", font=('Helvetica', 18, "bold"),command = lambda: master.switch_frame(Social_Science_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
        state += 1
class Social_Science_Lin(tk.Frame):
    def __init__(self, master):
        global state
        global bline
        global cline
        bline += "2"
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d2_Social_Science[state], font=("標楷體", 20, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
        if state != 10:
            tk.Button(self, text = "Next", font=('Helvetica', 25, "bold"), command = lambda: master.switch_frame(Social_Science_Lin)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        elif state == 10 and bline.find("1") != -1 and bline.find("2") != -1 and bline.find("3") != -1 and cline.find("4") == -1:
            tk.Button(self, text = "早知道上林明仁的課這麼無聊，去玩貓就好了" + "\n想去社科院找貓...", font=('Helvetica', 18, "bold"),command = lambda: [messagebox.showinfo(title = "訊息框", message = "恭喜你上完三位老師的課!" + "\n去社科院找貓吧!"), master.switch_frame(No_ID_Cat)]).grid(row=1, column=0, columnspan=2, sticky="nsew")
            cline += "4"
            state = 0
        else:
            tk.Button(self, text = "早知道上林明仁的課這麼無聊，就去上吳聰敏的課就好了" + "\nBack to Social Science", font=('Helvetica', 18, "bold"),command = lambda: master.switch_frame(Social_Science_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
        state += 1
class Social_Science_Wu(tk.Frame):
    def __init__(self, master):
        global state
        global bline
        global cline
        bline += "3"
        tk.Frame.__init__(self, master)
        tk.Label(self, text = d3_Social_Science[state], font=('標楷體', 20, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
        if state != 10:
            tk.Button(self, text = "Next", font=('Helvetica', 25, "bold"), command = lambda: master.switch_frame(Social_Science_Wu)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        elif state == 10 and bline.find("1") != -1 and bline.find("2") != -1 and bline.find("3") != -1 and cline.find("4") == -1:
            tk.Button(self, text = "早知道上吳聰敏的課這麼無聊，去玩貓就好了" + "\n想去社科院找貓...", font=('Helvetica', 18, "bold"),command = lambda: [messagebox.showinfo(title = "訊息框", message = "恭喜你上完三位老師的課!" + "\n去社科院找貓吧!"), master.switch_frame(No_ID_Cat)]).grid(row=1, column=0, columnspan=2, sticky="nsew")
            cline += "4"
            state = 0
        else:
            tk.Button(self, text = "早知道上吳聰敏的課這麼無聊，就去上王道一的課就好了" + "\nBack to Social Science", font=('Helvetica', 18, "bold"),command = lambda: master.switch_frame(Social_Science_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
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
        tk.Frame.__init__(self, master)
        if state == 3:
            tk.Label(self, text = d1_No_ID_Cat[state], font=('標楷體', 20, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_No_ID_Cat[state + 4], font=('Helvetica', 20, "bold"),command=lambda: [messagebox.showinfo(title = "訊息框", message = "拿到了沾滿貓咪口水的管中閔畢業證書!"), master.switch_frame(No_ID_Cat)]).grid(row=1, column=0, columnspan=2, sticky="nsew")
        elif state == 4:
            tk.Label(self, text = d1_No_ID_Cat[state], font=('標楷體', 20, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_No_ID_Cat[state + 4], font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="nsew")
            state = 0
            Change_Backpack('Diploma')
        else:
            tk.Label(self, text = d1_No_ID_Cat[state], font=('標楷體', 20, "bold"),bg='lawngreen').grid(row=0, column=0, columnspan=2, sticky="nsew")
            tk.Button(self, text = d1_No_ID_Cat[state + 4], font=('Helvetica', 20, "bold"),command=lambda: master.switch_frame(No_ID_Cat)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        state += 1

class Multi_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="諾大的大廳裡，大家都抱著一台電腦\n準備去上今天的商管程，只有你在那邊發呆", font=('標楷體', 20)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=1, column=0, columnspan=2, sticky="n" + "e" + "s" + "w")


class Multi_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="販賣機", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_sale)).grid(row=0, column=0, columnspan=3, sticky="nsew")
        tk.Button(self, text="綜合大講堂", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Audi)).grid(row=0, column=3, columnspan=3, sticky="nsew")
        tk.Button(self, text="討論室", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=1, column=0, columnspan=3, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=1, column=3, columnspan=3, sticky="nsew")

class Kong(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="請寫出一段可以印出“Hello World.”的程式", font=('標楷體', 25, "bold")).grid(row=0, column=0, columnspan=5, sticky="n"+"e"+"s"+"w")
        tk.Label(self, text="輸入").grid(row=1, column=0,columnspan=1, sticky="n"+"e"+"s"+"w")
        self.print_ = tk.StringVar()
        content = tk.Entry(self, textvariable=self.print_)
        content.grid(row=1, column=1, columnspan=4, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Ok",
                      command=self.Input).grid(row=2, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                      command=lambda: master.switch_frame(Multi_Audi_Talk)).grid(row=3, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")

    def Input(self):
        if  self.print_.get() == "print(\"Hello World.\")" or self.print_.get() == "print(\'Hello World.\')":
            tk.Label(self, text="AC", font=('Helvetica', 25, "bold")).grid(row=4, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")
        else:
            tk.Label(self, text="WA", font=('Helvetica', 25, "bold")).grid(row=4, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")


Lu_Dialogue = {1:"好來，今天我們要教的東西吼。",2:"ㄜ...那個",3:"那個....",4:"我剛剛恍神了，我們重來一次。",5:"BlaBlaBla...",6:"我們今天的課程就到這邊結束。",7:"請按下Cancel回到上一頁"}
Lu_Dialogue_State = 1
class Lu(tk.Frame):
    def __init__(self, master):
        global Lu_Dialogue_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Lu_Dialogue[Lu_Dialogue_State], font=('標楷體', 20, "bold")).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")

        if Lu_Dialogue_State < 7:
            tk.Button(self, text="Next", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Lu)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        if Lu_Dialogue_State >= 7:
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                    command=lambda: master.switch_frame(Multi_Audi_Talk)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        Lu_Dialogue_State += 1
        if Lu_Dialogue_State >= 7:
            Lu_Dialogue_State = 7

class Multi_Audi(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="綜合大講堂", font=('Helvetica', 50, "bold")).grid(row=0, column=0, columnspan=6, sticky="nsew")
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Audi_Look)).grid(row=1, column=0, columnspan=3, sticky="nsew")
        tk.Button(self, text="talk", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Audi_Talk)).grid(row=1, column=3, columnspan=3, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=2, column=0, columnspan=6, sticky="nsew")


class Multi_Audi_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="孔令傑", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Kong)).grid(row=0, column=0,columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="盧信銘", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Lu)).grid(row=0, column=3,columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Multi_Audi)).grid(row=1, column=0,columnspan=6, sticky="n"+"e"+"s"+"w")

class Multi_sale(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="販賣機", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Label(self, text="請投入硬幣", font=('Helvetica', 20)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        coin_have = Check_Thing("Coin")
        if coin_have == 1:
            tk.Button(self, text="投入", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_sale2)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=2, column=0, columnspan=2, sticky="nsew")

class Multi_sale2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="販賣機", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Label(self, text="請輸入商品代碼", font=('Helvetica', 15)).grid(row=1, column=0, columnspan=4, sticky="nsew")
        self.var = tk.IntVar()
        merchan = tk.Entry(self, textvariable=self.var)
        merchan.grid(row=2, column=0, columnspan=2, sticky="nsew")
        button = tk.Button(self, text="Enter", font=('Helvetica', 25, "bold"), command=self.get_item)
        button.grid(row=2, column=2, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=3, column=0, columnspan=4, sticky="nsew")

    def get_item(self):
        if self.var.get() == 4143:
            messagebox.showinfo("Congrats!", "你獲得一張沒用印的校長聘書")
            Change_Backpack("Contract")
            self.master.switch_frame(Lead_him_to_next_scene)

        else:
            messagebox.showinfo("像話嗎", "沒認真上課還敢喝飲料啊")


class Lead_him_to_next_scene(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="寫程式真是累人啊\n休息是為了走更長遠的路\n回去水源宿舍睡覺吧", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="confirm", command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="nsew")

class Multi_conver(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Button(self, text="討論室A", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="討論室B", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converB)).grid(row=1, column=2, columnspan=2, sticky="nsew")
        tk.Button(self, text="討論室C", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converC)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="討論室D", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converD)).grid(row=2, column=2, columnspan=2, sticky="nsew")
        tk.Button(self, text="討論室E", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converE)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=3, column=2, columnspan=2, sticky="nsew")


class Multi_converA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室A", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子A", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子B", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子C", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA_tableC)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_converB(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室B", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子A", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子B", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子C", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_converC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室C", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子A", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子B", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子C", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_converD(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室D", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子A", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子B", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子C", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_converE(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="討論室E", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子A", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子B", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="桌子C", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_table(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌子", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Look_normaltable)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Use", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Use_normaltable)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Get", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_get_normaltable)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_Use_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="電腦", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Use_normaltable_computer)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")


class Multi_Look_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌上只有一個別人的電腦和一枚十元硬幣", font=('Helvetica', 20, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")


class Multi_Use_normaltable_computer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="不亂使用別人的電腦\n是\n\"基本禮貌\"\n吧?", font=('Helvetica', 40, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")


class Multi_get_normaltable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="硬幣", font=('Helvetica', 25, "bold"), command=self.get_coin).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_table)).grid(row=1, column=0, columnspan=2, sticky="nsew")


    def get_coin(self):
        tk.messagebox.showinfo("Congrats!", "你\"借到\"了一枚十元硬幣")
        Change_Backpack("Coin")

    # 但我這裡還沒有寫獲得多次硬幣的情況，只先把畫面寫出來而已

class Multi_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌子", font=('Helvetica', 30, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Look_converA_tableC)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Get", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_get_ACtable)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Use", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Use_converA_tableC)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_conver)).grid(row=4, column=0, columnspan=2, sticky="nsew")


class Multi_get_ACtable(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="硬幣", font=('Helvetica', 30, "bold"), command=self.get_coin).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA_tableC)).grid(row=1, column=0, columnspan=2, sticky="nsew")

    def get_coin(self):
        messagebox.showinfo("Congrats!", "你\"借到\"了一枚十元硬幣")
        Change_Backpack("Coin")



class Multi_Look_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="桌上只有一個電腦和一枚十元硬幣", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="電腦", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_Look_computer_converA_tableC)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA_tableC)).grid(row=2, column=0, columnspan=2, sticky="nsew")


class Multi_Use_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="電腦", font=('Helvetica', 30, "bold"), command=lambda: master.switch_frame(Multi_Use_converA_tableC_computer)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA_tableC)).grid(row=1, column=0, columnspan=2, sticky="nsew")


class Multi_Look_computer_converA_tableC(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="電腦", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Label(self, text="一台亮著的電腦，上面的程式似乎是可以使用的", font=('Helvetica', 19, "bold")).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA_tableC)).grid(row=2, column=0, columnspan=2, sticky="nsew")

class Multi_Use_converA_tableC_computer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="文字轉換器", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Label(self, text="剛剛上課夠認真，應該知道答案是什麼吧", font=('Helvetica', 15)).grid(row=1, column=0, columnspan=4, sticky="nsew")
        self.ord = tk.StringVar()
        ord_content = tk.Entry(self, textvariable=self.ord)
        ord_content.grid(row=2, column=0, columnspan=2, sticky="nsew")
        button = tk.Button(self, text="Enter", font=('Helvetica', 25, "bold"), command=self.ord_correct)
        button.grid(row=2, column=2, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi_converA_tableC)).grid(row=3, column=0, columnspan=4, sticky="nsew")


    def ord_correct(self):
        if self.ord.get() == "AC":
            messagebox.showinfo("文字轉換器", "4143")
            tk.Label(self, text="若覺得渴的話不妨到飲料機看看", font=('Helvetica', 15)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        else:
            messagebox.showinfo("文字轉換器", "錯誤資訊，請稍後再輸入")
# 綜合大樓結束

class Administration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="行政大樓", font=('Helvetica', 50, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2, sticky="nsew")
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"),
        command=lambda: master.switch_frame(Administration_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Move", font=('Helvetica', 25, "bold"),
        command=lambda: master.switch_frame(Administration_Move)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
        command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")



class Counsel(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="心輔中心", font=('Helvetica', 50, "bold")).grid(row=0, column=0, columnspan=6, rowspan=2, sticky="nsew")
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel_Look)).grid(row=2, column=0, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Talk", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel_Talk)).grid(row=2, column=3, columnspan=3, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=3, column=0, columnspan=6, sticky="n"+"e"+"s"+"w")

class Campus_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)        
        tk.Button(self, text="綜合大樓", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Multi)).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="水源宿舍", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Dorm)).grid(row=0, column=2, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="社科圖", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Social_Science_Library)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="行政大樓", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Administration)).grid(row=1, column=2, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="心輔中心", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Counsel)).grid(row=2, column=0, columnspan=4, sticky="n"+"e"+"s"+"w")
        if Check_Thing('Diploma')==Check_Thing('Contract')==Check_Thing('Seal')==1:
            tk.Button(self, text="公車站", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Bus)).grid(row=3, column=0, columnspan=4, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=4, column=0, columnspan=4, sticky="n"+"e"+"s"+"w")

# 裝飾性對話開始

class Campus_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="寬闊的椰林大道上行人與腳踏車來來去去\n只有你還站在原地傻看。", font=('標楷體', 20, "bold")).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")

class Dorm_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="這裡就是太子學舍嗎?\n看起來是太子與他們的產地。", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")

class Multi_Audi_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="半圓形的大講堂，承載著許多人對程式的怨念。", font=('標楷體', 20, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Multi)).grid(row=1, column=0, columnspan=2, sticky="n" + "e" + "s" + "w")

class Administration_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="在傅鐘旁邊有出來戶外教學的小學生在玩\n喔對了，我的學生證又掉了。", font=('標楷體', 20, "bold")).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")

# 裝飾性對話結束

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
        tk.Label(self, text=Fudict[Fu_State], font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=1, column=0, columnspan=2, sticky="nsew")

# 此行後為行政大樓和心輔中心
class Administration_Move(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="校長室", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Principal_Office)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="教務處", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Academic_Office)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Administration)).grid(row=2, column=0, columnspan=2, sticky="nsew")

class Principal_Office(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="這裡什麼都沒有。", font=('Helvetica', 30, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 30, "bold"),
                  command=lambda: master.switch_frame(Administration_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")

class Academic_Office(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Talk", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Assistant)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Administration_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")

Assistant_Dialogue = {1:"請問要補辦學生證嗎？",2:"好了，這是您的學生證。",3:"請按下Cancel回到上一頁"}
Assistant_Dialogue_State = 1
class Assistant(tk.Frame):
    def __init__(self, master):
        global Assistant_Dialogue_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Assistant_Dialogue[Assistant_Dialogue_State], font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        if Assistant_Dialogue_State < 3:
            tk.Button(self, text="Next", font=('Helvetica', 25, "bold"), command=lambda: master.switch_frame(Assistant)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        if Assistant_Dialogue_State >= 3:
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Administration_Move)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        Assistant_Dialogue_State += 1
        if Assistant_Dialogue_State >= 3:
            Assistant_Dialogue_State = 3
        Change_Backpack('ID_Card')

class Counsel_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Secret of the World", font=('Helvetica', 35, "bold"),
                  command=lambda: master.switch_frame(Counsel_Clock)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel)).grid(row=1, column=0, columnspan=2, sticky="nsew")

Clock = {1:"你還不了解人生的真諦。",2:'你對人生的真諦似懂非懂。',3:'離真理只有一步之遙了。',4:"這裡已經沒辦法滿足你\n去更遠的地方看看吧！"}
Clock_State = 1
class Counsel_Clock(tk.Frame):
    def __init__(self, master):
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Clock[Clock_State], font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel_Look)).grid(row=1, column=0, columnspan=2, sticky="nsew")
 
class Counsel_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='請依序和三位心理學家對話。', font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="佛洛依德", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Freud)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="皮亞傑", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Piaget)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="馬斯洛", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Maslow)).grid(row=3, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel)).grid(row=4, column=0, columnspan=2, sticky="nsew")

Freud_Dialogue = {1:"人的精神或人格主要分為三個部分：",2:"分別是本我、超我、自我",3:"當你在街上扶老奶奶過馬路時是哪一個呢？",4:"請按下Cancel回到上一頁"}
Freud_Dialogue_State = 1
class Freud(tk.Frame):
    def __init__(self, master):
        global Freud_Dialogue_State
        global Clock_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Freud_Dialogue[Freud_Dialogue_State], font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        if Freud_Dialogue_State < 4:
            tk.Button(self, text="Next", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Freud)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        if Freud_Dialogue_State >= 4:
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel_Talk)).grid(row=1, column=0, columnspan=2, sticky="nsew")
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
        tk.Label(self, text=Piaget_Dialogue[Piaget_Dialogue_State], font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        if Piaget_Dialogue_State < 5:
            tk.Button(self, text="Next", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Piaget)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        if Piaget_Dialogue_State >= 5:
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel_Talk)).grid(row=1, column=0, columnspan=2, sticky="nsew")
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
        tk.Label(self, text=Maslow_Dialogue[Maslow_Dialogue_State], font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        if Maslow_Dialogue_State < 3:
            tk.Button(self, text="Next", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Maslow)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        if Maslow_Dialogue_State >= 3:
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Counsel_Talk)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        Maslow_Dialogue_State += 1
        if Maslow_Dialogue_State >= 3:
            Maslow_Dialogue_State = 3
        if Clock_State < 4:
            Clock_State += 1

class Bus(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Bus", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Button(self, text="Look", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus_Look)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Talk", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus_Talk)).grid(row=1, column=2, columnspan=2, sticky="nsew")
        tk.Button(self, text="Use", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus_Use)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Campus)).grid(row=2, column=2, columnspan=2, sticky="nsew")

class Bus_Look(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="這裡只有一位司機", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus)).grid(row=1, column=0, columnspan=2, sticky="nsew")

class Bus_Talk(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="司機", font=('Helvetica', 25, "bold"),command=lambda: master.switch_frame(Bus_Driver)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus)).grid(row=1, column=0, columnspan=2, sticky="nsew")

class Bus_Driver(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="請把有價值的東西交給我", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus)).grid(row=1, column=0, columnspan=2, sticky="nsew")
class Bus_Use(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        if Check_Thing('Contract')==1:
            tk.Button(self, text="聘書", font=('Helvetica', 25, "bold"),
              command=lambda: master.switch_frame(Bus_Use_Contract)).grid(row=0, column=0, columnspan=2, sticky="nsew")
        if Check_Thing('Seal')==1:
            tk.Button(self, text="印章", font=('Helvetica', 25, "bold"),
              command=lambda: master.switch_frame(Bus_Use_Seal)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        if Check_Thing('Diploma')==1:
            tk.Button(self, text="畢業證書", font=('Helvetica', 25, "bold"),
              command=lambda: master.switch_frame(Bus_Use_Diploma)).grid(row=2, column=0, columnspan=2, sticky="nsew")
        if Check_Thing('Diploma')==Check_Thing('Contract')==Check_Thing('Seal')==-1:
            tk.Button(self, text="遊戲結束，請進結算畫面", font=('Helvetica', 25, "bold"),
              command=lambda: master.switch_frame(Game_Over)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        if Check_Thing('Diploma')!=-1 or Check_Thing('Contract')!=-1 or Check_Thing('Seal')!=-1:
            tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                      command=lambda: master.switch_frame(Bus)).grid(row=3, column=0, columnspan=2, sticky="nsew")
class Bus_Use_Contract(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="謝謝你幫我找回聘書", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus_Use)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        Use_Thing('Contract')
class Bus_Use_Seal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="謝謝你幫我找回印章", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus_Use)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        Use_Thing('Seal')
class Bus_Use_Diploma(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="謝謝你幫我找回畢業證書", font=('Helvetica', 25, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="Cancel", font=('Helvetica', 25, "bold"),
                  command=lambda: master.switch_frame(Bus_Use)).grid(row=1, column=0, columnspan=2, sticky="nsew")
        Use_Thing('Diploma')
class Game_Over(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="謝謝大家，校長回來了，下次再見", font=('Helvetica', 20, "bold")).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self, text="謝天謝地商管程終於結束了", font=('Helvetica', 20, "bold"),
                  command=self.quit).grid(row=1, column=0, columnspan=2, sticky="nsew")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
