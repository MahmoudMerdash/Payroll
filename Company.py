from Payroll import *
from Employees import *
from Invoice import *
 

class Company:
    def __init__(self):
        self.payroll = Payroll()
        
    def run(self):
        self.payroll.add_payable(Volunteer("Mahmoud Abdellatif Abdellaziz", "Elharam", "0109397", "29501", 2550))
        self.payroll.add_payable(HourlyEmployee("Ahmed Abdellatif Abdellaziz", "Elharam", "010939", "29501223","20-5-2023", 200,10))
        self.payroll.add_payable(SalariedEmployees('Ziad', "Elharam", "010939", "29501223","20-5-2023",2500))
        self.payroll.add_payable(ComissionedEmployee('Asmaa', "Cairo", "010939", "29501223","20-5-2023",2500,100,10))

        invoice = Invoice(1234)
        invoice.add_item(Item("Book", 10,10))
        invoice.add_item(Item("foood",1,1000))
        self.payroll.add_payable(invoice)
        
        print(self.payroll.amount_to_pay) #11650 (2550+2000+2500+3500+100+1000)


if __name__ == '__main__':
    Company().run()