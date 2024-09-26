from datetime import datetime

def all_different(input_list):
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] == input_list[j]:
                return False
    return True

print(all_different([1,2,3,4,5]))
print(all_different([1,2,3,4,1]))


def all_different_sort(input_list):
    sorted_list= sorted(input_list)
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return False
    return True

before = datetime.now()
print(all_different_sort([i for i in range(10000)]))
print(datetime.now() - before)

def all_different_set(input_list):
    set_list= set(input_list)
    if len(input_list) == len(set_list):
        return True
    return False

before = datetime.now()
print(all_different_set([i for i in range(10000)]))
print(datetime.now() - before)

def all_different_set_optimized(input_list):
    return len(input_list) == len(set(input_list))

before = datetime.now()
print(all_different_set_optimized([i for i in range(10000)]))
print(datetime.now() - before)


