
#h inherits the properties from multiple parent class to single child class is called as mutliple inheritance 


# pc1 -> pc2 .._> pc3 ----> child class

class a :
    property1 = 10
class b :
    property2 = 20
class c :
    property1 = 30
class d(b,a,c):
    pass
print(d.property1)

