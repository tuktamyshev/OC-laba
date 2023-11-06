def work_with_data(data):
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    count_wait_time = 0
    for i, process_time in data.items():
        s = "Г" * count_wait_time + "И" * process_time
        data_for_table[i - 1] += list(s)
        count_wait_time = len(s)
    return data_for_table


def calculate(data):
    wait_time = 0
    sum_wait_time = 0
    sum_execute_time = 0
    for i in data.values():
        sum_execute_time += i + wait_time
        sum_wait_time += wait_time
        wait_time += i

    return [round(sum_wait_time/len(data), 2), round(sum_execute_time/len(data), 2)]