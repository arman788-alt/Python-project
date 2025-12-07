class Calculator:

    def add(self, num1, num2):
       return num1 + num2

    def subtract(self, num1, num2):
       return num1 - num2

    def multiply( self, num1, num2):
       return num1*num2

    def divide(self, num1, num2):

      if num2 == 0:
         return f"Can not divide by 0"
    
      return num1/num2
    


    def Menu(self):

        print("="*40)
        print("Calculator")
        print("="*40)
        print("List of Options: ")
        print("1. press for Add")
        print("2. press for Subtract")
        print("3. press for Multiply")
        print("4. press for Divide")
        print("5. press for Exit")
        print("="*40)

    
    def run(self):

        while True:
          
          self.Menu()

          choice = input("Enter your option: ")

          if choice == "5":
             break
          
          if choice not in ['1', '2', '3', '4', '5']:
             print("Invalid Option")
             continue


          try:
             num1 = int(input("Enter number 1: "))
             num2 = int(input("Enter number 2: "))
          except ValueError:
             print("The value is not Allowed")
             continue
          

          if choice == "1":
             print(f"The addition result: {num1} + {num2} = {int(self.add(num1, num2))}")
    
          elif choice == "2":
             print(f"The subtraction result: {num1} - {num2} = {(self.subtract(num1, num2))}")
    
    
          elif choice == "3":
             print(f"The multiplication result: {num1} * {num2} = {(self.multiply(num1, num2))}")
    
    
          elif choice == "4":
            print(f"The Divison result: {num1} / {num2} = {(self.divide(num1, num2))}")
        
         
        

   

calc = Calculator()

calc.run()


















# Project Overview
# In this project, you will build a fully functional calculator in Python. You will start
# with simple functions, gradually add user interaction, handle errors, and finally
# convert the entire system into an object-oriented, menu-driven calculator program.
# Your goal is to combine all tasks into one project, understanding each step as a
# building block for the final calculator.


# Project Requirements
# 1. Create Arithmetic Functions

# As the base of your calculator, write four separate Python functions:
#  A function to add two numbers
#  A function to subtract two numbers
#  A function to multiply two numbers
#  A function to divide two numbers (must handle division-by-zero safely)


# These functions form the foundation for all later steps.

# 2. User Input & Displaying Results

# Ask the user to enter two numbers.

# Using the functions above, display:

#  The addition result

#  The subtraction result

#  The multiplication result

#  The division result (show appropriate message for division by zero)

# 3. Input Validation

# Create a separate function that:

#  Takes user input

#  Uses try–except to check if the input is a valid number

#  Repeats until the user enters a valid number

# This ensures the calculator never crashes due to invalid inputs.

# 4. Menu-Based Calculator

# Turn your calculator into a menu-driven program.

# Show a list of options:

# 1. Add

# 2. Subtract

# 3. Multiply

# 4. Divide

# 5. Exit

# Keep the calculator running inside a while loop so the user can perform unlimited

# operations until they choose Exit.

# Also print each result in a formatted way, such as:

# 5 + 3 = 8

# 5. Convert to Object-Oriented Calculator

# Create a Calculator class that contains all the arithmetic methods:

#  add()

#  subtract()

#  multiply()

#  divide() (must return a custom message for division by zero)

# Then:

# A. Add a menu() method

# Inside the class, create a method that prints all available options.

# B. Add a run() method

# This method will:

#  Display the menu

#  Take user input

#  Ask for two numbers

#  Perform the selected operation

#  Keep looping until the user chooses Exit

# This method acts as the “controller” for the whole calculator project.

# C. Create a Calculator object

# At the end of the program, create an instance of the Calculator class and call the

# run() method so the entire calculator system starts automatically.

# Submission Instructions
#  Submit your assignment as a GitHub repository link or a ZIP file

#  Important: Submissions without a valid link or ZIP file will receive zero (0)

# marks