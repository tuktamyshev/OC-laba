import FCFS
import RR
import SJF
import PSJF_PSJF
import RR_SJF
from tkinter import *
from tkinter.ttk import Combobox, Scrollbar, Treeview
from time import sleep


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500+400+200")
        self.root.title("Симуляция обработки процессов")
        self.run()

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.processes_frame = Frame(self.root, bd=5, relief=SUNKEN)
        self.bottom_frame = Frame(self.root)

        self.modes = ["FCFS", "RR", "SJF", "PSJF_PSJF", "RR_SJF"]
        self.combobox = Combobox(self.bottom_frame, values=self.modes, state="readonly", font=10, width=8)
        self.combobox.current(0)
        self.combobox.bind("<<ComboboxSelected>>", self.mode_change)

        self.entry_box = Entry(self.bottom_frame, font=("Arial", 30), width=5)

        self.data = [("Процесс1", "И","И", "И") * 10]
        self.create_table()

        self.submit_botton = Button(self.bottom_frame, text="Добавить процесс", font=30, command=self.submit)
        self.reset_button = Button(self.bottom_frame, text="Сбросить процессы", font=30, command=self.reset)

        self.processes_frame.pack(fill=X)
        self.bottom_frame.pack(anchor=NW)
        Label(self.bottom_frame, text="Выбор режима", font=30).grid(row=0, column=0, padx=10, pady=10)
        self.combobox.grid(row=1, column=0, padx=10, pady=10)
        Label(self.bottom_frame, text="Процессорное время", font=30).grid(row=0, column=1, padx=50, pady=10)
        self.entry_box.grid(row=1, column=1, padx=50, pady=10)
        self.submit_botton.grid(row=2, column=1, padx=10, pady=10)
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)
        Label(self.bottom_frame, text="Среднее время ожидания: ").grid(row=0, column=2, padx=10, pady=10)
        Label(self.bottom_frame, text="Среднее время выполнения: ").grid(row=1, column=2, padx=10, pady=10)

    def create_table(self):
        heads = ["Процесс"]
        if self.data:
            for i in range(1, len(self.data[-1])):
                heads.append(i)
        self.table = Treeview(self.processes_frame, show="headings", columns=heads)
        for header in heads:
            self.table.heading(header, text=header, anchor=W)
            if header != "Процесс":
                self.table.column(f"#{header + 1}", stretch=NO, width=30)
            else:
                self.table.column(f"#1", stretch=NO, width=60)

        for row in self.data:
            self.table.insert("", "end", values=row)
        self.scrollbar_y = Scrollbar(self.processes_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)
        self.scrollbar_x = Scrollbar(self.processes_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)
        self.table.pack(anchor=SW)

    def refresh_table(self):
        self.table.destroy()
        self.scrollbar_x.destroy()
        self.scrollbar_y.destroy()
        self.create_table()

    def mode_change(self, event):
        mode = self.combobox.get()
        print(f"режим сменён на  {mode}")
        #смена режима

    def submit(self):
        pass

    def reset(self):
        pass


def main():
    gui = Interface()


if __name__ == '__main__':
    main()
