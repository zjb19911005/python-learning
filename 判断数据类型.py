__author__ = 'Junior'

L1=['zhu','jun','bo',2.0007,1,2,3]
L2=[]
L3=[]
L4=[]
for x in L1:
    if isinstance(x,str):
        L2.append(x)
    elif isinstance(x,list):
        L3.extend(x)
    elif isinstance(x,float):
        L4.append(x)
print L3,L4,L2