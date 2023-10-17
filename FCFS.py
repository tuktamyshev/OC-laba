def work_with_data(data):
    data_for_table = []
    count_wait_time = 0
    for i, process_time in enumerate(data):
        s = "Г" * count_wait_time + "И" * process_time
        data_for_table.append(("Процесс" + str(i + 1), list(s)))
    return []

def calculate(data):
    pass