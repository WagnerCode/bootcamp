from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31',
        info=None
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))
    print(bank.accounts[0].__dict__)
    print(bank.accounts[1].__dict__)
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')

        bank.fix_account('William John')
        bank.fix_account('Smith Jane')
        print(bank.accounts[0].__dict__)
        print(bank.accounts[1].__dict__)
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')
