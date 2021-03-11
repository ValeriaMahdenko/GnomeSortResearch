import random
import time
import csv


def GnomeSort(a):
    i, j, size = 1, 2, len(a)
    while i < size:
        if a[i - 1] <= a[i]:
            i, j = j, j + 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return a


def random_arr(a, count):
    for i in range(count):
        a.append(random.randint(0,1000))
    return a


def write_csv(all):
    FILENAME = "Python_data.csv"
    with open(FILENAME, "w", newline="") as file:
        columns = ["Count", "Time"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(all)


if __name__ == '__main__':

    arr = []
    i = 500
    all = []
    while i <= 10000:
        arr = random_arr(arr, i)
        start_time = time.time()
        arr_sort = GnomeSort(arr)
        result_time = time.time()-start_time
        all.append(result_time)
        i += 500

    with open("/Users/sophiyca/PycharmProjects/gnom_algorithm/python_gnome.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow([i for i in all])