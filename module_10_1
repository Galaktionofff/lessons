import time
import threading
def write_words(word_count=10, file_name='example.txt'):
    with open(file_name, 'w') as w:
        for num in range(1, word_count + 1):
            time.sleep(0.1)
            w.write(f'Какое-то слово № {num} \n')
    print(threading.currentThread())
    print(f"Завершилась запись в файл {file_name}")

args_list1 = [
    (10, 'example1.txt'),
    (30, 'example2.txt'),
    (200, 'example3.txt'),
    (100, 'example4.txt'),
]
start1 = time.time()
for args1 in args_list1:
    write_words(*args1)
end1 = round(time.time() - start1, 2)
print(end1)

args_list = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt'),
]
start = time.time()
threads = []
for args in args_list:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = round(time.time() - start, 2)
print(end)


