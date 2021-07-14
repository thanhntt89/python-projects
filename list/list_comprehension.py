class listComprehension():
    transactions = [100, 200, 500, 980]
    TAX_RATE = 0.08
    SERVICE_CHARGE = 0.07

    def getPriceTaxService(self, bill):
        return bill*(1+self.TAX_RATE + self.SERVICE_CHARGE)
