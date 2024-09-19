#  Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
# focusing on the use of private attributes and getters and setters.

# Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget.
# - Initialize these attributes in the constructor.

# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. 
# - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. 
# - Validate the expense amount before making deductions from the budget.

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, 
# allocated budget, and remaining budget after expenses.

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.


class BudgetCategory:
    def __init__(self, category_name, budget):
        self.__category_name = category_name
        self.__budget = budget
        budgets.append(self)

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_budget_remaining(self):
        return self.__budget
    
    def set_budget_remaining(self, new_amount):
        self.__budget = new_amount

    def add_expense(self, amount):
        if 0 < amount <= self.get_budget_remaining():
            self.set_budget_remaining(self.get_budget_remaining() - amount)
            print(f"{amount} was added as an expense to {self.get_category_name()}")
        else:
            print(f"There isn't enough money left in the {self.get_category_name()} budget for that expense.")

    def display_category_summary(self):
        print(f"Category: {self.get_category_name()}, Budget Remaining: {self.get_budget_remaining()}")
        
budgets = []

food_category = BudgetCategory("Food", 500)
medical_category = BudgetCategory("Medical", 800)
entertainment_category = BudgetCategory("Entertainment", 200)
rent_category = BudgetCategory("Rent", 1500)

food_category.add_expense(100)
medical_category.add_expense(650)

for budget in budgets:
    budget.display_category_summary()