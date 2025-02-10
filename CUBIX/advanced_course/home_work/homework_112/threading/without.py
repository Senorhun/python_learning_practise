import time

def task(name, duration):
    print(f"Task {name} started")
    time.sleep(duration)
    print(f"Task {name} completed after {duration} seconds")

start_time = time.time()
task("A", 2**2)
task("B", 3**3)
task("C", 1**1)
end_time = time.time()

print(f"Execution time: {end_time - start_time:.2f} seconds")