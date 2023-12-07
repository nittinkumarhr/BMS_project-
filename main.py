from datetime import datetime
import pandas as pd

class CakeManagement:   
    order_quantity = pd.DataFrame(columns=["Customer Name", "Contact", "Item", "Quantity", "Order Date"])

    def __init__(self, choice):
        self.choice = choice
        if choice == "1":
            self.add_order()  
        elif choice == "2":
            self.view_order()
        elif choice == "3":
            self.save_to_csv()
        elif choice == "4":
            self.update_order()   
        elif choice == "5":
            print("Thank you for using our services")
            exit()
        else:
            print("Invalid choice")
            e = input("Do you want to continue? (y/n)")
            if e == "y":
                self.under_choice()
            else:
                print("Thank you for using our services")
                exit()
    def update_order(self):
        print("\n<><><><><><><><><><><>><><>><><>Updating Order<><><><><><><><<><><><><><><>\n")
        order_id = int(input("Enter order ID to update: "))
        if order_id >= len(self.order_quantity):
            print("Order not found.")
        else:
            print("Updating Order ID:", order_id)
            self.order_quantity.at[order_id, "Item"] = input("Enter new item: ")
            self.order_quantity.at[order_id, "Quantity"] = int(input("Enter new quantity: "))
            print("Order updated successfully!")
    def under_choice(self):
        
        print("""  WELCOME TO bakery management system 
        
        1. Add order
        2. View order 
        3. Save to Excel 
        4. Update Order
        5. Exit """)
        choice = input("Enter your choice: ")
        self.__init__(choice)
        
    def add_order(self):
        print("<><><><><><><><><><>(Add order)<><><><><><><><><><<><<><><>")
        c_name = input("Enter customer name: ")
        c_phone = input("Enter customer phone: ")
        c_order = input("Enter order: ")
        c_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c_quantity = input("Enter quantity: ")
        add_quantity = pd.DataFrame([[c_name, c_phone, c_order, c_quantity, c_date]], 
                                 columns=["Customer Name", "Contact", "Item", "Quantity", "Order Date"])
        
        CakeManagement.order_quantity = pd.concat([CakeManagement.order_quantity, add_quantity], ignore_index=True)
        #print('Order added successfully', CakeManagement.order_quantity)
   

    def view_order(self):   
        print("<><><><><><><><><><>(View order)<><><><><><><><><><<><<><><>")
        if CakeManagement.order_quantity.empty:
            print('No orders available.')
        else:
            print(CakeManagement.order_quantity)
    def save_to_csv(self):
        path = "CakeManagement.csv"
        CakeManagement.order_quantity.to_csv(path, index=False)
        print("Order saved successfully in CSV format")

        
        
    

while True:        
    print("""  WELCOME TO bakery management system 
        
        1. Add order
        2. View order 
        3. Save to Excel 
        4.Update order 
        5. Exit """)
    choice = input("Enter your choice: ")
    obj_BMS = CakeManagement(choice)
