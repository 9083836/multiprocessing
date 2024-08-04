import time
import multiprocessing
import random

def create_file(file_number):
    random_number = random.randint(1, 10000)
    time.sleep(1)
    file_name = f"file_{file_number}.txt"
    with open(file_name, "w") as file:
        file.write(f"In file number {random_number}")
    print(f"{file_name} has been created")
    return file_name


if __name__ == "__main__":
    start_time = time.time() 

    maltiprocesings = []  # Список для хранения потоков
    for i in range(1000):
        #Новый поток для выполнения функкции
        process = multiprocessing.Process(target=create_file, args=(i,))
        #Добавление потока в список 
        maltiprocesings.append(process)
        process.start()  # Запуск потока


    end_time = time.time()  # Конец замера времени
    print(f"Total time: {end_time - start_time} seconds")