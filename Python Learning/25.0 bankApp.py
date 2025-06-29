print("=== BANK APPLİCATİON ===")

JamesAccount = {
    'name' : 'James Bond',
    'account_no' : '12345',
    'balance' : 3000,
    'additional_account' : 2000
}

AliceAccount = {
    'name' : 'Alice Spring',
    'account_no' : '67891',
    'balance' : 2000,
    'additional_account' : 1000
}

def withdraw(account, amount):
    print(f"Hello {account['name']}")
    if account['balance'] >=amount:
        account['balance'] -= amount
        print("You can take your money.")
    else:
        total = account['balance'] + account['additional_account']
        if total>=amount:
            additional_account_use= input("Use additional account?(y/n) ")
            if additional_account_use == 'y' :
                additional_account_use_amount=amount-account['balance']
                account['balance'] = 0
                account['additional_account'] -= additional_account_use_amount
                print("You can take your money.")
            else:
                print(f"There is {account['balance']} in your account {account['account_no']}.")

        else:
            print("No enough money.")
            inquiryBalance(JamesAccount)

withdraw(JamesAccount, 4000)

def inquiryBalance(account):
    print(f"There are {account['balance']} in your account {account['account_no']}")