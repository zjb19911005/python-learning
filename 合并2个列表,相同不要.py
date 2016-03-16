__author__ = 'Junior'
L1=[1,4,5,7]
L2=[2,5,7,8]
L1.extend(L2)
for x in L1:
    if L1.count(x)>1:
        L1.remove(x)
print L1