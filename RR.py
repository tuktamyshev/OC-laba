from collections import deque


# def work_with_data(data):
#     data = [i for i in data.values()]
#     data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
#     current_process = 0
#     while sum(data) != 0:
#         i = 0
#         while current_process < len(data) and data[current_process] == 0:
#             current_process = (current_process + 1) % len(data)
#         while i < len(data):
#             if data[i] != 0:
#                 if i == current_process:
#                     data_for_table[i] += "И"
#                 else:
#                     data_for_table[i] += "Г"
#             i += 1
#         data[current_process] -= 1
#         current_process = (current_process + 1) % len(data)
#     return data_for_table


def work_with_data(data):
    data_for_table = [[f"Процесс {i}"] for i in range(1, len(data) + 1)]
    data = deque([[i, j] for i,j in data.items()])
    s = sum(n for _, n in data)
    while s != 0:
        while data[0][1] == 0:
            current_process = data.popleft()
            data.append(current_process)
        for i in range(len(data)):
            if data[i][1] != 0 and i == 0:
                data_for_table[data[i][0] - 1] += "И"
                data[0][1] -= 1
                s -= 1
            elif data[i][1] != 0:
                data_for_table[data[i][0] - 1] += "Г"
        current_process = data.popleft()
        if current_process[1] != 0:
            data.append(current_process)
    return data_for_table


def calculate(data):
    t, T, M, R, P = 0, 0, 0, 0, 0
    for i in data:
        l = len(i) - 1
        T += l
        t = i.count("И")
        M += i.count("Г")
        try:
            R += t/l
            P += l/t
        except ZeroDivisionError:
            pass

    T, M, R, P = map(lambda x: round(x/(len(data)), 2), [T, M, R, P])
    return [T, M, R, P]