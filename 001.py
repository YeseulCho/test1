#! /usr/bin/env python

import Bio
import math

"""
print("Hello Python")
print()

# 원의 면적 구하기
r = 3
PI = math.pi
area = PI * r * r
print(area)
print()

# 사칙연산
n1 = 3
n2 = 5

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 % n2)
print(n1 ** n2) # 제곱
print()

# 홀수 짝수 구하기 
num1 = 3
if num1 % 2 == 1 :
    print("even")
    print()

else :
    print("odd")
    print()

# 3의 배수, 7의 배수
num1 = 21

if num1 % 3 == 0 & num1 % 7 == 0 :
    print("3 and 7")
    print()

elif num1 % 3 == 0 :
    print("3")
    print()

elif num1 % 7 == 0 :
    print("7")
    print()

else :
    print("None")
    print()

# 1부터 10까지합
total_sum=0

for i in range(11) :
    total_sum += i

print(total_sum)
print()

# 구구단의 짝수단만 출력
odd_sum = 0

for i in range(2, 10, 2) :
    print("---{} dan---".format(i))

    for j in range(1, 10) :
        print("{} * {} = {}".format(i, j, j*i))

# 구구단의 짝수단만 출력- 강사님

for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        if i % 2 == 0 :
            print(f"{i} X {j} = {i*j}") # f string을 사용해보기 

# mySum
def mySum(n1 : int, n2 : int) -> None :
    print(f"{n1} + {n2} = {n1+n2}")

mySum(2,3)
mySum(5,7)
mySum(10, 15)

# 글자
word = input("word : ")

if word.isalpha() :
    print("string")

elif word.isnumeric() :
    print("num")

else :
    print("?")
"""

import sys

print(f"run -> smaple {sys.argv[1]}")

