__author__ = 'Junior'
class Hello:

    def __init__(self,x):
        self.b = x


    def sayHello(self):
        print 'hello',self.b
        #print 'hello {0}'.format(self.b)

class Hi(Hello):
    def __int__(self,x):
        Hello.__init__(self.b)
    def sayHi(self):
        print 'Hi',self.b
        #print "Hi {0}".format(self.b)

h=Hello("jikexueyuan")
h.sayHello()
h1 =Hi('ZHujunbo')
h1.sayHi()