class Service:
    secret="영구는 배꼽이 두 개다"
    def setname(self,name):
        self.name = name

    def sum(self,a,b):
        result=a+b
        print("%s + %s = %s입니다."%(a,b,result))

pay = Service()

pay.sum(1,1)