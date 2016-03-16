#coding=utf-8
__author__ = 'Junior'
def digui(n):
    if n==1:
        return n
    else:
        return n*digui(n-1)

print(digui(5))