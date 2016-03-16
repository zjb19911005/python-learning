__author__ = 'Junior'
def odd(n):
    return n%2==1

l4=list(filter(odd,[1,2,3,4,5,6,9,10,15]))
l5=list(map(odd,[1,2,3,4,5,6,9,10,15]))
print l4
print l5