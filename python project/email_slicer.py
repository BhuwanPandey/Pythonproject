import tkinter as tk

root=tk.Tk()
root.title("Email slicer")
root.geometry(f"{400}x{500}")

lbl1=tk.Label(root,text="Email Slicer",font=("new times roman",15,'bold'))
lbl1.pack()

email_lbl=tk.Label(root,text="Enter Email Address",font=("new times roman",15,'bold'))
email_lbl.place(x=20,y=100)
var=tk.StringVar()
email_entry=tk.Entry(root,textvariable=var,width=20,font=("new times roman",15,'bold'))
email_entry.place(x=20,y=130)

# message displayed
msg_lbl=tk.Label(root,text="",font=("new times roman",15,'bold'))
msg_lbl.place(x=40,y=200)

def action():
    value=var.get()
    # slice out username
    user_name=value[:value.index("@")]
    # slice the domain name
    domain_name=value[value.index("@")+1:]
    # Format message
    output = "Your username is '{}' \n your domain name is '{}'".format(user_name,domain_name)
    msg_lbl.config(text=output)

def clear():
    var.set("")
    msg_lbl.config(text="")


click_btn=tk.Button(root,text="CLick me",bg='yellow',fg='red',command=action)
click_btn.place(x=100,y=160)
clear_btn=tk.Button(root,text="Clear",bg='red',fg='blue',command=clear)
clear_btn.place(x=180,y=160)
root.mainloop()
