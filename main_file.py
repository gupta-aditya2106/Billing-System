import pandas as pd

amount = 0
total_tax = 0

my_product = []
total_price = []
gst_tax = []
# These are empty list created - whenever customer buy products, the name, price and tax
# of each product respectively is appended in this list
csv = pd.read_csv(r"C:\Users\Aditya\Desktop\Projects\Billing System\Products list.csv", index_col="ProductID")

all_products = list(csv.loc[:, 'Products'])
Final_Price = list(csv.loc[:, 'Price'])
final_tax = list(csv.loc[:, 'Tax'])
# These lists shows the items which are already available in the store


print("################################################")
print("#     Welcome to our Showroom: THE HAMAN LLP   #")
print("################################################")
# heading - looks good, thats why
# These are global variables- whenever the customer buys the product, the tax and the amount gets added here
################################################
#                  MAKE CSV                    #
################################################
def make_csv():
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax, Final_Price
   csv.to_csv(r"C:\Users\Aditya\Desktop\Projects\Billing System\Products list.csv")
   csv = pd.read_csv(r"C:\Users\Aditya\Desktop\Projects\Billing System\Products list.csv", index_col="ProductID")
   all_products = list(csv.loc[:, 'Products'])
   Final_Price = list(csv.loc[:, 'Price'])
   final_tax = list(csv.loc[:, 'Tax'])


################################################
#                 MAIN MENU                    #
################################################
# Function defined - This is main function which initially receives the input from customer
# The next step depends on the input given by user here
# This is the main function(sabse important)!!
def main():
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax
   #Global variables - variables used for whole program

   print("\t\t\t +---------------------------+")
   print("\t\t\t |         MAIN MENU         |")
   print("\t\t\t +---------------------------+")
   print("\t\t\t |1. Make Bill               |")
   print("\t\t\t |2. Add Products            |")
   print("\t\t\t |3. Remove Products         |")
   print("\t\t\t |4. Logout                  |")
   print("\t\t\t +---------------------------+")
 
   step1 = int(input("What do you want to do?"))
   if step1 == 1:
       billing()
       # To make bill
   elif step1 == 2:
       add()
       # To add products in the store(in the list all_products)
   elif step1 == 3:
       delete()
       # To delete products from the store(from the list all_products)
   elif step1 == 4:
       logout()


################################################
#                 NEW PRODUCT                  #
################################################
# Function Created - To add products in the list [all_products] and other global lists
def add():
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax
   # Global variables - variables used for whole program
   print(csv)
   #Here, dataframe of available products is created to help user choose correct input

   new_p = str(input("Enter the Product you want to add in the list>>"))
   new_pp = int(input("Enter the price for that Product>>"))
   new_ptax = int(input("Enter the Tax for that Product>>"))
   new_pid = str(input("Enter the Product ID of product you want to add in the list>>"))
   #input about new items is taken from user - like name, price, tax

   all_products.append(new_p)
   Final_Price.append(new_pp)
   final_tax.append(new_ptax)
   df_new=pd.DataFrame([[ new_p, new_pp,  new_ptax]], columns=['Products', 'Price', 'Tax'], index=[new_pid])
   df_new.index.name = 'ProductID'

   #csv=csv.append(df_new)
   csv = pd.concat([csv, df_new])
   make_csv()
   print(csv)
   # The input about new information is appended in the list which was containing whole data of available items

   print("...Your Products are successfully added...")
   # To give confirmation to user that products are added

   main()
   # After add() function work is done, main() will take you back to the main function
   # Again ask you about what to do next


