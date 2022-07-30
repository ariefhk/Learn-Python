from __future__ import division
from math import remainder


def quizNumber(number):
    print(f'\n=== QUIZ Number {number} ===')


quizNumber(1)
print('Day 2: 30 Days of python programming')

quizNumber(2)
first_name = 'Arief Rachman'
last_name = 'Hakim'
full_name = f'{first_name} {last_name}'
country = 'Indonesia'
city = 'Ciamis'
age = 20
year = 2022
is_married = False
is_true = True
is_ligth_on = True
hobby, activity = 'Swimming', 'Gaming'

quizNumber(3)
num_one = 5
num_two = 4
print(type(num_one))

quizNumber(4)
print(len(first_name))
print(len(last_name))
print(
    f'compare len of firstname: {len(first_name)} and lastname: {len(first_name)}')
print(len(full_name))

quizNumber(5)
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

quizNumber(6)
radius = 30


def calculateAreaOfCircle(radius):
    area_of_circle = 3.14 * radius ** 2
    return area_of_circle


def calculateCircumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference


print(calculateAreaOfCircle(radius))
print(calculateCircumference(radius))
