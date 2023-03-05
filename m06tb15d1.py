import multiprocessing
import time
import random
import datetime

def process():
    wait_time = random.random()
    time.sleep(wait_time)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"Current time is {current_time}")
    
if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

else:
    print("Oops.")
