


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        #if (len(self.__dict__) % 2 != 0):
        #    for item in self.__dict__:
        #        if (item[0]) == 'b':
        #            raise AttributeError("Attribute name has litera b")

    def transfer(self, amount):
        self.value += amount


class Bank(object):

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        flag = 0
        flagA = 1
        flagB = 0
        if isinstance(new_account, Account):
            if(len(new_account.__dict__) % 2 != 0):
                print("haha")
                for item in new_account.__dict__:
                    if(item[0]) == 'b':
                        flag = 1

                if flag == 0:
                    for item in new_account.__dict__:
                        if item == 'zip' or item == 'addr':
                            flagA = 0


                if flagA == 0:
                    for item in new_account.__dict__:
                        if item == 'name':
                            if isinstance(item, str):
                                flagB += 1
                            else:
                                print("name is not a str")
                            flagB += 1

                        elif item == 'id':
                            if isinstance(new_account.__dict__[item], int):
                                flagB += 1
                            flagB += 1

                        elif item == 'value':
                            if isinstance(new_account.__dict__[item], float):
                                flagB += 1
                            flagB += 1
                print(flagB)
                if flagB == 6:
                    self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):

        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        a = None
        b = None

        for item in self.accounts:
            print(item)
    # ... Your code ...
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
    # ... Your code ...