class listComprehension():    
    TAX_RATE = 0.08
    SERVICE_CHARGE = 0.07
        
    def getPriceTaxService(self, bill):
        return bill*(1 + self.TAX_RATE + self.SERVICE_CHARGE)
    
    def getBill(self, transactions):
        final_bill = [self.getPriceTaxService(bill) for bill in transactions]
        return final_bill

def main():
    listUtils = listComprehension()
    transactions = [20, 500, 30]
    print(f'Current transactions:{transactions}')
    print(f'After calculated:{listUtils.getBill(transactions)}')

if __name__ == "__main__":
    main()
