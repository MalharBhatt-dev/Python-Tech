class Sample:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
    
    def __add__(self,other):
        return self.value1 + other.value2
    
    ab1 = Sample(12,56)
    ab2 = Sample(90,80)