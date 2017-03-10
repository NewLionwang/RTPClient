import argparse
import sys
import time

from Tkinter import *

class RTPClientApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("RTPClient")
        self.canvas = Canvas(self.root) #   create canvas for drawings
        
        #   Screen vars
        (wMax, hMax) = self.get_screen_size()
        (w, h) = (wMax / 2, hMax / 2)        
        self.wndwSize = (w, h)
        
        #   Update App Window
        self.root.config(width=w, height=h, bg='black')
        self.center_window()
                
        #   Create Widget Frames
        self.btnFrame = Frame(bg="gray10")
        self.vidFrame = Frame(bg="gray10")
        
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
    def get_screen_size(self):
        #   Returns the size (in pixels) of the current monitor
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        return (w, h)
        
    def get_wndw_size(self):
        #   Returns the size (in pixels) of the current app screen
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        return (w, h)
        
    def center_window(self, canvas = None):
        self.root.update()
        x = (self.root.winfo_screenwidth()/2) - (self.root.winfo_width()/2)
        y = (self.root.winfo_screenheight()/2) - (self.root.winfo_height()/2)
        self.root.geometry('%dx%d+%d+%d' % (self.wndwSize[0], self.wndwSize[1], x, y))
        
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
        #self.root.update()
        (w, h) = self.get_wndw_size()
        if (event is not None and self.wndwSize == (w, h)):
            return
            
        self.wndwSize = (w, h)

        self.btnFrame.config(width=w, height=.2*h)
        self.btnFrame.place(relx=0.5,rely=0.9, anchor="c")
        
        self.vidFrame.config(width=.8*w, height=.75*h)
        self.vidFrame.place(relx=0.5,rely=0.4, anchor="c")
        
        btnSize = (int(self.wndwSize[0] / 60), int(self.wndwSize[1] / 170))
        
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
        
def main(serverAddr, serverPort, rtpPort, fileName):

    app = RTPClientApp()
    app.root.mainloop()
    
if __name__ == "__main__":
    try:
        serverAddr = sys.argv[1]
        serverPort = sys.argv[2]
        rtpPort = sys.argv[3]
        fileName = sys.argv[4]
        main(serverAddr, serverPort, rtpPort, fileName)
    except:
        print "[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]"
        print "Launching in Debug mode."
        main(None, None, None, None)
