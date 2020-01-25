# PAGE 16

def setting_and_swapping():
    my_number = 42
    my_name = 'jon'
    my_number, my_name =  my_name, my_number
    print(my_number, my_name)
# setting_and_swapping()

def print_minus_to_plus():
    for i in range(-52, 1067):
        print(i)
# print_minus_to_plus()

def dont_worry_be_happy():
    print("good morning")
# for i in range(98):
#     dont_worry_be_happy()

def multiples_of_three_but_not_all():
    for i in range(-300, 0):
        if i != -3 and i != -6:
            print(i)
# multiples_of_three_but_not_all()

def print_with_while():
    count = 2000
    while count <= 5280:
        print(count)
        count += 1
# print_with_while()

def you_say_its_your_birthday(month, day):
    if day == 26 and month == 1:
        print("How did you know?")
    else:
        print("Just another day.")
# you_say_its_your_birthday(1, 26)

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
# print(leap_year(1900))
    
def print_and_count():
    count = 0
    for i in range(512, 4096):
        if i % 5 == 0:
            count += 1
            print(i)
    print('count', count)
# print_and_count()

def multiplies_of_six():
    count = 0
    while count <= 60000:
        if count % 6 == 0:
            print(count)
        count += 1
# multiplies_of_six()

def counting_the_dojo_way():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
# counting_the_dojo_way()

def what_do_you_know(incoming):
    print(incoming)
# what_do_you_know('word')

def whoa_that_sucker_is_huge():
    total = 0
    for i in range(-300000, 300000):
        if i % 2 != 0:
            total += i
    print(total)
# whoa_that_sucker_is_huge()

def countdown_by_fours():
    count = 2016
    while count > 0:
        print(count)
        count -= 4
# countdown_by_fours()

def flexible_countdown(low_num, high_num, mult):
    for i in reversed(range(low_num, high_num + 1)):
        if i % mult == 0:
            print(i)
# flexible_countdown(2, 9, 3)

def the_final_countdown(param1, param2, param3, param4):
    while param2 <= param3:
        if param2 % param1 == 0 and param2 != param4:
            print(param2)
        param2 +=1
# the_final_countdown(3, 5, 17, 9)

