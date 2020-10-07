import tkinter as tk
import random


class DiceRolling:
    def __init__(self,root):
        self.root=root
        self.root.title("Dice Rolling")
        self.root.geometry(f"{500}x{400}")
        self.root.resizable(0,0)

        title_lbl=tk.Label(self.root,text="Dice Rolling Game",font=('new times roman',20,'bold'))
        title_lbl.pack()

        self.lbl1=lbl1=tk.Label(self.root,text="Dice Rolling Simulation starting..",font=('new times roman',15,'bold'))
        lbl1.place(x=50,y=100)

        self.count=0

        # message label
        self.msg_lbl=msg_lbl=tk.Label(self.root,text="",fg='red')
        msg_lbl.place(x=100,y=150)

        self.btn=tk.Button(root,text="start",font=("new times roman",19,'bold'),padx=50,bg='green',command=self.start)
        self.btn.place(x=120,y=200)

        root.mainloop()

    def start(self):
        self.lbl1.config(text="Target Value:")
        self.target_var=target_var=tk.IntVar(value=random.randint(1,50))
        ene1=tk.Entry(self.root,textvariable=target_var,width=5,font=('new times roman',15,'bold'),state='readonly')
        ene1.place(x=190,y=100)

        self.msg_lbl.place_forget()
        self.btn.place_forget()
        self.lbl2=lbl2=tk.Label(self.root,text="Your total Score:",font=('new times roman',15,'bold'))
        lbl2.place(x=50,y=150)


        self.score_var=score_var=tk.IntVar(value=0)
        self.score_ent=score_ent=tk.Entry(self.root,textvariable=score_var,width=5,font=('new times roman',15,'bold'))
        score_ent.place(x=230,y=150)

        self.dice_lbl=dice_lbl=tk.Label(self.root,text="Dice Score:",font=('new times roman',15,'bold'))
        dice_lbl.place(x=320,y=150)

        self.dice_var=dice_var=tk.IntVar()
        self.dice_ent=dice_ent=tk.Entry(self.root,textvariable=dice_var,width=5,font=('new times roman',15,'bold'))
        dice_ent.place(x=430,y=150)
        
        self.quit_btn=quit_btn=tk.Button(self.root,text="Quit",font=("new times roman",15,'bold'),padx=13,bg='red',command=self.quit)
        quit_btn.place(x=50,y=250)

        self.dice_btn=dice_btn=tk.Button(self.root,text="Roll Dice",padx=10,font=("new times roman",15,'bold'),bg='yellow',command=self.rolldice)
        dice_btn.place(x=320,y=250)

    def quit(self):
        self.forget()


    def rolldice(self):
        self.dice_var.set(random.randint(1,6))
        val=self.score_var.get()+self.dice_var.get()
        if(val==self.target_var.get()):
            self.msg_lbl.config(text=f"Congratulation! It took {self.count} times.",font=("new times roman",15,'bold'))
            self.msg_lbl.place(x=100,y=150)
            self.forget()

        elif(val>self.target_var.get()):
            pass
        else:
            self.score_var.set(val)
        self.count+=1

    def forget(self):
        self.count=0
        self.quit_btn.place_forget()
        self.target_var.set(0)
        self.score_var.set(0)
        self.dice_var.set(0)
        self.lbl2.place_forget()
        self.score_ent.place_forget()
        self.dice_lbl.place_forget()
        self.dice_ent.place_forget()
        self.btn.place(x=120,y=200)
        self.dice_btn.place_forget()

DiceRolling(tk.Tk())
