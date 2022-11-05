class test:
    def __init__(self):
        self.a 
    
    def fun1(self):
        self.a=10
        return self.a
        
    def fun2(self):
        self.fun1()
        print(self.fun1())
        
    def run(self):

        self.fun2()