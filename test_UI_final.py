from multiprocessing import Process
import threading
from tkinter import Tk, BOTH, Text, TOP, X, LEFT, W, N, E, S,Listbox, StringVar, END
from tkinter.ttk import Frame,Button,Style,Label, Entry
from tkinter import *
import os
import datetime
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import importlib
import test_UI_boy
from test_UI_boy import *

class OnMyWatch:
    watchDirectory = "C:\ChatApplication"
    reciever=""
            
    def __init__(self):
        self.observer = Observer()
        #self.reciever= "girl"
        print("watchdog created")
        #self.watchDirectory="C:\\ChatApplication"+"\\"+ self.reciever
        #print(self.watchDirectory)
        self.run()
         
    def run(self):
        print("watchdog run")
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        print("observer started")
        try:
            while True:
                time.sleep(0.5)
        except:
            self.observer.stop()
            print("Observer Stopped")          
        self.observer.join()
          
          
class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
          
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)
            strng=event.src_path
            strPath = os.path.realpath(event.src_path)
            nmFolders = strPath.split( os.path.sep )
            print( "List of Folders:", nmFolders )
            print( nmFolders[-1] )
            print( nmFolders[-2] )
            print( nmFolders[-3] )
            sender=nmFolders[-2]
            #print(sender)
            reciever=nmFolders[-3]
            #print(reciever)

