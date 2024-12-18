import json
import os

cache_file = "CUBIX/home_work/home_work_170_176_185/185/factorial/factorial_cache.json"

def load_cache():
    if os.path.exists(cache_file):
        with open(cache_file, "r") as file:
            return json.load(file)
    return {}

def save_cache(cache):
    with open(cache_file, "w") as file:
        json.dump(cache, file)

def factorial(n, cache):
    if str(n) in cache:
        print(f"Cache contains {n} --> loading from cache...")
        return cache[str(n)]
    
    print(f"Calculating factorial of {n}")
    result = 1
    for i in range(1, n + 1):
        result *= i

    cache[str(n)] = result
    save_cache(cache)
    return result

if __name__ == "__main__":
    cache = load_cache()

    while True:
        try:
            num = int(input("Enter a number to calculate its factorial (-1 to exit): "))
            if num == -1:
                break
            elif num < 0:
                print("Please enter a non-negative integer.")
            else:
                print(f"The factorial of {num} is: {factorial(num, cache)}")
        except ValueError:
            print("Invalid input, please enter an integer...")
