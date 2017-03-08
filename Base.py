from Tkinter import *
from random import randint
import time
import thread

class ClientWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("ClientWindow")
        self.canvas = Canvas(self.root)
        self.canvas.focus_set() #   need to set the focus for any bindings to work
                
        #   Screen vars
        w = 0.8 * self.root.winfo_screenwidth()
        h = 0.8 * self.root.winfo_screenheight()
        self.screen = (w, h)
        
        #   Canvas Configuration
        self.canvas.configure(width=self.screen[0], height=self.screen[1], background='black')
        self.canvas.create_rectangle(0, 0, self.screen[0] - 1, self.screen[1] - 1, fill='black', tags='MainWin')
        self.canvas.pack(fill=BOTH, expand=YES)
                
        #   Frames
        bFrame = Frame(width=w, height=.2*h, bg="gray5")
        bFrame.place(relx=0.5,rely=0.9, anchor="c")
        
        vFrame = Frame(width=.8*w, height=.6*h, bg="gray5")
        vFrame.place(relx=0.5,rely=0.4, anchor="c")
        
        #   Buttons
        s = (25, 5)
        
        b0 = Button(bFrame, text="Setup", command=self.btn_setup) # state=DISABLED
        b0.config(width=s[0], height=s[1])
        b0.place(relx=0.2, rely=0.5, anchor="c")
        
        b1 = Button(bFrame, text="Play", command=self.btn_play) # state=DISABLED
        b1.config(width=s[0], height=s[1])
        b1.place(relx=0.4, rely=0.5, anchor="c")
        
        b2 = Button(bFrame, text="Pause", command=self.btn_pause) # state=DISABLED
        b2.config(width=s[0], height=s[1])
        b2.place(relx=0.6, rely=0.5, anchor="c")
        
        b3 = Button(bFrame, text="Teardown", command=self.btn_teardown) # state=DISABLED
        b3.config(width=s[0], height=s[1])
        b3.place(relx=0.8, rely=0.5, anchor="c")

        
    #   Control Events
    def btn_setup(self):
        print "setup button"
        
    def btn_play(self):
        print "play button"
        
    def btn_pause(self):
        print "pause button"
        
    def btn_teardown(self):
        print "teardown button"
        
def main():
    app = ClientWindow()
    app.root.mainloop()
    
if __name__ == "__main__":
   main()
