def print_1_255():
    for i in range(1, 256):
        print(i)
# print_1_255()

def print_odds_1_255():
    for i in range(1, 256):
        if i % 2 != 0:
            print(i)
# print_odds_1_255()

def print_ints_and_sum_0_255():
    total = 0
    for i in range(256):
        total += i
        print("Num: ", i, ", Total: ", total)
# print_ints_and_sum_0_255()

def iterate_and_print_array(arr):
    for i in arr:
        print(i)
# iterate_and_print_array([1,2,3,4,5])

def find_and_print_max(arr):
    print(max(arr))
# find_and_print_max([1,5,8,65,9,3])

def get_and_print_average(arr):
    total = 0
    for i in arr:
        total += i
    print(total / len(arr))
# get_and_print_average([1,2,3,4,5,6,7,8,9])

def array_with_odds():
    new_list = list()
    for i in range(1, 256):
        if i % 2 != 0:
            new_list.append(i)
    return new_list
# print(array_with_odds())

def square_the_values(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]
    return arr
# print(square_the_values([1,2,3,4,5,6,7,8,9]))

def greater_than_y(arr, y):
    for i in arr:
        if i > y:
            print(i)
# greater_than_y([1,2,3,4,5,6,7,8,9], 4)

def zero_out_negative_numbers(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr
# print(zero_out_negative_numbers([1,2,3,-1,-4,7,-8]))

def min_max_average(param_list):
    list_min = param_list[0]
    list_max = param_list[0]
    list_avg = param_list[0]
    for i in range(1, len(param_list)):
        if list_min > param_list[i]:
            list_min = param_list[i]
        if list_max < param_list[i]:
            list_max = param_list[i]
        list_avg += param_list[i]
    print('Min: ', list_min)
    print('Max: ', list_max)
    print('Avg: ', list_avg / len(param_list))
# min_max_average([1,2,3,4,5,6,7,8,9])

from statistics import mean
def min_max_average_refined(param_list):
    print('Min: ', min(param_list))
    print('Max: ', max(param_list))
    print('Avg: ', mean(param_list))
# min_max_average_refined([1,2,3,4,5,6,7,8,9])
l1 = [1,2,3,4,5,6,7,8,9]
def shift_array_values(arr):
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = 0
    return arr
# print(shift_array_values(l1))


def swap_string_for_array_negative_values(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 'Dojo'
    return arr
# print(swap_string_for_array_negative_values([1,2,3,-1,-4,7,-8]))