################################################
#                DELETE PRODUCT                #
################################################
# Function Created - To delete products from the list [all_products] and other global lists
def delete():
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax
   # Global variables - variables used for whole program
   print(csv)
   # Here, dataframe of available products is created to help user choose correct input

   delete_p = str(input("Enter the Product ID you want to delete from the list"))
   # input about items to be deleted is taken from user - like name, price, tax
   #index = all_products.index(delete_p) # This will give the index no. of the item which we want to delete
                                       # (the index no. is stored in a variable - index)
   csv = csv.drop(index = delete_p)
   make_csv()
   print("...Your Products are successfully deleted...")
   make_csv()
   # To give confirmation to user that products are added

   main()
   # After delete() function work is done, main() will take you back to the main function
   # Again ask you about what to do next


################################################
#                 BUY PRODUCT                  #
################################################
# Function Created - To have input of the item details that the customer wants to buy
def buy(pid, quantity):
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax
   # Global variables - variables used for whole program

   price = csv.loc[pid, 'Price']       # This will store the price of the item which we want to buy(the Price is
                                       # stored in a variable - price)
   tax = csv.loc[pid, 'Tax']           # This will store the tax of the item which we want to buy(the Tax is stored in
                                       # a variable - tax)
   prod = csv.loc[pid, 'Products']
   # here we could have used if-else statements, but that would give us problem in the future,
   # while adding/deleting items
   x = quantity * price
   y = (x*tax)/100
   # Mathematical formulas used to calculate amount and Tax on the product selected

   total_price.append(x)
   gst_tax.append(y)
   my_product.append(prod)
   # This will append the empty lists -  which we made in the starting - with the products that we have selected
   # and respective price and tax

   amount += x
   total_tax += y
   # The variable which we created in the start(amount and total_tax), where we kept values = 0
   # Now we will add the price and tax calculated from the above formulas in it


################################################
#             END BILLING FUNCTION             #
################################################
# Function Created - To end the process of buying items and produce bill
def end():
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax
   # Global variables - variables used for whole program

   final_bill = {'Products': my_product, 'Price': total_price, 'Tax':gst_tax}
   Bill = pd.DataFrame(final_bill)
   # This will make dataframe of the products that user wants to buy

   print("...............................Your Bill is Generated......................................")
   print("..........")
   print(Bill)
   # This will print the dataframe of the products as BILL

   print("..........")
   print('Total Price of Products......', amount)
   print('Total Tax on products........', total_tax)
   print('Total Amount to be paid is...', amount + total_tax)
   # This specifies - amount, tax, and total payable
   print("..........")
   print("..........")


################################################
#                   MAKE BILL                  #
################################################
# Function Created - To start the process of billing(includes buying itens and making bill)
# buy() and end() are used inside this
def billing():
   global amount, price, all_products, my_product, total_price, total_tax, final_tax, csv, gst_tax
   # Global variables - variables used for whole program
   print(csv)
   # Here, dataframe of available products is created to help user choose correct input

   p = str(input('Enter the Product ID You want to buy...............'))
   q = int(input('Enter the quantity of Product You want to buy...'))
   print("..........")
   # Input of details of items that user wants to buy
   buy(p, q)

   # Loop Created - To ask user whether to proceed with more products or to stop.
   while True:
       cont = input("Want to buy more? (y/n)")

       if cont == "y":
           p = str(input('Enter the Product ID You want to buy...............'))
           q = int(input('Enter the quantity of Product You want to buy...'))
           print("..........")
           buy(p, q)

       elif cont == "n":
           print("..........")
           end()
           print("Thank You for shopping with us")
           print("...........................................................................................")
           break

       else:
           print("Either type y or n")
   main()
   # After billing() function work is done, main() will take you back to the main function
   # Again ask you about what to do next


################################################
#                   PASSWORD                   #
################################################
def password():
   pas = input("Enter your Password>>")
   if pas == 'haman123':
       main()
   else:
       print('Invalid Password')
       password()


################################################
#                    LOGOUT                    #
################################################
def logout():
   op = input('Are you sure, You want to logout?(y/n)')
   if op == 'y':
       print("You are successfully logged out")
   elif op == 'n':
       main()


password()
# The first function is password().
# This is top priority.
# All other functions defined inside this.



