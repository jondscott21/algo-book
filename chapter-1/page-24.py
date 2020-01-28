# PAGE 24
import random

def only_keep_the_last_few(arr , removal_num):
    return arr[-removal_num:]
# print(only_keep_the_last_few([2,4,6,8,10], 3))

def math_help(m, b):
    pass


def poor_kenny():
    chance = random.randint(1, 100)
    if chance <= 10:
        print('volcano')
        return chance
    elif chance > 10 and chance <= 25:
        print('tsunami')
        return chance
    elif chance > 25 and chance <= 45:
        print('earthquake')
        return chance
    elif chance > 45 and chance <= 70:
        print('blizzard')
        return chance
    else:
        print('meteor strike')
        return chance
# print(poor_kenny())

def what_really_happened():
    chance = random.randint(1, 100)
    if chance <= 10:
        print('volcano')
    chance = random.randint(1, 100)
    if chance > 10 and chance <= 25:
        print('tsunami')
    chance = random.randint(1, 100)
    if chance > 25 and chance <= 45:
        print('earthquake')
    chance = random.randint(1, 100)
    if chance > 45 and chance <= 70:
        print('blizzard')
        return chance
    if chance > 70:
        print('meteor strike')
# what_really_happened()

def soaring_iq(iq):
    for i in range(1, 99):
        iq += (i / 100)
    return iq
# print(soaring_iq(100))

def letter_grade(score):
    grade = ""
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Score: {score}, Grade: {grade}")
# letter_grade(90)
    