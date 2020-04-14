#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
# f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
# print(f)
# print(f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()

print(f1())#此处调用的是f(),调用直接进入到地19行，此时i已经等于3了，因此结果都是3*3=9
print(f2())
print(f3())

# # fix:
# def count():
#     fs = []
#     def f(n):
#         def j():
#             return n * n
#         return j
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
#
# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())