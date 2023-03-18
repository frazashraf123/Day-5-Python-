#Q.2.
class student:
    def _init_(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_details(self,sid,sm,sa):
        self.__student_id=sid
        self.__marks=sm
        self.__age=sa
    def validate_marks(self):
        if 100>=self.__marks>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
        else:
            return True
    def choose_course(self):
        if self.check_qualification():
            self.fees=None
            self.course=int(input("\nyou are eligible for admission,\ninput 1001 to choose course 1001 (default fees 25575.0)\ninput 1002 to choose course 1002 (default fees 15500.0)\nyour choice: "))
            if self.course==1001 and self.__marks>85:
                self.fees =25575.0- 0.25*25575.0
            elif self.course==1001 and self.__marks<=85:
                self.fees =25575.0
            elif self.course==1002 and self.__marks>85:
                self.fees =15500.0- 0.25*15500.0
            elif self.course==1002 and self.__marks<=85:
                self.fees =15500.0
            print(f"\nyou have joined course {self.course} and your fees is {self.fees}")
            

s1=student()
s1.set_details(int(input("enter id: ")),int(input("enter marks: ")),int(input("enter age: ")))
s1.choose_course()
    
        
        

'''

#OR

class Student:
    def init(self):
        self.__s_id=None
        self.__s_age=None
        self.__s_marks=None
    def validate_marks(self):
        if(self.__s_marks>0 and self.__s_marks<100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.__s_age>20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age() and self.__s_marks>65):
            return True
        else:
            return False
        
        
    def choose(self,c_id):
        if self.check_qualification():
            if(c_id == 1001):
                f = 25575.0
                if(self.__s_marks>85):
                    fees_to_paid = f - f*0.25
                    print("fees to be paid is ",fees_to_paid)
                else:
                    print("fees to be paid is ",f)
            elif(c_id == 1002):
                f = 15500.0
                if(self.__s_marks>85):
                    fees_to_paid = f - f*0.25
                    print("fees to be paid is ",fees_to_paid)
                else:
                    print("fees to be paid is ",f)
            else:
                print("Invalid couse id")  
        else:
            print("not eligible")
    def set_id(self,x):
        self.__s_id = x
    def get_id(self):
        return self.__s_id
    def set_age(self,x):
        self.__s_age = x
    def get_age(self):
        return self.__s_age
    def set_marks(self,x):
        self.__s_marks = x
    def get_marks(self):
        return self.__s_marks

    
s1=Student()
s1.set_id(1010)
s1.set_age(98)
s1.set_marks(66)
s1.choose(1009)

s2=Student()
s2.set_id(1011)
s2.set_age(36)
s2.set_marks(99)
s2.choose(1001)

'''










            
            
            
            
        
        
        
        
    
  








































        
