
#h CREATE A CLASS WHICH CONSISIT OF NAME , PERCENTAGE AND SCHOOL NAME AS OBJECT MEMBERS  AND THEN CREATE ANOTHER CLASS RESUME 2 WHICH INHERIT THE PROPEERTIES FROM RESUME1 AND ALONG WITH THAT HAVE 12TH PERCENTAGE AND COLLEGE NAME AS OBJECT MEMBERS AND THEN CREATE ANOTHER CLASS RESUME 3 WHICH INHERITS FROM RESUME 2 CLASS AND CONSISTS OF ADDITIONAL DEGREE COLLEGE AND DEGREE PERCENTAGE AS OBJECT MEMBERS.

class resume1:
    def __init__(self , name , sper , sname):
        self.NAME = name
        self.SPER = sper
        self.SNAME = sname
    def display(self):
       return (self.NAME,self.SPER,self.SNAME)

class resume2(resume1):
    def __init__(self , name , sper , sname , per12 , clg_name ):
        super().__init__(name , sper , sname)
        self.PER12 = per12
        self.CLG_NAME = clg_name
    def display(self):
        return super().display() + (self.PER12,self.CLG_NAME)

class resume3(resume2):
    def __init__(self , name , sper , sname , per12 , clg_name , deg_clg , deg_per):
        super().__init__(name , sper , sname , per12 , clg_name)
        self.DEG_CLG = deg_clg
        self.DEG_PER = deg_per
    def display(self):
        return super().display() + (self.DEG_CLG,self.DEG_PER)
        
s1 = resume3('Smit' , 70 , 'abc' , 65 , 'Inuds' , 'SPIT' , 75)
print(s1.display())


#H mult
