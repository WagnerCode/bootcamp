


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

    #def __str__(self):
    #    return f'{self.name} {self.value}'



class Bank(object):

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        print("added")
        if isinstance(new_account, Account):
            self.accounts.append(new_account)


    def transfer(self, origin, dest, amount):

        a = None
        b = None
        flagForTransfer = 0
        for item in self.accounts:
            if item.name == dest:
                b = item
            elif item.name == origin:
                a = item

        flag = 0
        flagA = 1
        flagB = 0

        if (len(a.__dict__) % 2 != 0):
            print("haha")
            for item in a.__dict__:
                if (item[0]) == 'b':
                    flag = 1

            if flag == 0:
                for item in a.__dict__:
                    if item == 'zip' or item == 'addr':
                        flagA = 0

            if flagA == 0:
                for item in a.__dict__:
                    if item == 'name':
                        if isinstance(item, str):
                            flagB += 1
                        else:
                            print("name is not a str")
                        flagB += 1

                    elif item == 'id':
                        if isinstance(a.__dict__[item], int):
                            flagB += 1
                        flagB += 1

                    elif item == 'value':
                        if isinstance(a.__dict__[item], float):
                            flagB += 1
                        flagB += 1
            print(flagB)
            if flagB == 6:
                flagForTransfer += 1

        flag = 0
        flagA = 1
        flagB = 0

        if (len(b.__dict__) % 2 != 0):
            print("haha")
            for item in b.__dict__:
                if (item[0]) == 'b':
                    flag = 1

            if flag == 0:
                for item in b.__dict__:
                    if item == 'zip' or item == 'addr':
                        flagA = 0

            if flagA == 0:
                for item in b.__dict__:
                    if item == 'name':
                        if isinstance(item, str):
                            flagB += 1
                        else:
                            print("name is not a str")
                        flagB += 1

                    elif item == 'id':
                        if isinstance(b.__dict__[item], int):
                            flagB += 1
                        flagB += 1

                    elif item == 'value':
                        if isinstance(b.__dict__[item], float):
                            flagB += 1
                        flagB += 1
            print(flagB)
            if flagB == 6:
                flagForTransfer += 1

        if flagForTransfer == 2:
            if amount <= a.value:
                a.value = a.value - amount
                b.value = b.value + amount
        else:
            return False

    # ... Your code ...
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        for item in self.accounts:
            pass
            if item.name == name:
                if not hasattr(item, 'addr'):
                    item.addr = "Somewhere"

