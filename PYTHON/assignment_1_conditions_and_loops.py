# Q1. Movie Ticket Counter
age = int(input("Enter your age: "))
if age < 5:
    print("Your ticket is Free")
elif age <= 17:
    print("Your ticket price is Rs. 100")
elif age <= 59:
    print("Your ticket price is Rs. 200")
else:
    print("Your ticket price is Rs. 120")

# Q2. Electricity Bill Calculator
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units - 100) * 5
else:
    bill = 100 * 3 + 100 * 5 + (units - 200) * 8
print("Total bill: Rs.", bill)

# Q3. Multiplication Table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Q4. Savings Piggy Bank
total = 0
days = 0
while total < 1000:
    total += int(input("Enter today's savings: "))
    days += 1
print("Goal reached in", days, "days! Total saved: Rs.", total)

# Q5. ATM PIN Check
attempts = 0
while attempts < 3:
    pin = int(input("Enter PIN: "))
    if pin == 4321:
        print("Access granted")
        break
    print("Wrong PIN")
    attempts += 1
if attempts == 3:
    print("Card blocked")

# Q6. Even and Odd Counter
n = int(input("Enter N: "))
even = odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# Q7. Number Guessing Game
secret = 27
guesses = 0
while True:
    guess = int(input("Guess the number: "))
    guesses += 1
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct! You took", guesses, "guesses.")
        break

# Q8. Exam Result with Grade
marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")

# Q9. Sum of Digits on a Bill Number
num = int(input("Enter bill number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)
if total > 20:
    print("Congratulations! You win a free gift.")
else:
    print("Sorry, no gift this time.")

# Q10. Staircase Pattern
steps = int(input("Enter number of steps: "))
for i in range(1, steps + 1):
    for j in range(i):
        print("*", end=" ")
    print()
