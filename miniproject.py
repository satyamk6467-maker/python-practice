# expense tracker calculating the all expense 

expenselist=[]
print("welcome to expense tracker :")

while True: 
    print("====menu====")
    print("1.add the expense")
    print("2. view all the expense ")
    print("3. view total  amount ")
    print("4. Exit")

choice=int(input("enter the choice :"))

# add the expense 
if (choice==1):
    date=input("enter the date of spending:")
    category=input("enter the cateogry of spending? (food ,travel,shopping,hangout,chilling):")
    description=input("enter the more details about the spending details :")
    amount=float(input("enter the amount"))

    expense={
        "date": date ,
        "category": category,
        "description":description,
        "amount":amount,
    }
    expenselist.append(expense)
    print("\n Done bro .expense is added sucessfully ")
#view all the expensess
if (choice==2):
    if(len(expenselist)==0):
        print("do some spending :")
    else:
        print("====this is your expense====")
        for eachspending in expenselist:
            print(f"spending number.{count}:{eachspending['date']},{eachspending["cateogry"]},{eachspending["amount"]}")
            count=count+1
    # view the spending
    if(choice==3):
        total=0 
        for eachspending in expenselist:
            total=total+eachspending["amount"]
            print("\n total spending =",total)

# exit
    elif(choice==4):
        print("thank you for using our system")
        break 

    else:
        print("invalid choice .try again ")
 