#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#name = input('please input your name:')
#print('I\'m \"OK\"')
#a='ABC'.encode('ascii')
#print(len(a))
#print('hello %s' % 'lsh')
# print('hello %s, your $%d is time to back' % ('lyf' , 20000))
# print('%s I want marry you %d days later' % ('hxy' , 10))
# classmate=['Tom','jerry','tiger']
# classmate.append('trump')
# classmate.pop(0)
# classmate[0]='tom2'
# print(classmate[0])
# age = 8
# if age > 18:
#     print('this guy is $d years old' % (age))
#     print('adult')
# else:
#     print('this guy is %d years old' %(age))
# L = ['Bart', 'Lisa', 'Adam']
# for a in L:
# #     print(a)
# n = 0
# while n<10:
#     n=n+1
#     if n % 2 == 0:
#         break
# #     print(n)
#
# import math
# def qiugen(a,b,c):
#     deta=b*b-4*a*c
#     xx = -b+ math.sqrt(deta)
#     x1 = xx /( 2*a)
#     yy = -b- math.sqrt(deta)
#     x2 = yy / (2*a)
#     return x1,x2
#
# result = qiugen(2,9,4)
# print(result)
# def power(x,n=2):
#     s = 1
#     while n > 0:
#         n = n-1
#         s = s * x
#     return s
# print(power(2))
# from collections import Iterable
# result = isinstance('abc', Iterable) # str是否可迭代
# if result:
#     print('true')
# L = ['A', 'B', 'C']
# for i, value in enumerate(L):
#     print(i, value)
# print(L[2])
# L = []
# for i in range(1,5):
#     L.append(i * i)
#  print(L)
# q = list(range(1,5))
# print(q)
# L = [x*y for x in range(1,5) for y in range(3,8)]
# print(L)
# print(len(L))
# g = (x*x for x in range(1,5))
# for i in g:
#     print(i)
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-5, 6, abs))
# list = [36, 5, -12, 9, -21]
# sorted(list,key=abs)
# print(list)
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())
# import _functools , datetime
# def timelog(text):
#     def time(func):
#         def wapper(*args, **kw):
#             print('%s %s():' % (text,datetime.datetime.now()))
#             return func(*args, **kw)
#         return wapper
#     return time
#
# @timelog('系统执行时间是：')
# def show():
#     print('success')
# show()
# import functools
# int2 = functools.partial(int,base=10)
# print(int2('1010101'))

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# ' a test module '
# __author__ = 'LSH'
# import sys
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# # if __name__=='__main__':
# test()
#################################################
# class student(object):
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
# test=student('mary',88)
# # test.adress='beijing'
# print(test._student__name)
#################################################
# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender1):
#         self.__gender=gender1
#
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
# ###########################################
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     def kill(self):
#         print('sucess')
#
# def kill2(Dog):
#     Dog.kill()
# kill2(Dog())
# class student(object):
#     __slots__ = ('name','age')
#
# class son(student):
#     pass
# s=son()
# s.score=88
# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s=Student()
# s.set_score(101)
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# from enum import Enum, unique
# @unique
# class Weekday(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1 = Weekday.Mon.value
# print(day1)
# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#         class Bart(Enum):
#             Male = 0
#             Female = 1
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')
# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()
# f=open('C:/users/16080/Desktop/1/1.docx','r',encoding='gbk')
# print(f.read())
# f.close()
# fpath = r'C:\Windows\system.ini'
#
# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world')
# print(f.getvalue())
# from io import BytesIO
# f = BytesIO()
# f.write('你好'.encode('utf-8'))
# print(f.getvalue())

import os
a=os.mkdir('C:/users/16080/Desktop/1/2')
b=os.mkdir('C:/users/16080/Desktop/1/3')








