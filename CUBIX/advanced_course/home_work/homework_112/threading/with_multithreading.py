import threading
import time

def task(name, duration):
    print(f"Task {name} started")
    time.sleep(duration)
    print(f"Task {name} completed after {duration} seconds")

start_time = time.time()

t1 = threading.Thread(target=task, args=("A", 2**2))
t2 = threading.Thread(target=task, args=("B", 3**3))
t3 = threading.Thread(target=task, args=("C", 1**1))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = time.time()

print(f"Execution time: {end_time - start_time:.2f} seconds")
