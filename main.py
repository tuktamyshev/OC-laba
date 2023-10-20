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
        self.root.geometry("800x600+400+100")
        self.root.title("Симуляция обработки процессов")
        self.run()

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.processes_frame = Frame(self.root, bd=5, relief=SUNKEN)
        self.bottom_frame = Frame(self.root)

        self.modes = ["FCFS", "RR", "SJF", "PSJF_PSJF", "RR_SJF"]
        self.combobox = Combobox(self.bottom_frame, values=self.modes, state="readonly", font=10, width=10)
        self.combobox.current(0)
        self.combobox.bind("<<ComboboxSelected>>", self.mode_change)

        self.entry_box = Entry(self.bottom_frame, font=("Arial", 30), width=5)

        self.entered_data = {}
        self.create_table()

        self.submit_botton = Button(self.bottom_frame, text="Добавить процесс", font=30, command=self.submit)
        self.reset_button = Button(self.bottom_frame, text="Сбросить процессы", font=30, command=self.reset)

        self.calculate_button = Button(self.bottom_frame, text="Вычислить", font=30, command=self.calculate)

        self.wait_time = Label(self.bottom_frame, text="") #средне время ожидания
        self.execute_time = Label(self.bottom_frame, text="") #среднее время выполнения

        self.total_execution_time_T = Label(self.bottom_frame, text="") #среднее общее время пребывания T
        self.lost_time_M = Label(self.bottom_frame, text="") #среднее потерянное время M
        self.reactivity_ratio_R = Label(self.bottom_frame, text="")#среднее отношение реактивности R
        self.penalty_ratio_P = Label(self.bottom_frame, text="") #среднее штрафное отношение P

        self.processes_frame.pack(fill=X)
        self.bottom_frame.pack(anchor=NW)
        Label(self.bottom_frame, text="Выбор режима", font=30).grid(row=0, column=0, padx=10, pady=10)
        self.combobox.grid(row=1, column=0, padx=10, pady=10)
        Label(self.bottom_frame, text="Процессорное время", font=30).grid(row=0, column=1, padx=50)
        self.entry_box.grid(row=1, column=1, padx=50, pady=10)
        self.submit_botton.grid(row=2, column=1, padx=10, pady=10)
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)
        self.widgets_for_FCFS()

    def create_table(self):
        current_mode = self.combobox.get()
        data_to_conversion = {i: v for i, v in self.entered_data.items()}
        if current_mode == "FCFS":
            self.data_for_table = FCFS.work_with_data(data_to_conversion)
        elif current_mode == "RR":
            self.data_for_table = RR.work_with_data(data_to_conversion)
        elif current_mode == "PSJF_PSJF":
            self.data_for_table = PSJF_PSJF.work_with_data(data_to_conversion)
        elif current_mode == "RR_SJF":
            self.data_for_table = RR_SJF.work_with_data(data_to_conversion)
        elif current_mode == "SJF":
            self.data_for_table = SJF.work_with_data(data_to_conversion)
        heads = ["Процесс"]
        if self.entered_data:
            for i in range(1, sum(self.entered_data.values()) + 1):
                heads.append(i)

        self.table = Treeview(self.processes_frame, show="headings", columns=heads)
        for header in heads:
            self.table.heading(header, text=header, anchor=W)
            if header != "Процесс":
                self.table.column(f"#{header + 1}", stretch=NO, width=30)
            else:
                self.table.column(f"#1", stretch=NO, width=70)

        for row in self.data_for_table:
            self.table.insert("", "end", values=row)
        self.scrollbar_y = Scrollbar(self.processes_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        self.scrollbar_x = Scrollbar(self.processes_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        self.table.pack(anchor=SW)

    def refresh_table(self):
        self.clear_results()
        self.table.destroy()
        self.scrollbar_x.destroy()
        self.scrollbar_y.destroy()
        self.create_table()

    def mode_change(self, event):
        try:
            if self.combobox.get() == "FCFS":
                self.T_label.grid_forget()
                self.M_label.grid_forget()
                self.R_label.grid_forget()
                self.P_label.grid_forget()
                self.calculate_button.grid_forget()
                self.total_execution_time_T.grid_forget()
                self.lost_time_M.grid_forget()
                self.reactivity_ratio_R.grid_forget()
                self.penalty_ratio_P.grid_forget()
                self.widgets_for_FCFS()
            else:
                self.wait_time_label.grid_forget()
                self.execute_time_label.grid_forget()
                self.calculate_button.grid_forget()
                self.wait_time.grid_forget()
                self.execute_time.grid_forget()
                self.widgets_for_others()
            self.refresh_table()
        except AttributeError:
            return

    def submit(self):
        process_time = self.entry_box.get()
        self.entry_box.delete(0, END)
        if process_time.isdigit():
            self.clear_results()
            self.entered_data[len(self.entered_data) + 1] = int(process_time)
            self.refresh_table()

    def clear_results(self):
        self.wait_time.config(text="")
        self.execute_time.config(text="")
        self.total_execution_time_T.config(text="")
        self.lost_time_M.config(text="")
        self.reactivity_ratio_R.config(text="")
        self.penalty_ratio_P.config(text="")

    def widgets_for_FCFS(self):
        self.wait_time_label = Label(self.bottom_frame, text="Среднее время ожидания: ")
        self.execute_time_label = Label(self.bottom_frame, text="Среднее время выполнения: ")
        self.wait_time_label.grid(row=0, column=2)
        self.execute_time_label.grid(row=1, column=2)
        self.calculate_button.grid(row=2, column=2, padx=10, pady=10)
        self.wait_time.grid(row=0, column=3)
        self.execute_time.grid(row=1, column=3)


    def widgets_for_others(self):
        self.T_label = Label(self.bottom_frame, text="Среднее общее время пребывания(T): ")
        self.M_label = Label(self.bottom_frame, text="Среднее потерянное время(M): ")
        self.R_label = Label(self.bottom_frame, text="Среднее отношение реактивности(R): ")
        self.P_label = Label(self.bottom_frame, text="Среднее штрафное отношение(P): ")
        self.T_label.grid(row=0, column=2)
        self.M_label.grid(row=1, column=2)
        self.R_label.grid(row=2, column=2)
        self.P_label.grid(row=3, column=2)
        self.calculate_button.grid(row=4, column=2, padx=10, pady=10)
        self.total_execution_time_T.grid(row=0, column=3)
        self.lost_time_M.grid(row=1, column=3)
        self.reactivity_ratio_R.grid(row=2, column=3)
        self.penalty_ratio_P.grid(row=3, column=3)


    def reset(self):
        self.entered_data = {}
        self.data_for_table = []
        self.refresh_table()
        pass

    def calculate(self):
        current_mode = self.combobox.get()
        if not self.entered_data:
            return
        if current_mode == "FCFS":
            calculated_data = FCFS.calculate(self.entered_data)
            self.wait_time.config(text=f"{calculated_data[0]}")
            self.execute_time.config(text=f"{calculated_data[1]}")
            return
        elif current_mode == "RR":
            calculated_data = RR.calculate(self.data_for_table)
        elif current_mode == "PSJF_PSJF":
            calculated_data = PSJF_PSJF.calculate(self.data_for_table)
        elif current_mode == "RR_SJF":
            calculated_data = RR_SJF.calculate(self.data_for_table)
        elif current_mode == "SJF":
            calculated_data = SJF.calculate(self.data_for_table)
        self.total_execution_time_T.config(text=f"{calculated_data[0]}")
        self.lost_time_M.config(text=f"{calculated_data[1]}")
        self.reactivity_ratio_R.config(text=f"{calculated_data[2]}")
        self.penalty_ratio_P.config(text=f"{calculated_data[3]}")




def main():
    gui = Interface()


if __name__ == '__main__':
    main()
