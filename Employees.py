class StaffMemebr:
    def __init__(self, name: str, address: str, phone_number: str, ID:str):
        super().__init__()
        self.name = name
        self.address = address #it will not change again so there is no setter methods 
        self._phone_number = phone_number #it will not change again so there is no setter methos 
        self.__ID = ID
        
    @staticmethod
    def name_process(name):
        
        first, *last_name = name.split(' ')
        last_name = " ".join(last_name)
        return first, last_name
    @property 
    def name(self):
        return f"{self.first_name} {self.last_name}"
    @name.setter
    def name(self, name):
        self.first_name, self.last_name = StaffMemebr.name_process(name)
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        self._address = address
    @property
    def phone_number(self):
        return self._phone_number
    @property
    def ID(self):
        return self.__ID
    
    
class Employees(StaffMemebr):
    def __init__(self, name: str, address: str, phone_number: str, ID:str, day_to_pay):
        super().__init__(name, address, phone_number, ID)
        self.day_to_pay = day_to_pay #its is the date to pay for that employees 
        
        @property
        def day_to_pay(self):
            return self._day_to_pay
        @day_to_pay.setter
        def day_to_pay(self, day_to_pay):
            self._day_to_pay =day_to_pay
        
class HourlyEmployee(Employees):
    def __init__(self, name: str, address: str, phone_number: str, ID:str, 
                 day_to_pay, total_working_hour:int, salalry_per_hour):
        super().__init__(name, address, phone_number, ID, day_to_pay)
        self.total_working_hour = total_working_hour
        self.salalry_per_hour = salalry_per_hour
    @property
    def amount_to_pay(self):
       return self.total_working_hour * self.salalry_per_hour
        
class SalariedEmployees(Employees):
    def __init__(self, name: str, address: str, phone_number: str, ID:str,
                 day_to_pay, monthly_salary):
        super().__init__(name, address, phone_number, ID, day_to_pay)
        self.monthly_salary = monthly_salary
        
    @property
    def amount_to_pay(self):
        return self.monthly_salary
    
class ComissionedEmployee(SalariedEmployees):
    def __init__(self, name: str, address: str, phone_number: str, ID:str, 
                 day_to_pay, monthly_salary, comission_rate, current_month_sales):
        super().__init__(name, address, phone_number, ID, day_to_pay, monthly_salary)
        self.comission_rate = comission_rate 
        self.current_month_sales = current_month_sales
        
    @property
    def amount_to_pay(self):
        return    super().amount_to_pay + self.comission_rate * self.current_month_sales

class Volunteer(StaffMemebr):
    def __init__(self,name: str, address: str, phone_number: str, ID:str, current_payment):
        super().__init__(name, address, phone_number,ID)
        self.current_payment = current_payment
    
    def upgrade_to_salaried_employee(self,day_to_pay, monthly_salary):
        return SalariedEmployees(self.name, self.address, self.phone_number, self.ID, day_to_pay, monthly_salary)
    
    @property
    def amount_to_pay(self):
        return self.current_payment
 
 
          
if __name__ == "__main__":
    s = Volunteer("Mahmoud Abdellatif Abdellaziz", "Elharam", "01093970079", 
                          "29501222101873", 2550)
    print(s.name)
    print(s.ID)
    print(s.address)
    print(s.phone_number)
    # print(s.day_to_pay)
    print(s.amount_to_pay)