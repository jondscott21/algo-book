def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr
# print(biggie_size([-1,3,5,-5]))

def print_low_return_high(arr):
    print(min(arr))
    return max(arr)
# print(print_low_return_high([-1,3,5,-5]))

def print_one_return_another(arr):
    print(arr[-2])
    for i in arr:
        if i % 2 != 0:
            return i
# print(print_one_return_another([2,4,5,9,8]))

arr1 = [1,2,3,4,5,6,7,8,9,10]
def double_vision(arr):
    return [i * 2 for i in arr]
# print(double_vision(arr1))
# print(arr1)

def count_postives(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    arr[-1] = count
    return arr
# print(count_postives([-1,1,1,1]))

def evens_and_odds(arr):
    even_count = 0
    odd_count = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_count += 1
            odd_count = 0
        if arr[i] % 2 != 0:
            odd_count += 1
            even_count = 0
        if even_count == 3:
            arr[i] = 'Even more so'
            even_count = 0
        elif odd_count == 3:
            arr[i] = "That's odd"
            odd_count = 0
    return arr
arr2 = [1,2,3,4,6,6,7,8,9,0]
# print(evens_and_odds(arr2))

def increment_the_seconds(arr):
    for i in range(len(arr)):
        if i % 2 != 0:
            arr[i] += 1
            print(arr[i])
    return arr
# print(increment_the_seconds(arr1))

def previous_lengths(arr):
    prev = None
    for i in range(len(arr)):
        temp = prev
        prev = arr[i]
        if temp is None:
            arr[i] = temp
        else:
            arr[i] = len(temp)
    return arr
arr3 = ['hi', 'word', 'this', 'something', 'else', 'running']
# print(previous_lengths(arr3))

def add_seven_to_most(arr):
    new_list = list(arr)
    for i in range(1, len(new_list)):
        new_list[i] += 7
    return new_list
# print(add_seven_to_most(arr1))

def reverse_array(arr):
    arr.reverse()
    return arr
# print(reverse_array(arr1))

def outlook_negative(arr):
    return [i * -1 if i > 0 else i for i in arr]
# print(outlook_negative([1,-3,5]))

def always_hungry(arr):
    count = 0
    for i in arr:
        if i == 'food':
            count += 1
            print('yummy')
    if count == 0:
        print("I'm hungry")
# always_hungry(arr1)
# always_hungry(['food', 'food'])

def swap_towards_the_center(arr):
    end = len(arr) - 1
    start = 0
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
# print(swap_towards_the_center(arr3))

def scale_the_array(arr, num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
# print(scale_the_array(arr1, 3))
