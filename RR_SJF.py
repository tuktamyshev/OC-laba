from collections import deque


def work_with_data(data):
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    sorted_data = deque([[i, j] for i, j in sorted_data.items()])
    s = sum(n for _, n in sorted_data)
    while s != 0:
        while sorted_data[0][1] == 0:
            current_process = sorted_data.popleft()
            sorted_data.append(current_process)
        for i in range(len(sorted_data)):
            if sorted_data[i][1] != 0 and i == 0:
                data_for_table[sorted_data[i][0] - 1] += "И"
                sorted_data[0][1] -= 1
                s -= 1
            elif sorted_data[i][1] != 0:
                data_for_table[sorted_data[i][0] - 1] += "Г"
        current_process = sorted_data.popleft()
        if current_process[1] != 0:
            sorted_data.append(current_process)
    return data_for_table
