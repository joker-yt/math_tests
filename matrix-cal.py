import random
import pandas as pd

class Matrix(object):
    def __init__(self, digit, calculator, minus=False):
        self.digit = digit
        self.calculate = calculator
        self.number_column = []
        self.number_row = []
        if digit == 1:
            self.number_column = [1,2,3,4,5,6,7,8,9]
            random.shuffle(self.number_column)
            self.number_row = [1,2,3,4,5,6,7,8,9]
            random.shuffle(self.number_row)
        elif digit == 2:
            while len(self.number_column) < 10:
                n = random.randint(1,99)
                if (n in self.number_column) == False:
                    self.number_column.append(n)
                
            while len(self.number_row) < 10:
                n = random.randint(1,99)
                if (n in self.number_row) == False:
                    self.number_row.append(n)

    def get_column(self):
        return self.number_column
    
    def get_row(self):
        return self.number_row
    
    def calculate(self, x, y):
        return self.calculate(x, y)
    

print("Welcome to the addition table practice!")
while 1:
    digit = int(input("Enter the number of digits for the number: (1 or 2) "))
    if digit in [1, 2]:
        break
    print("Invalid input. Please enter 1 or 2.")

while 1:
    print("minus number is allowed? (y/n)")
    minus = input().lower()
    if minus in ['y', 'n']:
        if minus == 'y' and digit == 2:
            print("Minus number is not allowed for 2-digit addition.")
            continue
        minus = True
        break
    print("Invalid input. Please enter 'y' or 'n'.")
    
while 1:
    print("which calculator do you want to use? (+, -, *, /)")
    calc = input()
    if calc in ['+', '-', '*', '/']:
        if calc == '+':
            function = lambda x, y: x + y
        elif calc == '-':
            function = lambda x, y: x - y
        elif calc == '*':
            function = lambda x, y: x * y
        elif calc == '/':
            function = lambda x, y: x / y if y != 0 else 'undefined'
        break

matrix = Matrix(digit=digit, calculator=function)

# ============================================================
# Start the game
# ============================================================
print("Column:", matrix.get_column())
print("Row:", matrix.get_row())

print("ready to check the answer?")
input("Press Enter to continue...")

# ============================================================
# Check the answer
# ============================================================
for i in matrix.get_row():
    for j in matrix.get_column():
        print(matrix.calculate(i,j), end="\t")
    print()