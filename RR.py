from collections import deque


def work_with_data(data):
    data = [i for i in data.values()]
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    current_process = 0
    while sum(data) != 0:
        i = 0
        if current_process == len(data):
            current_process = 0
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


'''def work_with_data(data):
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    data = deque([[i, j] for i,j in data.items()])
    while sum(n for _, n in data) != 0:
        for i in range(len(data)):
            if data[i][1] == 0:
                continue
            if data[i][1] != 0 and i == 0:
                data_for_table[data[i][0] - 1] += "И"
                data[0][1] -= 1
            elif data[i][1] != 0:
                data_for_table[data[i][0] - 1] += "Г"
        current_process = data.popleft()
        data.append(current_process)
    return data_for_table'''

def calculate(data):
    print(data)
    pass