#! /usr/bin/env/python
# —*— coding:utf-8 -*-


total = 8
y = int(input('取出计划总数y:'))
x = int(input('分层初始计划数x:'))
# 分层计划数倍率
m = int(input('分层计划数倍率m:'))
N = 0
a = 0
while True:
    N += 1
    a += m**(N - 1) * x
    if total <= y:
        print('计划数小于y全取')
        break
    elif a >=y:
        break
print('一共分了:%d' % N)
n = N - 1
f = 2*(y - x*n)
c = n*(n - 1)
q = f // c
print('引用参数q:%d' % q)
while n >= 1:
# 每层计划数
    PlannedNumber = x + (n - 1) * q
    n -= 1
    print(PlannedNumber)

