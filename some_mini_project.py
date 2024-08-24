'''
1. Write a Python program that asks the user to enter their marks. 

Based on the marks, the program should print the grade according to the following criteria:
Marks >= 90: Grade A
Marks >= 80 and < 90: Grade B
Marks >= 70 and < 80: Grade C
Marks >= 60 and < 70: Grade D
Marks < 60: Grade F
'''

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
elif marks >= 60 and marks < 70:
    grade = "D"
else:
    grade = "F"

print("Your Grade is", grade)     

# 2. Write a program that takes three numbers as input and prints the largest and smallest of the three using conditional statements.

num1 = float(input("Enter Your first Number: "))
num2 = float(input("Enter Your second Number: "))
num3 = float(input("Enter Your third Number: "))

if num1 >= num2 and num1 < num3:
    largest = num1
elif num2 >= num1 and num2 < num3:
    largest = num2
else:
    largest = num3


# Find the smallest number
if num1 >= num2 and num1 < num3:
    smallest = num1
elif num2 >= num1 and num2 < num3:
    smallest = num2
else:
    smallest = num3

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")    


#3. Write a Python program that checks if a given year is a leap year. A year is a leap year if it is divisible by 4 but not by 100 unless it is also divisible by 400.
    
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

year = int(input("Enter a Year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


#4. Write a Python program that takes an integer as input and checks if the number is even or odd.

num = float(input("Entar a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "id odd")


#5. Write a program that takes a character input from the user and checks if it is a vowel or a consonant.

char = input("Enter a character: ").lower()  

if char.isalpha() and len(char) == 1:  
    if char in 'aeiou':  
        print(f"{char} is a vowel.")  
    else:  
        print(f"{char} is a consonant.")  
else:  
    print("Please enter a single alphabet letter:")  


#6. Write a Python program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding arithmetic operation. If the operator is not recognized, print an error message.

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/":
    if second_num != 0:
        result = first_num / second_num
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operator."

print("Result:", result)


'''
7. Write a program that takes the user's age as input and prints out the age category:
Age < 13: Child
Age >= 13 and < 20: Teenager
Age >= 20 and < 60: Adult
Age >= 60: Senior Citizen
'''

age = float(input("Enter your age: "))

if age < 13:
    category = "Child" 
elif age >= 13 and age < 20:
    category = "Teenager"
elif age >= 20 and age < 60:
    category = "Adult"
else: 
    category = "Senior Citizen"

print(f"Your age category is: {category}")    

#8. Write a Python program that takes the lengths of three sides of a triangle and determines if the triangle is equilateral, isosceles, or scalene.
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "Isosceles"
    else:
        return "Scalene"
    
triangle_type = classify_triangle(side1,side2,side3)

print(f"The classify_triangle is: {triangle_type}")

#9. Write a program that converts a temperature from Celsius to Fahrenheit and vice versa based on user input. Use conditional statements to determine which conversion to perform.

unit = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").upper()

if unit == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
elif unit == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
    

#10. Write a Python program that takes a number as input and checks if it is divisible by 5, 7, or both. Print the appropriate message based on the divisibility.
number = int(input("Enter a number: "))
if number % 5 == 0 and num % 7 == 0:
    print(f"{number}is divisible by both 5 and 7.")
elif number % 5 == 0:
    print(f"{number}is divisible by 5.")  
elif number % 5 == 0:
    print(f"{number}is divisible by 5.")
else:
    print(f"{number} is not divisible by either 5 or 7.")      

