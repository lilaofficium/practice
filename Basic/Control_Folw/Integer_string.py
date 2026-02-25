score = 78

if score >= 90:
    print("Excellent Data Quality")
elif score >= 70:
    print("Good Data Quality")
elif score >= 50:
    print("Average Data Quality")
else:
    print("Poor Data Quality")


name = "John"
email = ""

if not name:
    print("Name is missing")
elif not email:
    print("Email is missing")
else:
    print("All fields present")

#Check If Data Is Numeric

value = "123"

if value.isdigit():
    print("Valid numeric value")
else:
    print("Invalid number")

#Salary Tax Calculation

salary = 75000

if salary <= 50000:
    tax = salary * 0.1
elif salary <= 100000:
    tax = salary * 0.2
else:
    tax = salary * 0.3

print("Tax:", tax)

# Check If Year Is Leap Year
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# nested if-else
amount = 5000
balance = 10000
account_active = True

if account_active:
    if amount <= balance:
        print("Transaction Approved")
    else:
        print("Insufficient Balance")
else:
    print("Account Inactive")

#Email Validation 
email = "test@gmail.com"

if "@" in email and "." in email:
    print("Valid Email Format")
else:
    print("Invalid Email")

#Password Validation
password = "Data1234"

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            print("Strong Password")
        else:
            print("Add uppercase letter")
    else:
        print("Add a digit")
else:
    print("Password too short")



#
marks = 82

if 90 <= marks <= 100:
    grade = "A"
elif 75 <= marks < 90:
    grade = "B"
elif 50 <= marks < 75:
    grade = "C"
elif 0 <= marks < 50:
    grade = "Fail"
else:
    grade = "Invalid Marks"

print("Grade:", grade)

#
amount = 1200
is_member = True

if is_member:
    if amount > 1000:
        discount = 0.2
    else:
        discount = 0.1
else:
    if amount > 1000:
        discount = 0.1
    else:
        discount = 0

print("Discount:", discount)

# Compare array  with conditions
day = 31
month = 4

if month in [4, 6, 9, 11]:
    if day <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")
elif month == 2:
    if day <= 28:
        print("Valid Date")
    else:
        print("Invalid Date")
else:
    if day <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")

# nested detection of fraud risk based on multiple conditions
amount = 15000
location = "international"
account_age_years = 0.5

if amount > 10000:
    if location == "international":
        if account_age_years < 1:
            print("High Fraud Risk")
        else:
            print("Medium Risk")
    else:
        print("Low Risk")
else:
    print("Normal Transaction")

    