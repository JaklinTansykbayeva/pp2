#date ex1

from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date after subtracting 5 days:", new_date)

#date ex2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#date ex3
from datetime import datetime

current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current Datetime with Microseconds:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)

#date ex4
from datetime import datetime

# Example dates
date1 = datetime(2023, 6, 1, 12, 0, 0)
date2 = datetime(2023, 6, 2, 12, 0, 0)

difference = date2 - date1
difference_in_seconds = difference.total_seconds()

print("Difference between dates in seconds:", difference_in_seconds)

#generators ex1
def generate_squares(N):
    for i in range(N):
        yield i * i
        

#generators ex2
def generate_even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i
            
# Пример 
n = int(input("Введите число n: "))
even_numbers_generator = generate_even_numbers(n)
even_numbers = ', '.join(str(num) for num in even_numbers_generator)
print(even_numbers)

#generators ex3
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


#generators ex4
def squares(a, b):
    for i in range(a, b+1):
        yield i * i


#generators ex5
def countdown(n):
    for i in range(n, -1, -1):
        yield i


#math ex1
import math

def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    return radian

degree = 15
print("Input degree:", degree)
print("Output radian:", degree_to_radian(degree))

#math ex2
def area_of_trapezoid(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = 5
base1 = 5
base2 = 6
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area_of_trapezoid(height, base1, base2))

#math ex3
import math

def area_of_polygon(num_sides, side_length):                      #polygon-многоугольник
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides)) 
                                             #num_sides — количество сторон
    return area                               #side_length — длина одной из сторон 


num_sides = 4
side_length = 25
print("Input number of sides:", num_sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", area_of_polygon(num_sides, side_length))

#math ex4
def area_of_parallelogram(base, height):
    area = base * height
    return area


base = 5
height = 6
print("Length of base:", base)
print("Height of parallelogram:", height)
print("Expected Output:", area_of_parallelogram(base, height))
