def work_with_data(data):
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    count_wait_time = 0
    for i, process_time in sorted_data.items():
        s = "Г" * count_wait_time + "И" * process_time
        data_for_table[i - 1] += list(s)
        count_wait_time = len(s)
    return data_for_table