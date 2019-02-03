# SI 507 - Lab 3


class Currency:
    unit_name = "currency"

    def __init__(self, value):
        self.value = value
        self.base_rate = 1

    def conversion(self, result_currency_reference):
        if(type(self) == Pound):
            rate = Pound.rate
        elif (type(self) == Yuan):
            rate = Yuan.rate
        elif (type(self) == Dollar):
            rate = Dollar.rate
        else:
            return "Can't convert. Please enter a valid currency."

        #Conversion
        value_in_currency = self.value * rate
        value_at_reference_rate = value_in_currency / result_currency_reference.rate
        return result_currency_reference(value_at_reference_rate)


class Dollar(Currency):
    unit_name = "Dollar"
    rate = 20

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        if self.value <= 1:
            return "{} Dollar".format(self.value)
        else:
            return "{} Dollars".format(self.value)


class Yuan(Currency):
    unit_name = "Yuan"
    rate = 8

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "{} Yuan".format(self.value)

class Pound(Currency):

    unit_name = "Pound"
    rate = 15

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        if self.value <= 1:
            return "{} Pound".format(self.value)
        else:
            return "{} Pounds".format(self.value)


if __name__ =="__main__":

    dollar = Dollar(1)
    pound = Pound(1)
    yuan = Yuan(1)

    print(yuan.conversion(Pound))
    # 0.5333333333333333 Pound

    print(pound.conversion(Pound))
    # 1.0 Pound

    print(pound.conversion(Dollar))
    # 0.75 Dollar

    print(dollar)
    # 1 Dollar

    two_dollars = Dollar(2)
    print(two_dollars)
    # 2 Dollars


class Bank:
    def __init__(self, name, unit, current_account = 0):
        self.name = name
        # self.current_account = current_account
        self.unit = unit
        if unit == Pound:
            self.current_account = Pound(current_account)
        elif unit == Dollar:
            self.current_account = Dollar(current_account)
        elif unit == Yuan:
            self.current_account = Yuan(current_account)

    def __str__(self):
        return "{} Bank holds the {} currency and currently holds {} of {}".format(self.name, self.unit.unit_name ,self.current_account.value,self.unit.unit_name)

    def __repr__(self):
        return self.name

    def deposit(self, unit2):

        if type(unit2) == self.unit:
            self.current_account.value = self.current_account.value + 1
            return 'successful deposit'

        else:
            return 'ERROR: cannot deposit that currency.'

if __name__ =="__main__":

    jpMorgan = Bank("J.P.Morgan", Dollar, 1)
    barclays = Bank("Barclays", Pound, 1)
    bank_of_china = Bank("Bank of China", Yuan, 1)

    print(jpMorgan.current_account.value)
    # should show: 1

    print(jpMorgan.deposit(dollar))
    # should show: 'successful deposit'

    print(jpMorgan.current_account.value)
    # should show: 2

    print(jpMorgan.deposit(pound))
    # should show: 'ERROR: cannot deposit that currency.'
