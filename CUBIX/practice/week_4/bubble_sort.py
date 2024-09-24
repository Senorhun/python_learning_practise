def bubble_sort(numbers):
    is_change = True
    while is_change:
        is_change = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                is_change = True

numbers = [4,6,2,5,8,7,1,7,3,9]
bubble_sort(numbers)
print(numbers)
