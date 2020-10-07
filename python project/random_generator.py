import tkinter as tk
import random

root=tk.Tk()
root.title("Guessing Random number")
root.resizable(0,0)

# width and height of application
width=500
height=600
root.geometry(f"{width}x{height}")

title_lbl=tk.Label(root,text="Guessing Number",font=('times new roman',30,'bold'),bg='grey',fg='white')
title_lbl.pack()

# variable
var=tk.IntVar()

guessnumber_lbl=tk.Label(root,text="Guess the number between 1 and 100",font=('times new roman',20,'bold'),fg='blue')
guessnumber_lbl.place(x=50,y=70)

# display error message 
guess_l=tk.Label(root,text="",font=('times new roman,',18,'bold'))
guess_l.place(x=30,y=80)

#  show result message
result_msg=tk.Label(root,text="",font=('times new roman,',18,'bold'))
result_msg.place(x=30,y=140)

guessing_number_frame=tk.Frame(root)
guessing_number_frame.place(x=100,y=200)

gn_lbl=tk.Label(guessing_number_frame,text="Guess Number",font=("times new roman",15,'bold'))
gn_lbl.grid(row=1,column=0)

gn_ent=tk.Entry(guessing_number_frame,textvariable=var,width=5,font=('times new roman,',15,'bold'))
gn_ent.grid(row=1,column=1)

count=0
num=random.randint(1,100)
def action():
    global count
    global num
    n=var.get()
    if(n==num):
        message=f"Congratulation! \n you win and it took {count} times."
        guess_l.place_forget()
        result_msg.place_forget()
        result_msg.place(x=30,y=100)
    elif(num>n):
        message="your number is smaller than destination number "
        count+=1
    else:
        message=" your number is larger  than destination number "
        count+=1
    
    guessnumber_lbl.place_forget()
    result_msg.config(text=f"{message}",fg='green')
    guess_l.config(text="Guess number again !",fg="red")
    


btn=tk.Button(root,text='click me',font=("new times roman",15,'bold'),command=action,padx=50)
btn.place(x=150,y=300)


root.mainloop()