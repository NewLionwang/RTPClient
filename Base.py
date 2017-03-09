from Tkinter import *
import time

class ClientWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("ClientWindow")
        self.canvas = Canvas(self.root)
        self.canvas.focus_set() #   need to set the focus for any bindings to work
        
        #   Screen vars
        w = 0.5 * self.root.winfo_screenwidth()
        h = 0.5 * self.root.winfo_screenheight()
        self.screen = (w, h)
        
        #   Canvas Configuration
        self.canvas.configure(width=self.screen[0], height=self.screen[1], background='black')
        self.canvas.create_rectangle(0, 0, self.screen[0], self.screen[1], fill='black', tags='MainWin')
        self.canvas.pack(fill=BOTH, expand=YES)
        
        #   Update App Window
        self.root.update()
        self.center_window()
                
        #   Create Widget Frames
        self.btnFrame = Frame(bg="gray5")
        self.vidFrame = Frame(bg="gray5")
        
        #   Create Buttons
        self.btnSetup = Button(self.btnFrame, text="Setup", command=self.btn_setup)
        self.btnPlayPause = Button(self.btnFrame, text="Play", command=self.btn_play)
        self.btnTearDown = Button(self.btnFrame, text="Teardown", command=self.btn_teardown)
        
        #   Attributes
        self.isPlaying = False
        
        self.eventTimer_Btn = 0
        self.eventCD_Btn = 0.2
        
        #   Remaining Initializations
        self.resize()
        
        #   Bindings        
        self.root.bind("<space>", self.btn_play)
        self.root.bind("<Escape>", self.center_window)
        self.root.bind("<Configure>", self.resize)
      
    #   Utilities
    def get_max_screen(self):
        #   Returns the size (in pixels) of the current monitor
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        return (w, h)
        
    def get_current_screen(self):
        #   Returns the size (in pixels) of the current app screen
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        return (w, h)
        
    def center_window(self, canvas = None):
        x = (self.root.winfo_screenwidth()/2) - (self.root.winfo_width()/2)
        y = (self.root.winfo_screenheight()/2) - (self.root.winfo_height()/2)
        self.root.geometry('%dx%d+%d+%d' % (self.screen[0], self.screen[1], x, y))
        
    def click_is_valid(self):
        #   Curates button presses to cap the rate of button presses
        currTime = time.time()
        if (currTime - self.eventTimer_Btn >= self.eventCD_Btn):
            self.eventTimer_Btn = currTime
            return True
        return False
        
    #   Events
    def resize(self, event = None):
        #   Resizes the frames and widgets whenever the window screen size changes    
        (w, h) = self.get_current_screen()
        if (event is not None and self.screen == (w, h)):
            return
            
        self.screen = (w, h)

        self.btnFrame.config(width=w, height=.2*h)
        self.btnFrame.place(relx=0.5,rely=0.9, anchor="c")
        
        self.vidFrame.config(width=.8*w, height=.75*h)
        self.vidFrame.place(relx=0.5,rely=0.4, anchor="c")
        
        btnSize = (int(self.screen[0] / 60), int(self.screen[1] / 170))
        
        self.btnSetup.config(width=btnSize[0], height=btnSize[1])
        self.btnSetup.place(relx=0.25, rely=0.5, anchor="c")
        
        self.btnPlayPause.config(width=btnSize[0], height=btnSize[1])
        self.btnPlayPause.place(relx=0.50, rely=0.5, anchor="c")
        
        self.btnTearDown.config(width=btnSize[0], height=btnSize[1])
        self.btnTearDown.place(relx=0.75, rely=0.5, anchor="c")
    
    def btn_setup(self, event = None):
        if (not self.click_is_valid()):
            return
        print "setup"
        
    def btn_play(self, event = None):
        if (not self.click_is_valid()):
            return
        print "play"
            
        #   Flip play button into pause button
        self.isPlaying = True
        self.btnPlayPause.config(command=self.btn_pause, text="Pause")
        self.root.unbind("<space>")
        self.root.bind("<space>", self.btn_pause)
        
    def btn_pause(self, event = None):
        if (not self.click_is_valid()):
            return
        print "pause"
            
        #   Flip pause button into play button
        self.btnPlayPause.config(command=self.btn_play, text="Play")
        self.root.unbind("<space>")
        self.root.bind("<space>", self.btn_play)
        self.isPlaying = False
        
    def btn_teardown(self, event = None):
        if (not self.click_is_valid()):
            return
        print "teardown"
        
def main():
    app = ClientWindow()
    app.root.mainloop()
    
if __name__ == "__main__":
   main()
