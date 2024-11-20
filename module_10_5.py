import multiprocessing
import time

def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as r:
        line = r.readline()
        all_data.append(line)
        while line:
            line = r.readline()
            all_data.append(line)


if __name__ == '__main__':
    file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    start = time.time()
    for file in file_list:
        read_info(file)
    end = round(time.time() - start, 2)
    print(end)

    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)
        end = round(time.time() - start, 2)
        print(end)
