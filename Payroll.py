class Payroll:
    def __init__(self):
        self.payables = []
    
    def add_payable(self, payable):
        self.payables.append(payable)
    
    @property
    def amount_to_pay(self):
        return sum([payable.amount_to_pay for payable in self.payables])
        
