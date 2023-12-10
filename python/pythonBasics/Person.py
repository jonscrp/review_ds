class Person:
    x = 3

    def getX(self):
        return self.x
    
    def modifyX(self):
        self.x = 4


p1 = Person()
p2 = Person()


print("p1.x: ", p1.x)
print("p1.getX(): ", p1.getX())

print("p2.modifyX(): ")
p1.modifyX() 

print("p2.x: ", p2.x)
print("p2.getX(): ", p2.getX() )

print("p1.x: ", p1.x)
print("p1.getX(): ", p1.getX())
