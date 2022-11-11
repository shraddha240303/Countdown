import time
from tkinter import *
from tkinter import messagebox

# window creation
wnd = Tk()
wnd.geometry("300x300")
wnd.title("Countdown")

# for getting the inputs
hrs = StringVar()
mins = StringVar()
secs = StringVar()

# default setting
hrs.set("00")
mins.set("00")
secs.set("00")

# Entry and labeling of Hours
hrs_Entry = Entry(wnd, width = 3, font = ("Arial", 18,""), textvariable = hrs)
hrs_Entry.place(x = 80, y = 20)
lbl_1 = Label(wnd, text = 'Hrs')
lbl_1.place(x = 87, y = 53)

# Entry and labeling of Minutes
mins_Entry = Entry(wnd, width = 3, font = ("Arial", 18,""), textvariable = mins)
mins_Entry.place(x = 130, y = 20)
lbl_1 = Label(wnd, text = 'Mins')
lbl_1.place(x = 135, y = 53)

# Entry and labeling of Seconds
secs_Entry = Entry(wnd, width = 3, font = ("Arial", 18,""), textvariable = secs)
secs_Entry.place(x = 180, y = 20)
lbl_1 = Label(wnd, text = 'Secs')
lbl_1.place(x = 185, y = 53)

# giving default values
pause_1 = False
resume_1 = False
reset_1 = False

# start function
def start():
    try:
        conv = int(hrs.get())*3600 + int(mins.get())*60 + int(secs.get())       # converting the values in seconds
    except:
        print ("Enter the correct value")

    global pause_1
    global resume_1
    global reset_1
    
    while (conv > -1):
        mins_1 = conv // 60                 # getting minutes values
        secs_1 = conv % 60                # getting seconds values
        hrs_1 = 0                                 # getting hours values
        if (mins_1 > 60):
            hrs_1 = mins_1 // 60
            mins_1 = mins_1 % 60

        # updating the values
        hrs.set("{0:2d}".format(hrs_1))
        mins.set("{0:2d}".format(mins_1))
        secs.set("{0:2d}".format(secs_1))
        
        if (pause_1):                           # iterating the loop
            conv += 1

        wnd.update()
        time.sleep(1)

        if (conv == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")

        if (reset_1):                           # for reset the function
            pause_1 = False
            break

        if (resume_1):                      # for resume the function
            pause_1 = False

        conv -= 1
        
    reset_1 = False

def pause():
    global pause_1
    pause_1 = True

def resume():
    global resume_1
    resume_1 = True

def reset():
    hrs.set("00")
    mins.set("00")
    secs.set("00")
    global reset_1
    reset_1 = True

def stop():
    wnd.destroy()

# Labeling of features
lbl_4 = Label(wnd, text = 'FEATURES')
lbl_4.place(x = 125, y = 105)

# All the buttons
btn_1 = Button(wnd, text = 'Start', command = start)
btn_1.place(x = 80, y = 150)
btn_2 = Button(wnd, text = 'Reset', command = reset)
btn_2.place(x = 80, y = 200)
btn_3 = Button(wnd, text = 'Pause', command = pause)
btn_3.place(x = 180, y = 150)
btn_4 = Button(wnd, text = 'Resume', command = resume)
btn_4.place(x = 180, y = 200)
btn_5 = Button(wnd, text = 'Stop', command = stop)
btn_5.place(x = 133, y = 250)

# closing of the window
wnd.mainloop()
