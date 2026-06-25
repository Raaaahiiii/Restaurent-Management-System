from food_item import FoodItem 
from menu import Menu 
from user import Customer,Admin,Employee
from restaurent import Restaurent
from orders import Order

mamar_restaurent = Restaurent("Mamar Restaurent ")

def customer_menu():
    name= input("Enter your Name: ")
    email= input("Enter your Email: ")
    phone= input("Enter your phone number: ")
    address= input("Enter your address: ")

    customer = Customer(name=name, email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu ")
        print("2. Add item to Cart ")
        print("3. View Cart ")
        print("4. Pay Bill ")
        print("5. Exit!! ")

        choice = int(input("Enter your Choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name= input("Enter item Name: ")
            item_quantity= int(input("Enter item quantity: "))
            customer.add_to_cart(mamar_restaurent,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid Input,Try Again! ")
def admin_menu():
    name= input("Enter your Name: ")
    email= input("Enter your email: ")
    phone= input("Enter your phone number: ")
    address= input("Enter your address: ")     

    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name}")
        print("1. Add New Item ")
        print("2. Add New Employee ")
        print("3. View Employee ")
        print("4. View Items ")
        print("5. Delete Items ")
        print("6. Exit! ")

        choice = int(input("Enter your Choice: "))
        if choice == 1:
            item_name= input("Enter Item Name: ")
            item_price= int(input("Enter Item Price: "))
            item_quantity= int(input("Enter Item Quantity: "))
            item= FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurent,item)
        elif choice == 2:
           name= input("Enter Employees Name: ")
           phone= input("Enter employess Phone: ")
           email= input("Enter employees email: ")
           address= input("Enter employees Address: ")
           designation= input("Enter employees designation: ")
           age= input("Enter Employees age: ")
           salary= input("Enter employees salary: ")
           employee= Employee(name,email,phone,address,age,designation,salary)
           admin.add_employee(mamar_restaurent,employee)
        elif choice==3:
           admin.view_employee(mamar_restaurent)
        elif choice==4:
            admin.view_menu(mamar_restaurent)
        elif choice==5:
            item_name= input("Enter item name: ")
            admin.remove_item(mamar_restaurent,item_name)    
        elif choice==6:
            break
        else:
            print("Invalid Input,Try Again! ")
while True:
    print(" WELCOME at MAMAR RESTAURENT ")
    print("1. Are you a Customer? ")
    print("2. Are you a Admin?  ")
    print("3. Exit!! ")
  

    choice = int(input(" Who you are: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid Input,Try Again! ")        
