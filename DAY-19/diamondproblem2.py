class College:
    c_name='GLS'
    C_code=130
    C_location='Ahmedabad'

    @classmethod
    def display(cls):
        return(cls.c_name,cls.C_code,cls.C_location)

class CS(College):
    CS_HOD='sahil'
    CS_code=102
    CS_faculty=5

    @classmethod
    def displayCS(cls):
        return(cls.CS_code,cls.CS_faculty,cls.CS_HOD) 

class IT(College):
    IT_HOD='Kalp'
    IT_code=112
    IT_faculty=7

    @classmethod     
    def displayIT(cls):
        return(cls.IT_code,cls.IT_faculty,cls.IT_HOD) 

class Student(CS,IT):
    def __init__(self,S_id,name,D_name,):
        self.S_ID=S_id
        self.NAME=name
        self.D_NAME=D_name
    
    def display(self):
        if self.D_NAME=='CS':
            a=super().displayCS()
            return(self.S_ID,self.NAME,self.D_NAME) + a
        else:
            a=super().displayIT()
            return(self.S_ID,self.NAME,self.D_NAME) + a
    
s1=Student('10','keya','CS')
print(s1.display())