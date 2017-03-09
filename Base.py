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
        
        self.canvas.bind("<space>", self.center_window)
        
        #   Screen vars
        w = 0.8 * self.root.winfo_screenwidth()
        h = 0.8 * self.root.winfo_screenheight()
        self.screen = (w, h)
        
        #   Canvas Configuration
        self.canvas.configure(width=self.screen[0], height=self.screen[1], background='black')
        self.canvas.create_rectangle(0, 0, self.screen[0] - 1, self.screen[1] - 1, fill='black', tags='MainWin')
        self.canvas.pack(fill=BOTH, expand=YES)
        
        #   Update App Window
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.center_window()
                
        #   Create Widget Frames
        bFrame = Frame(width=w, height=.2*h, bg="gray5")
        bFrame.place(relx=0.5,rely=0.9, anchor="c")
        
        vFrame = Frame(width=.8*w, height=.6*h, bg="gray5")
        vFrame.place(relx=0.5,rely=0.4, anchor="c")
        
        #   Create Buttons
        btnSize = (int(self.screen[0] / 60), int(self.screen[1] / 170))
        
        b0 = Button(bFrame, text="Setup", command=self.btn_setup)
        b0.config(width=btnSize[0], height=btnSize[1])
        b0.place(relx=0.25, rely=0.5, anchor="c")
        
        b1 = Button(bFrame, text="Play", command=self.btn_play)
        b1.config(width=btnSize[0], height=btnSize[1])
        b1.place(relx=0.50, rely=0.5, anchor="c")
        
        b2 = Button(bFrame, text="Teardown", command=self.btn_teardown)
        b2.config(width=btnSize[0], height=btnSize[1])
        b2.place(relx=0.75, rely=0.5, anchor="c")
        
        self.btnSetup = b0
        self.btnPlayPause = b1
        self.btnTearDown = b2
        
        #   Attributes
        self.isPlaying = False
      
    #   Utilities
        
    def center_window(self, canvas = None):
        # calculate x and y coordinates for the Tk root window
        x = (self.root.winfo_screenwidth()/2) - (self.screen[0]/2)
        y = (self.root.winfo_screenheight()/2) - (self.screen[1]/2)
        
        # set the dimensions of the screen 
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.screen[0], self.screen[1], x, y))
        
    #   Events
    def btn_setup(self):
        print "setup"
        
    def btn_play(self):
        self.isPlaying = True
        self.btnPlayPause.config(command=self.btn_pause, text="Pause")
        print "play"
        
    def btn_pause(self):
        self.btnPlayPause.config(command=self.btn_play, text="Play")
        self.isPlaying = False
        print "pause"
        
    def btn_teardown(self):
        print "teardown"
        
def main():
    app = ClientWindow()
    app.root.mainloop()
    
if __name__ == "__main__":
   main()
