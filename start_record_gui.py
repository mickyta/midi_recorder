import tkinter as tk
from midi_record import arec_start_record, arec_stop_record

E=tk.E
W=tk.W
N=tk.N
S=tk.S

class Window(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=tk.YES)

        self.master.title("Midi record application")
        self.master.geometry("450x300")
#        self.grid(sticky=N+S+E+W)
        self.__add_component()


    def __add_component(self):
        self.label = tk.Label(self,
                           justify='center',
                           text="Please press START/STOP")
        self.label.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

        self.button1 = tk.Button(self,
                           text="Start",
                           fg="green", height= 5,
                           command=self.start_record)

#        self.button1.grid(row = 1, column = 1)
        self.button1.pack(side=tk.LEFT,fill=tk.BOTH,
                          pady=50,
                          expand=tk.YES)

        self.button2 = tk.Button(self,
                           text="Stop", fg="red", height = 5,
                           command=self.stop_record)

#        self.button2.grid(row = 1, column = 3)
        self.button2.pack(side=tk.RIGHT,fill=tk.BOTH,
                          pady=50,
                          expand=tk.YES)


    def stop_record(self):
        self.label.config(text = "Record Stopped!")
        arec_stop_record()

    def start_record(self):
        self.label.config(text = "Record Started!")
        arec_start_record()


# initialize tkinter
root = tk.Tk()
app = Window(root)

# show window
app.mainloop()

