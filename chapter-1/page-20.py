# PAGE 20

def countdown(num):
    arr = list()
    while num >= 0:
        arr.append(num)
        num -= 1
    return arr
# print(countdown(10))

def print_and_return(arr):
    print(arr[0])
    return arr[1]
# print_and_return([0, 1])

def first_plus_length(arr):
    if type(arr[0]) is not int:
        return 'You can only add numbers'
    return arr[0] + len(arr)
# print(first_plus_length([1, 1]))

def values_greater_than_second():
    arr = [1,2,5,7,9,13]
    total = 0
    for el in arr:
        if el > arr[1]:
            total += 1
            print(el)
    return total
# values_greater_than_second([1,2,5,7,9,13])

def values_greater_than_second_generalized(arr):
    total = 0
    if len(arr) < 2:
        return 0
    for el in arr:
        if el > arr[1]:
            total += 1
            print(el)
    return total
# values_greater_than_second_generalized([1,2,5,7,9,13])

def this_length_that_value(num1, num2):
    return [num2 for i in range(num1)]
# print(this_length_that_value(3,6))

def fit_the_first_value(arr):
    if len(arr) < 1:
        print('The array needs values')
    elif arr[0] > len(arr):
        print('Too big!')
    elif arr[0] < len(arr):
        print('Too small!')
    elif arr[0] == len(arr):
        print('Just right!')
# fit_the_first_value([0])

def farenheit_to_celcius(temp):
    divider = 9 / 5
    return (divider * temp) + 32
# print(farenheit_to_celcius(1))

def celcius_to_farenheit(temp):
    divider = 5 / 9
    return (temp - 32) * divider
# print(celcius_to_farenheit(212))