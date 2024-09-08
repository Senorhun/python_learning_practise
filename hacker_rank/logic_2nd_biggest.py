# def looking(arr):
#     arr_list = list(arr)
#     biggest = arr_list[0]
#     for num in arr_list:
#         if num > biggest:
#             biggest = num
#     result_list = []
#     for num in arr_list:
#         if num != biggest:
#             result_list.append(num)
#     final_list = sorted(result_list)
#     return final_list[len(final_list)-1]



# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(looking(arr))

def looking(arr):
    unique_numbers = set(arr) 
    unique_numbers.remove(max(unique_numbers)) 
    return max(unique_numbers)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(looking(arr))
