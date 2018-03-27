class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second

    def sum(self):
        result=self.first+self.second
        return result

    def mul(self):
        result=self.first*self.second
        return result

    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

a = FourCal()

a.setdata(1,3)
a.setdata(1,3)
a.setdata(5,3)
a.setdata(6,2)

print(a.sum())
print(a.mul())
print(a.sub())