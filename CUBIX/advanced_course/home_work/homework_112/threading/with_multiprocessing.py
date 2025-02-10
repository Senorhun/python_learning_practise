import multiprocessing
import time

def task(name, duration):
    print(f"Task {name} started")
    time.sleep(duration)
    print(f"Task {name} completed after {duration} seconds")

if __name__ == "__main__":
    start_time = time.time()

    p1 = multiprocessing.Process(target=task, args=("A", 2))
    p2 = multiprocessing.Process(target=task, args=("B", 3))
    p3 = multiprocessing.Process(target=task, args=("C", 1))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
