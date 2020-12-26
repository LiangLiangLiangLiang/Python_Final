class Kong(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="請寫出一段可以印出“Hello World.”的程式", font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=5, sticky="n"+"e"+"s"+"w")
        tk.Label(self, text="輸入").grid(row=1, column=0,columnspan=1, sticky="n"+"e"+"s"+"w")
        self.print_ = tk.StringVar()
        content = tk.Entry(self, bg="black", fg="white", textvariable=self.print_)
        content.grid(row=1, column=1, columnspan=4, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Ok",
                      command=self.Input).grid(row=2, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")
        tk.Button(self, text="Cancel",
                      command=lambda: master.switch_frame(Multi_Audi_Talk)).grid(row=3, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")

    def Input(self):
        if  self.print_.get() == "print(\"Hello World.\")" or self.print_.get() == "print(\'Hello World.\')":
            tk.Label(self, text="AC", font=('Helvetica', 18, "bold")).grid(row=4, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")
        else:
            tk.Label(self, text="WA", font=('Helvetica', 18, "bold")).grid(row=4, column=0,columnspan=5, sticky="n"+"e"+"s"+"w")


Lu_Dialogue = {1:"好來，今天我們要教的東西吼。",2:"ㄜ...那個",3:"那個....",4:"我剛剛恍神了，我們重來一次。",5:"BlaBlaBla...",6:"我們今天的課程就到這邊結束。",7:"請按下Cancel回到上一頁"}
Lu_Dialogue_State = 1
class Lu(tk.Frame):
    def __init__(self, master):
        global Lu_Dialogue_State
        tk.Frame.__init__(self, master)
        tk.Label(self, text=Lu_Dialogue[Lu_Dialogue_State], font=('Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="n"+"e"+"s"+"w")

        if Lu_Dialogue_State < 7:
            tk.Button(self, text="Next",command=lambda: master.switch_frame(Lu)).grid(row=1, column=0, columnspan=1, sticky="n"+"e"+"s"+"w")
        if Lu_Dialogue_State >= 7:
            tk.Button(self, text="Cancel",
                    command=lambda: master.switch_frame(Multi_Audi_Talk)).grid(row=1, column=1, columnspan=2, sticky="n"+"e"+"s"+"w")
        Lu_Dialogue_State += 1
        if Lu_Dialogue_State >= 7:
            Lu_Dialogue_State = 7
