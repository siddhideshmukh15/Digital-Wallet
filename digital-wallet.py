balance =0

while True:
    print("\n ==== Digital Wallet ====")
    print("1. 'Check balance' \n 2.'Add Money' \n 3.'Spend money'\n 4.'Exit'")
    
    choice=input("Enter your choice:")
    
    if choice =="1":
        print("Current Balance: rs",balance)
        
    elif choice =="2":
        amount =float(input("Enter amount to add:"))
        
        if amount >0:
            balance += amount
            print("Money added sucessfully !")
            
        else:
            print("Enter a valid amount!")
            
    elif choice =="3":
        amount = float(input("Enter amount to spend:"))
        
        if amount <= 0:
            print("Enter a valid amount!")
            
        elif amount > balance:
            print("Insufficient balance !")
            
        else:
            balance -= amount
            print("payment successful!")
            print("Remaining Balance: rs",balance)
            
    elif choice =="4":
        print("Thank you for using Digital Wallet !")
        break
    
    else:
        print("Invalid choice!")
            
    