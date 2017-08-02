# coding:utf-8

def fun(a):
    return a*a

def f1(x):
    def f2(a):
        return x(a)+1
    return f2
@f1
def f3(b):
    return b**b