class Example(Frame):
    sender=""
    reciever=""
    
    def __init__(self, s="",r=""):
        super().__init__()
        print(s,r)
        self.sender=s
        self.reciever=r
        print(self.sender,self.reciever)
        self.initUI()

    def initUI(self):
        print("b")
        self.master.title("ChatApplication")
        #self.master.configure(bg="green")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        new_person_window = Toplevel()
        new_person_window.geometry('300x200')
        new_person_window.configure(bg="grey")
        new_person_window.withdraw()
        #sender=""
        #reciever=""
        def new_person_popup():
            new_person_window.deiconify()
    
        class NEW_PERSON: # new order class, simplified for example)
            def __init__(self, product_num):
                self.product_num = product_num
        
        def new_order(product_num):
            input_product_num = pro_num_entry.get()
            newOrder = NEW_PERSON(input_product_num)
            return newOrder

        
        quitButton = Button(self, text="NewPerson",command = lambda: new_person_popup())
        quitButton.grid(row=0, column=3)

        def option_changed1(*args):
            value=self.menu1.get()
            newperson=value
            path="C:\ChatApplication"
            files=[]
            for name in os.listdir(path):
                if name!=newperson:
                    files.append(name)
                    

        def sub_ex(): # same as other button but closes toplevel window.
            
            product_num2 = new_order(product_num=str)
            person_new= product_num2.product_num
            parent_dir = 'C:\\ChatApplication'
            files=[]
            for name in os.listdir(parent_dir):
                path = os.path.join(parent_dir, name, person_new)
                os.makedirs(path)
                fp = open(path+'\\'+'Read.txt', 'x')
                fp.close()
                fp = open(path+'\\'+'Unread.txt', 'x')
                fp.close()
                files.append(name)
                            
            directory = person_new
            
            path2 = os.path.join(parent_dir, directory)
            os.makedirs(path2)

            for file in files:
                path3=os.path.join(path2,file)
                os.makedirs(path3)
                fp = open(path3+'\\'+'Read.txt', 'x')
                fp.close()
                fp = open(path3+'\\'+'Unread.txt', 'x')
                fp.close()
            
            new_person_window.withdraw()
            files=[]
            path="C:\ChatApplication"
            for name in os.listdir(path):
                files.append(name)
                print(name)
            self.drop["menu"].delete(0, "end")
            self.menu= StringVar()
            for item in files:
                self.drop["menu"].add_command(label=item,command=lambda value=item: self.menu.set(value))
        
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        #defining the person1
        #lbl = Label(self, text=newperson)
        #lbl.grid(row=0, column=0,sticky=W, pady=4, padx=5)
        
        path="C:\ChatApplication"

        files=[]
        for name in os.listdir(path):
            files.append(name)
                
        self.menu1= StringVar()
        if self.sender=="":
            self.menu1.set(files[0])
        else:
            self.menu1.set(self.sender)
        self.menu1.trace("w",option_changed1)

        #Create a dropdown Menu
        self.drop1= OptionMenu(self, self.menu1, *files)
        self.drop1.grid(row=0, column=0,sticky=W, pady=4, padx=5)       

        txt = "There is no message. You can start a conversation"

        label1 = Message(self, text=txt)
        label1.grid(row=1,column=0,columnspan=2,rowspan=2,padx=5, sticky=E+W+S+N)
        #label1.pack()

        self.area = Text(self)
        self.area.grid(row=3, column=0, columnspan=3, rowspan=2,
            padx=5, sticky=E+W+S+N)

        obtn = Button(self, text="Send",command= self.save_text)
        obtn.grid(row=5, column=3)

        def option_changed(*args):
            print("the user chose the value {}".format(self.menu.get()))
            value=self.menu.get()
            newperson=self.menu1.get()
            st=(os.stat('C:\\ChatApplication\\'+ newperson +"\\"+ value+"\\"+ "Unread.txt").st_size == 0)
            if st== True:
                pt=(os.stat('C:\\ChatApplication\\'+ newperson +"\\"+ value+"\\"+ "Read.txt").st_size == 0)
                if pt==True:
                    txt="There is no message. You can start a conversation"
                else:
                    with open('C:\\ChatApplication\\'+ newperson +"\\"+ value+"\\"+ "Read.txt") as f:
                        for last_line in f:
                            pass
                        txt = last_line
            else:
                with open('C:\\ChatApplication\\'+ newperson +"\\"+ value+"\\"+ "Unread.txt") as fp:
                    txt=fp.readlines()
                with open('C:\\ChatApplication\\'+ newperson +"\\"+ value+"\\"+ "Read.txt", "a") as f:
                    f.writelines(txt)
                    f.close()
                with open('C:\\ChatApplication\\'+ newperson +"\\"+ value+"\\"+ "Unread.txt",'r+') as fp:
                    fp.truncate(0)
            print(txt)
            label1.config(text=txt)

        self.menu= StringVar()
        if self.reciever=="":
            self.menu.set(files[1])
        else:
            self.menu.set(self.reciever)
        self.menu.trace("w",option_changed)

        #Create a dropdown Menu
        self.drop= OptionMenu(self, self.menu, *files)
        self.drop.grid(row=1, column=3)

        list_label = Label(new_person_window)
        list_label.configure(text='Name')
        list_label.place(anchor=NW, x=15, y=15)

        pro_num_entry = Entry(new_person_window)
        pro_num_entry.configure(width=20)
        pro_num_entry.place(anchor=NW, x=100, y=15)
        
        submit_exit_button = Button(new_person_window)
        submit_exit_button.configure(text='Submit', command = lambda: sub_ex())
        submit_exit_button.place(anchor=NW, x=100, y=100)
        
    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.var.set(value)
        print(value)   
        
        
    def save_text(self):
        value= self.menu.get()
        newperson=self.menu1.get()
        text_file = open('C:\\ChatApplication\\'+value+'\\'+newperson+'\\Unread.txt', "a")
        text_file.write("\n")
        text_file.writelines(self.area.get(1.0, END))
        text_file.close()
        self.area.delete("1.0", "end")
        #creation of popup
        popup = Tk()
        popup.wm_title("!")
        labela = Label(popup, text=value+" you got a msg from " + newperson)
        labela.place(anchor=NW, x=20, y=20)            
        B1 = Button(popup)
        B1.configure(text='okay', command = popup.destroy)
        B1.place(anchor=NW, x=100, y=100)
        self.menu1.set(value)
        self.menu.set(newperson)
        popup.mainloop()
        

    def centerWindow(self):

        w = 350
        h = 300

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():

    root = Tk()
    root.geometry("500x500+500+500")
    watchdog = threading.Thread(target=OnMyWatch, name="Watchdog",daemon=True)
    
    #ex= threading.Thread(target=Example,name="ex", daemon=True)
    watchdog.start()
    ex = Example()
    root.mainloop()


if __name__ == '__main__':
    
    #main()
    root= main()

