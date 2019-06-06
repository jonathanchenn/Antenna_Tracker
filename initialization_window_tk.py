#creating a popup for ground station init.
#First attempt at making initilization slightly less terrible
#6/4/2019
#Michael Valentino-Manno
from tkinter import *
master = Tk()

#If every box is clicked, close window
def isDone():
    if var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and var5.get() == 1 and var6.get() == 1 and var7.get() == 1 and var8.get() == 1 and var9.get() == 1:
        master.destroy()

#this section deals with setting up each button in the window and their positions
Label(master, text="Ground Station Initialization").grid(row=0, sticky=W)
var1=IntVar()
Checkbutton(master,text="Plug in USBs", variable=var1).grid(row=1,sticky=W)

var2=IntVar()
Checkbutton(master,text="Move antenna to center", variable=var2).grid(row=2,sticky=W)

var3=IntVar()
Checkbutton(master,text="Enter IMEI #", variable=var3).grid(row=3,sticky=W)

var4=IntVar()
Checkbutton(master,text="Search", variable=var4).grid(row=4,sticky=W)

var5=IntVar()
Checkbutton(master,text="Move antenna to center", variable=var5).grid(row=5,sticky=W)

var6=IntVar()
Checkbutton(master,text="Update settings", variable=var6).grid(row=6,sticky=W)

var7=IntVar()
Checkbutton(master,text="Move IMU", variable=var7).grid(row=7,sticky=W)

var8=IntVar()
Checkbutton(master,text="Select iridium", variable=var8).grid(row=8,sticky=W)

var9=IntVar()
Checkbutton(master,text="Start auto-tracking", variable=var9).grid(row=9,sticky=W)


Button(master, text='Done',command=isDone).grid(row=10,sticky=W, pady=4)

mainloop()



