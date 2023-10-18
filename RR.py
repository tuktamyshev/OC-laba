def work_with_data(data):
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    current_process = 0
    while sum(data) != 0:
        i = 0
        while current_process < len(data) and data[current_process] == 0:
            current_process += 1
        if current_process == len(data):
            current_process = 0
        while i < len(data):
            if data[i] != 0:
                if i == current_process:
                    data_for_table[i] += "И"
                else:
                    data_for_table[i] += "Г"
            i += 1
        data[current_process] -= 1
        current_process += 1
    return data_for_table


def calculate(data):
    pass