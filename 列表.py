li=[1,2,3,4,5,3,6,3]
l2=[]
for x in li:
    if li.count(x) > 1:
        li.remove(x)
print li
