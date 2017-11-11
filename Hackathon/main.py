#!/usr/bin/python

from tkinter import *   
from _collections import OrderedDict

class start_window(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.pack(self)


#Build the sidebar on the right using another frame and various widgets
def addSidebar():
    #Create a frame to store everything and force it to keep the same size
    sidebar = Frame(width=200, height=200, bg="gray")
    sidebar.grid_propagate(False)
    
    #The default padding values
    padx = 10
    pady = 10
    
    #Create the top lave
    topLabel = Label(sidebar, text="Welcome! Please select your values below.", bg="gray")
    topLabel.pack(padx=padx)
    
    #Create the dropdown label and selection
    dowLabel = Label(sidebar, text="Day of the week:", bg="gray")
    dowLabel.pack(padx=padx, pady=pady)
    daysOfWeek = OrderedDict([("Sunday",0), ("Monday",1), ("Tuesday",2), ("Wednesday",3), ("Thursday",4), ("Friday",5), 
                              ("Saturday",6)])
    global dowDropdown 
    dowDropdown = StringVar(sidebar)
    dowDropdown.trace("w", onChange)
    dowDropdown.set("Sunday")
    dowOptionMenu = OptionMenu(sidebar, dowDropdown, *daysOfWeek)
    dowOptionMenu.pack(padx=padx)
    
    #Create the time entry label, selection, and input fields
    timeBar = Frame(sidebar, width=200, bg="gray")
    timeBar.grid_propagate(False)
    timeLabel = Label(sidebar, text="Time:", bg="gray")
    timeLabel.pack(padx=padx, pady=pady)
    timeOptions = OrderedDict([("1",0), ("2",1), ("3",2), ("4",3), ("5",4), ("6",5), ("7",6), ("8",7), ("9",8), 
                              ("10",9), ("11",10), ("12",11)]) 
    timeDropdown = StringVar(sidebar)
    timeDropdown.trace("w", onChange)
    timeDropdown.set("1")
    timeOptionMenu = OptionMenu(timeBar, timeDropdown, *timeOptions)
    timeOptionMenu.pack(padx=padx, side=LEFT)
    
    timeMinuteInput = Entry(timeBar)
    timeMinuteInput.insert(0, "00")
    timeMinuteInput.pack(side=LEFT)
    
    timeBar.pack()
    sidebar.pack(side=RIGHT, fill=Y)

def onChange(*args):
    print(dowDropdown.get())
    
if __name__ == '__main__':
    root = Tk()
    #TODO change the title
    root.wm_title("Title goes here")
    root.minsize(width=1200, height=800)
    root.maxsize(width=1200, height=800)
    start_window(root)
    addSidebar()
    root.mainloop()