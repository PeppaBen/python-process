class Triangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def getArea(self):
        area=self.width*self.height/2
        return area

    
class square:
    def __init__(self,size):
        self.size=size
        
    
    def getArea(self):
        size=self.size*self.size
        return size

a=Triangle(5,5)
print(a.getArea())
b=square(5)
print(b.getArea())
