class DigitalWallet :
  def __init__(self):
    self.owner_name = input("Enter owner name : ")
    self.wallet_balance = 0
    self.show_menu()

  def show_menu(self):
      choice = input("""
      welcome! choose a option:
      1.Add money
      2.Pay Bill
      3.View Balance
      4.Exit 
      your choice is : """)
      
      if choice == "1":
         self.add_money()
      elif choice =="2":
         self.pay_bill()
      elif choice == "3": 
         self.view_balance()
      elif choice == "4":
         print("Thankyou for using DigitalWallet") 
      else :
         print("invalid choice")
         self.show_menu()

  def add_money(self):
     
      try :
           amount = float(input("enter amount : "))
           if amount > 0:
              self.wallet_balance += amount
              print("Amount added successfully!")
              self.show_menu()
           else:
              print("enter valid amount")
      except ValueError :
         print("Invalid Amount!")
         self.show_menu()

  def pay_bill(self):
     try :
        amount = float(input("enter amount to pay : "))

        if amount <= 0 :
           print("please enter valid amount")
        elif amount > self.wallet_balance :
           print("Insufficient Balance")   
        else :
           self.wallet_balance -= amount
           print("Bill paid successfully!")
     except :
        print("Invalid Amount")
        self.show_menu()   

  def view_balance(self):
     print("Owner : ",self.owner_name)
     print("Your Balance is : ",self.wallet_balance)
     self.show_menu()  

wallet = DigitalWallet()           

               
   
         



         