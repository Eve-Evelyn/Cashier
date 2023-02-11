# Self-service Cashier
This is the python code for a cashier system to generate, modify, and summarize a transaction

# Background
To lower operating expenses, a business can opt to have a self-service cashier instead of a conventional manned cashier station. This self-service cashier will allow customer to input the details of the items that they would like to purchase. The system will then be able to provide the summary of their order and the total amount need to be paid to complete the transaction. Other than reducing the number on manpower needed in the store, the self-service cashier will also allow customers to make purchases remotely online and have the items delivered to them.

# System Features and Workflow
To start using this, make sure the all 3 files are downloaded in the same location and then run main.py

The main features of this system are:
1. Add new items and its details
2. Modify any details of existing items
3. Remove any existing items
4. Reset the transaction to remove all the previously added items
5. Check transaction summary and total price

The system will also be able to catch invalid inputs such as string being inputted when asked to input qty, trying to update an item that has not existed yet in the transaction, etc.

The workflow of this system is as follows:

![cashier flowchart](https://user-images.githubusercontent.com/123367779/216753815-00475521-e8ac-40c3-be94-04f4de280372.png)

# Code Description
There are 3 modules:
1. Transaction.py contains the Transaction class definitions, including all the attributes and methods associated with it
2. user_input.py contains the functions to ask users to input the details of items they wanted to add or modify
3. main.py is the main code combining all the features mentioned previously into the proper workflow

# Test Case Result
1. Start transaction and add item

   ![image](https://user-images.githubusercontent.com/123367779/216757666-ba30afb8-2149-4e9d-b764-fc6c04d6189a.png)
   
2. Update item details
   - Update item name
   
     ![image](https://user-images.githubusercontent.com/123367779/216757845-431a62f0-bd27-4bca-99f8-ee9dc586e132.png)
     
   - Update item qty
   
     ![image](https://user-images.githubusercontent.com/123367779/216757909-692d6b77-370f-4a9e-b821-1e4a11eb015e.png)

   - Update item price

     ![image](https://user-images.githubusercontent.com/123367779/216757944-9fe78606-81c7-4601-873d-deae7587a502.png)

3. Delete an item and check order summary
   
   ![image](https://user-images.githubusercontent.com/123367779/216758100-b760c635-6450-4891-aace-d7c88b13eedf.png)
   
4. Reset transaction and check order summary

   ![image](https://user-images.githubusercontent.com/123367779/216758169-bf356a2f-f116-4d19-9995-89ae262e7481.png)

5. Check order summary, confirm order, and start new transaction

   ![image](https://user-images.githubusercontent.com/123367779/216758353-644ae5a4-368e-4e96-ae54-12791b5256b7.png)

6. Error handling
   - Invalid input
   
     ![image](https://user-images.githubusercontent.com/123367779/216758477-6692dfe6-5fa7-4e45-b7bc-247016a8cb1f.png)

   - Item not found
   
     ![image](https://user-images.githubusercontent.com/123367779/216758526-38f14513-309c-4a57-801e-93580b268ca5.png)

# Further Improvements Needed
1. Add a dictionary containing prices of each item so that the price do not need to be manually added and will be automatically filled once item name is inputted
2. Develop a more proper user interface 
