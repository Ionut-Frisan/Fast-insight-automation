import tkinter
from tkinter import ttk, messagebox
import RUN
import time
import random
import generate_code
import threading
import multiprocessing
from queue import Queue
import os,sys

Exit = False

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fast Insight")
        self.geometry("200x150")
        self.initUI()
        self.minsize(200, 150)
        self.iconbitmap("mcds.ico")
        self.exit = False
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def initUI(self):
        self.Label = ttk.LabelFrame(self)
        self.LabelNewText = ttk.LabelFrame(self)

        self.Cod = ttk.Entry(self.Label)
        self.NrRuns = ttk.Entry(self.Label)
        self.RunB = ttk.Button(self.Label, text="Start!", command= lambda :threading.Thread(target=self.run).start())
        self.NewText = ttk.Entry(self.LabelNewText)
        self.AddText = ttk.Button(self.LabelNewText, text="Adauga!")
        self.CloseB = ttk.Button(self.Label, text = "Exit!", command=self.destroy)

        self.NewText.insert(0,"Adauga merite noi")
        self.Cod.insert(0,"Cod")
        self.NrRuns.insert(0,"Numar sondaje")
        self.Cod.bind("<FocusIn>", lambda args: self.Cod.delete('0', 'end'))
        self.NrRuns.bind("<FocusIn>", lambda args: self.NrRuns.delete('0', 'end'))
        self.NewText.bind("<FocusIn>", lambda args: self.NewText.delete('0', 'end'))

        self.Label.pack()
        self.LabelNewText.pack()

        self.Cod.pack()
        #self.NrRuns.pack()
        self.RunB.pack()
        self.CloseB.pack()
        self.NewText.pack()
        self.AddText.pack()
        self.threads=[]

    def destroy(self):
        #quit()
        global Exit
        self.exit = True
        Exit = True
        #sys.exit()
        super().destroy()


    def get_cod(self):
        cod = tkinter.StringVar()
        try:
            cod = str(self.Cod.get())
        except:
            raise ValueError(" !!! Cod Invalid !!! ")

        if len(cod) != len("0dfwd9yumu4e"):
            raise ValueError(" !!! Cod Invalid !!! ")
        return cod

    def get_number_of_runs(self):
        nr = tkinter.StringVar()
        try:
            nr = int(self.NrRuns.get())
        except:
            raise ValueError(" !!! Valoarea introdusa la \' Numar sondaje \' trebuie sa fie numar !!! ")
        return nr


    def run(self):
        print(2)
        runtimes = 0
        try:
            cod = self.get_cod()
            # nr = self.get_number_of_runs()
        except ValueError as ve:
            tkinter.messagebox.showerror(" Graba strica treaba ", ve)
            return
        codes = generate_code.get_codes(cod, 300)

        for i in range(0, 50):
            cod = random.choice(codes)
            queue = Queue()
            global Exit
            t = threading.Thread(target= RUN.run, args = (cod, queue))
            t.setDaemon(True)
            self.threads.append(t)

        i = 0
        while i < len(self.threads) and self.exit == False:
            if threading.activeCount() >  multiprocessing.cpu_count() :
                time.sleep(0.1)
            else:
                self.threads[i].start()
                i += 1

        for t in self.threads:
            t.join()

GUI = GUI()

if __name__ == '__main__':
    GUI.mainloop()