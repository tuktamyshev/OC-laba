import FCFS
import RR
import SJF
import PSJF_PSJF
import RR_SJF
from tkinter import *
from tkinter.ttk import Combobox, Scrollbar


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500+400+200")
        self.root.title("Симуляция обработки процессов")

        self.modes = ["FCFS", "RR", "SJF", "PSJF_PSJF", "RR_SJF"]
        self.combobox = Combobox(self.root, values=self.modes, state="readonly")

        self.processes_canvas = Canvas(self.root, bg="#cccccc", bd=5, relief=SUNKEN, width=400, height=250)
        self.processes_frame = Frame(self.processes_canvas)

        self.run()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.combobox.current(0)
        self.combobox.pack(side=RIGHT)
        self.combobox.bind("<<ComboboxSelected>>", self.combobox_change)

        self.processes_canvas.place(x=0, y=0)
        self.processes_frame.place(x=10, y=10)
        Label(self.processes_frame, text="111"*1000).pack()
        scrollbar = Scrollbar(orient="horizontal", command=self.processes_canvas.xview)
        scrollbar.pack(fill="y", side=BOTTOM)

    def combobox_change(self, event):
        mode = self.combobox.get()
        print(f"режим сменён на  {mode}")
        #смена режима

def main():
    gui = Interface()


if __name__ == '__main__':
    main()
