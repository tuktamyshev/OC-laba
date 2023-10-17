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

        self.entered_data = []
        self.create_table()

        self.submit_botton = Button(self.bottom_frame, text="Добавить процесс", font=30, command=self.submit)
        self.reset_button = Button(self.bottom_frame, text="Сбросить процессы", font=30, command=self.reset)

        self.calculate_button = Button(self.bottom_frame, text="Вычислить", font=30, command=self.calculate)

        self.wait_time = Label(self.bottom_frame, text="1")
        self.execute_time = Label(self.bottom_frame, text="1")

        self.processes_frame.pack(fill=X)
        self.bottom_frame.pack(anchor=NW)
        Label(self.bottom_frame, text="Выбор режима", font=30).grid(row=0, column=0, padx=10, pady=10)
        self.combobox.grid(row=1, column=0, padx=10, pady=10)
        Label(self.bottom_frame, text="Процессорное время", font=30).grid(row=0, column=1, padx=50)
        self.entry_box.grid(row=1, column=1, padx=50, pady=10)
        self.submit_botton.grid(row=2, column=1, padx=10, pady=10)
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)
        Label(self.bottom_frame, text="Среднее время ожидания: ").grid(row=0, column=2)
        Label(self.bottom_frame, text="Среднее время выполнения: ").grid(row=1, column=2)
        self.calculate_button.grid(row=2, column=2, padx=10, pady=10)
        self.wait_time.grid(row=0, column=3)
        self.execute_time.grid(row=1, column=3)
    def create_table(self):
        current_mode = self.combobox.get()
        if current_mode == "FCFS":
            self.data_for_table = FCFS.work_with_data(self.entered_data)
        elif current_mode == "RR":
            self.data_for_table = RR.work_with_data(self.entered_data)
        elif current_mode == "PSJF_PSJF":
            self.data_for_table = PSJF_PSJF.work_with_data(self.entered_data)
        elif current_mode == "RR_SJF":
            self.data_for_table = RR_SJF.work_with_data(self.entered_data)
        elif current_mode == "SJF":
            self.data_for_table = SJF.work_with_data(self.entered_data)

        heads = ["Процесс"]
        if self.entered_data:
            for i in range(1, len(self.data_for_table) + 1):
                heads.append(i)
        self.table = Treeview(self.processes_frame, show="headings", columns=heads)
        for header in heads:
            self.table.heading(header, text=header, anchor=W)
            if header != "Процесс":
                self.table.column(f"#{header + 1}", stretch=NO, width=30)
            else:
                self.table.column(f"#1", stretch=NO, width=60)

        for row in self.data_for_table:
            print(row)
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
        # смена режима
        self.refresh_table()

    def submit(self):
        process_time = self.entry_box.get()
        self.entry_box.delete(0, END)
        if process_time.isdigit():
            self.entered_data.append(int(process_time))
            self.refresh_table()
            self.wait_time.config(text="")
            self.execute_time.config(text="")

    def reset(self):
        self.entered_data = []
        self.data_for_table = []
        self.refresh_table()
        pass

    def calculate(self):
        current_mode = self.combobox.get()
        if current_mode == "FCFS":
            calculated_data = FCFS.calculate(self.data_for_table)
        elif current_mode == "RR":
            calculated_data = RR.calculate(self.data_for_table)
        elif current_mode == "PSJF_PSJF":
            calculated_data = PSJF_PSJF.calculate(self.data_for_table)
        elif current_mode == "RR_SJF":
            calculated_data = RR_SJF.calculate(self.data_for_table)
        elif current_mode == "SJF":
            calculated_data = SJF.calculate(self.data_for_table)


def main():
    gui = Interface()


if __name__ == '__main__':
    main()
