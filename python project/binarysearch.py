import tkinter as tk
import random


root=tk.Tk()

root.title("Binary Search ")
root.geometry(f"{400}x{500}")

head_lbl=tk.Label(root,text='Binary Search Tree',font=('new times roman',20,'bold'),bg='yellow')
head_lbl.pack()

# range random number in list
list_ofNumber=random.sample(range(1,100),10)
list_ofNumber.sort()
array_lbl=tk.Label(root,text=f"{list_ofNumber}",font=('new times roman',15,'bold'))
array_lbl.place(x=10,y=80)

frame_=tk.Frame(root)
frame_.place(x=70,y=140)

number_lbl=tk.Label(frame_,text="Enter Number",font=('new times roman',15))
number_lbl.grid(row=0,column=0)

var=tk.IntVar()
number_entry=tk.Entry(frame_,textvariable=var,font=('new times roman',15),width=5)
number_entry.grid(row=0,column=1)

message_lbl=tk.Label(root,text="",font=('new times roman',35),fg='blue')
message_lbl.place(x=100,y=300)

count=0
def action(arr,low,high):
    global count
    if(high>=low):
        mid=(low+high)//2
        if(arr[mid]==var.get()):
            message_lbl.config(text="FOUND")
        elif(arr[mid]>var.get()):
            action(arr,low,mid-1)
        elif(arr[mid]<var.get()):
            action(arr,mid+1,high)
    else:
        message_lbl.config(text="NOT FOUND")


submit_btn=tk.Button(root,text="Find",bg='green',padx=50,pady=10,command=lambda :action(list_ofNumber,0,len(list_ofNumber)-1))
submit_btn.place(x=110,y=200)
root.mainloop()