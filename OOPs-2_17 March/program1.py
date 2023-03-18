#Q.1
class Vehicle:
    def __init__(self,idvehicle,typevehicle,cost):
        self.__id=idvehicle
        self.__type=typevehicle
        self.__cost=cost
        self.__pr=None
    def prem(self):
        if(self.__type=='Two Wheeler'):
            self.__pr=0.02
            print("Vehicle id:",self.__id)
            print("Vehicle type:",self.__type)
            print("Vehicle cost:",self.__cost)
            print("Premium:",self.__pr*self.__cost)
        elif(self.__type=='Four Wheeler'):
            self.__pr=0.06
            print("Vehicle id:",self.__id)
            print("Vehicle type:",self.__type)
            print("Vehicle cost:",self.__cost)
            print("Premium:",self.__pr*self.__cost)
        else:
            print("Invalid type")
            
    def set_id(self,x):
        self.__id = x
    def get_id(self):
        return self.__id
    def set_type(self,x):
        self.__type = x
    def get_type(self):
        return self.__type
    def set_cost(self,x):
        self.__cost = x
    def get_cost(self):
        return self.__cost
        
        
car=Vehicle(230,"Four Wheeler",750000)
car.prem()
print()
car.set_id(213)
car.prem()
print()
bike=Vehicle(230,"Two Wheeler",750000)
bike.prem()

