def work_with_data(data):
    data_for_table = []
    count_wait_time = 0
    for i, process_time in enumerate(data, start=1):
        s = "Г" * count_wait_time + "И" * process_time
        data_for_table.append([f"Процесс {i}"] + list(s))
        count_wait_time = len(s)
    return data_for_table

def calculate(data):
    wait_time = 0
    sum_wait_time = 0
    sum_execute_time = 0
    for i in data:
        sum_execute_time += i + wait_time
        sum_wait_time += wait_time
        wait_time += i

    return ["{:.2f}".format(sum_wait_time/len(data)), "{:.2f}".format(sum_execute_time//len(data))]
