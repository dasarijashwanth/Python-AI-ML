# PYTHON ASSIGNMENT 2: Loops, if-else, Lists and Strings


# Q1. Class Marks Report
print("===== Q1. Class Marks Report =====")
marks = [78, 45, 92, 33, 67, 88, 51, 29]

passed = 0
for m in marks:
    if m >= 35:
        passed = passed + 1

average = sum(marks) / len(marks)

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Class average:", average)
print("Students passed:", passed)


# Q2. Grocery Shopping List
print()
print("===== Q2. Grocery Shopping List =====")
shopping_list = []

while True:
    item = input("Enter item: ")
    if item == "done":
        break
    if item in shopping_list:
        print("Already added")
    else:
        shopping_list.append(item)

number = 1
for item in shopping_list:
    print(str(number) + ". " + item)
    number = number + 1

print("Total items:", len(shopping_list))


# Q3. Username Validator
print()
print("===== Q3. Username Validator =====")
username = input("Enter username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid: Username must be between 5 and 12 characters")
elif " " in username:
    print("Invalid: Username cannot contain spaces")
elif username[0] in "0123456789":
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


# Q4. Vowel Counter for a Tweet
print()
print("===== Q4. Vowel Counter for a Tweet =====")
sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for ch in sentence.lower():
    if ch in "aeiou":
        vowels = vowels + 1
    elif ch in "bcdfghjklmnpqrstvwxyz":
        consonants = consonants + 1
    elif ch == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


# Q5. Palindrome Name Checker
print()
print("===== Q5. Palindrome Name Checker =====")
name = input("Enter your name: ")
name = name.lower()

reversed_name = ""
for ch in name:
    reversed_name = ch + reversed_name

if name == reversed_name:
    print("Bonus! Your name is a palindrome.")
else:
    print("Your name is not a palindrome.")


# Q6. Temperature Tracker
print()
print("===== Q6. Temperature Tracker =====")
temps = [32, 35, 38, 41, 36, 29, 40]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Heat alert days:")
for i in range(len(temps)):
    if temps[i] > 37:
        print(days[i], temps[i])

hottest = max(temps)
for i in range(len(temps)):
    if temps[i] == hottest:
        print("Hottest day:", days[i], hottest)

fahrenheit = []
for c in temps:
    fahrenheit.append(c * 9 / 5 + 32)
print("Temperatures in Fahrenheit:", fahrenheit)


# Q7. Word Frequency in a Sentence
print()
print("===== Q7. Word Frequency in a Sentence =====")
sentence = input("Enter a sentence: ")
words = sentence.split()

longest = words[0]
shortest = words[0]
capital_count = 0

for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word
    if word[0] == word[0].upper() and word[0] != word[0].lower():
        capital_count = capital_count + 1

print("Longest word:", longest)
print("Shortest word:", shortest)
print("Words starting with capital letter:", capital_count)


# Q8. Remove Negative Balances
print()
print("===== Q8. Remove Negative Balances =====")
balances = [1500, -200, 3000, -50, 0, 750, -1000]

positive_accounts = []
negative_accounts = []

for b in balances:
    if b > 0:
        positive_accounts.append(b)
    elif b < 0:
        negative_accounts.append(b)

print("Positive accounts:", positive_accounts)
print("Negative accounts:", negative_accounts)
print("Total amount owed:", -sum(negative_accounts))


# Q9. Password Strength Checker
print()
print("===== Q9. Password Strength Checker =====")
password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True

count = 0
if has_upper:
    count = count + 1
if has_lower:
    count = count + 1
if has_digit:
    count = count + 1
if len(password) >= 8:
    count = count + 1

if count == 4:
    print("Strong")
elif count == 2 or count == 3:
    print("Medium")
else:
    print("Weak")


# Q10. Simple Name Initials Generator
print()
print("===== Q10. Simple Name Initials Generator =====")
full_name = input("Enter full name: ")
parts = full_name.split()

initials = ""
title_name = ""
short_name = ""

for part in parts:
    initials = initials + part[0].upper() + "."
    title_name = title_name + part[0].upper() + part[1:].lower() + " "

for i in range(len(parts) - 1):
    short_name = short_name + parts[i][0].upper() + ". "
last = parts[len(parts) - 1]
short_name = short_name + last[0].upper() + last[1:].lower()

print(initials)
print(title_name)
print(short_name)
