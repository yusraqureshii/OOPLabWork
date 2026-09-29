#task1

class person:
      name="yusra"
      gender="female"
      profession="student"
      study_hour=2

      def working(self):
            print(self.name,"is working.")

      def study(self):
            print(self.name,"is studying.")


#task2
class Student:
    def __init__(self, name, roll_no, program, marks):
        self.name = name
        self.roll_no = roll_no
        self.program = program
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Program:", self.program)
        print("Marks:", self.marks)


# Creating Student object
student1 = Student("Ali", 101, "BSCS", 85)

# Displaying student information
student1.display()

#task3
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area:", area)


# Creating two rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)

# Calculating and displaying areas
rectangle1.calculate_area()
rectangle2.calculate_area()

#task4
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)



account1 = BankAccount("Ali", 12345, 10000)

account1.deposit(2000)

# Withdraw money
account1.withdraw(3000)

# Display account information
account1.display_balance()