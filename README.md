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

The workflow of this system is as follows:

![cashier flowchart](https://user-images.githubusercontent.com/123367779/216753815-00475521-e8ac-40c3-be94-04f4de280372.png)

# Code Description
There are 3 modules:
1. Transaction.py contains the Transaction class definitions, including all the attributes and methods associated with it
2. user_input.py contains the functions to ask users to input the details of items they wanted to add or modify
3. main.py is the main code combining all the features mentioned previously into the proper workflow

# Test Case Result
1. Start transaction and add item
