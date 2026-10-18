
class BankATM:
    def __init__(self):
        self.secret_code = ""
        self.account_bal = 0
        self.show()

    def show(self):
        choice = input("""
        Welcome! Choose an option:
        1. Create PIN
        2. Change PIN
        3. Check Balance
        4. Withdraw Cash
        5. Deposit Cash
        6. Exit
        Your choice is: """)

        if choice == "1":
            self.set_pin()
        elif choice == "2":
            self.update_pin()
        elif choice == "3":
            self.check_balance()
        elif choice == "4":
            self.do_withdraw()
        elif choice == "5":
            self.do_deposit()
        elif choice == "6":
            print("Thank you for using our ATM!")
        else:
            print("Invalid choice!")
            self.show()

    def set_pin(self):
        new_code = input("Enter a PIN: ")
        self.secret_code = new_code

        opening_balance = int(input("Opening balance: "))
        self.account_bal = opening_balance

        print("PIN Created!")
        self.show()

    def update_pin(self):
        current = input("Enter your current PIN: ")

        if current == self.secret_code:
            new_pin = input("Enter new PIN: ")
            self.secret_code = new_pin
            print("PIN Updated!")
        else:
            print("Wrong PIN!")

        self.show()

    def check_balance(self):
        current_pin = input("Provide your PIN: ")

        if current_pin == self.secret_code:
            print("Your balance:", self.account_bal)
        else:
            print("Wrong PIN!")

        self.show()

    def do_withdraw(self):
        current_pin = input("Provide your PIN: ")

        if current_pin == self.secret_code:
            amount = int(input("Enter amount to withdraw: "))

            if amount > 0 and amount <= self.account_bal:
                self.account_bal -= amount
                print("New account balance:", self.account_bal)
            else:
                print("Invalid amount or insufficient balance!")
        else:
            print("Wrong PIN!")

        self.show()
    def do_deposit(self):
      current_pin = input("provide your PIN : ")
      if current_pin == self.secret_code:
        try:
            amount = float(input("Enter Amount to Deposit : "))
            if amount > 0 :
                self.account_bal += amount
                print("new account balance is : ", self.account_bal)

            else :
                print("Amount must be greater than Zero")    

        except ValueError :
            print("Please enter valid amount")

      else :
            print("wrong PIN")   
                     

      self.show()      
        





obj1 = BankATM()
