
def printLocalx():
    x=12
    print 'f1 local x = ',
    print x
def printLocaly():
    y=13
    print 'f2 local y = ',
    print y
def readGlobal():
    print 'f3 read global x = ',
    print x
    print 'f3 read global y = ',
    print y
def modifyGlobal():
    global x
    print 'f4 write x = -1'
    x=-1
def main():
    printLocalx()
    printLocaly()
    readGlobal()
    modifyGlobal()
x=200
y=100
main()
print 'after modified global x= ',
print x
print'End'
