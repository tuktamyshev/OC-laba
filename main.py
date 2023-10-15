import FCFS
import RR
import SJF
import PSJF_PSJF
import RR_SJF
from tkinter import *
from tkinter.ttk import Combobox, Scrollbar, Treeview
from time import sleep


class Interface(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500+400+200")
        self.title("Симуляция обработки процессов")

        self.modes = ["FCFS", "RR", "SJF", "PSJF_PSJF", "RR_SJF"]
        self.combobox = Combobox(self, values=self.modes, state="readonly")

        self.processes_frame = Frame(self, bg="#cccccc", bd=5, relief=SUNKEN, width=400, height=250)

        self.data = [("1","и", "г" ), ("2","и", "г")]
        self.table = Treeview(self.processes_frame, show="headings")

        self.run()

    def run(self):
        self.draw_widgets()
        self.mainloop()

        sleep(1)
        self.table.insert("", "end", values=('1', 'и', 'г'))
        self.table.update()
    def draw_widgets(self):
        self.combobox.current(0)
        self.combobox.pack(side=RIGHT)
        self.combobox.bind("<<ComboboxSelected>>", self.mode_change)

        self.processes_frame.pack(anchor="ne")
        self.test()

    def mode_change(self, event):
        mode = self.combobox.get()
        print(f"режим сменён на  {mode}")
        #смена режима

    def test(self):
        heads = ["Процесс"]
        for i in range(1, len(self.data[-1]) + 1):
            heads.append(i)
        self.table["columns"] = heads
        for header in heads:
            self.table.heading(header, text=header, anchor=W)
        for i, row in enumerate(self.data):
            self.table.insert("", "end", values=row)
        scrollbary = Scrollbar(self.processes_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbary.set)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx = Scrollbar(self.processes_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=scrollbarx.set)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.table.pack(expand=YES, fill=BOTH)


def main():
    gui = Interface()


if __name__ == '__main__':
    main()
