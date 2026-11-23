# PYTHON ASSIGNMENT 3: Loops, if-else, Sets, Tuples, Dictionaries


# Q1. Phone Contact Book
print("===== Q1. Phone Contact Book =====")
contacts = {}

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found")
    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "4":
        break
    else:
        print("Invalid choice")


# Q2. Unique Visitors on a Website
print()
print("===== Q2. Unique Visitors on a Website =====")
visits = [101, 205, 101, 330, 205, 412, 101, 330, 509]

unique_visitors = set(visits)

print("Total visits:", len(visits))
print("Unique visitors:", len(unique_visitors))
print("Unique visitor IDs:", sorted(unique_visitors))


# Q3. Student Marks Dictionary
print()
print("===== Q3. Student Marks Dictionary =====")
marks = {"Aman": 82, "Priya": 91, "Rahul": 45,
         "Sneha": 67, "Kiran": 30}

for name, mark in marks.items():
    if mark >= 40:
        print(name, "- Pass")
    else:
        print(name, "- Fail")

topper = ""
top_marks = 0
for name, mark in marks.items():
    if mark > top_marks:
        top_marks = mark
        topper = name
print("Topper:", topper, "with", top_marks, "marks")

passed_students = {}
for name, mark in marks.items():
    if mark >= 40:
        passed_students[name] = mark
print("Passed students:", passed_students)


# Q4. Common Friends
print()
print("===== Q4. Common Friends =====")
riya_friends = {"Aman", "Neha", "Karan", "Sita", "Vikram"}
arjun_friends = {"Neha", "Vikram", "Pooja", "Aman", "Rohan"}

print("Mutual friends:", riya_friends.intersection(arjun_friends))
print("Only Riya's friends:", riya_friends.difference(arjun_friends))
print("All people:", riya_friends.union(arjun_friends))
print("Suggestions for Riya:", arjun_friends.difference(riya_friends))


# Q5. Character Counter
print()
print("===== Q5. Character Counter =====")
text = input("Enter text: ")

counts = {}
for ch in text:
    if ch != " ":
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1
print(counts)

most_char = ""
most_count = 0
for ch, count in counts.items():
    if count > most_count:
        most_count = count
        most_char = ch
print("Most frequent character:", most_char, "(" + str(most_count) + " times)")


# Q6. Restaurant Menu Billing
print()
print("===== Q6. Restaurant Menu Billing =====")
menu = {"dosa": 60, "idli": 40, "vada": 30,
        "coffee": 25, "tea": 15}

total = 0
while True:
    item = input("What would you like to order? ")
    if item == "bill":
        break
    if item in menu:
        total = total + menu[item]
    else:
        print("Item not available")

print("Total bill: Rs.", total)
if total > 200:
    discount = total * 10 / 100
    total = total - discount
    print("10% discount applied: Rs.", discount)
    print("Amount to pay: Rs.", total)


# Q7. City Coordinates (Tuples)
print()
print("===== Q7. City Coordinates (Tuples) =====")
cities = [("Hyderabad", 17.38, 78.48),
          ("Mumbai", 19.07, 72.87),
          ("Chennai", 13.08, 80.27),
          ("Delhi", 28.61, 77.20)]

for city, lat, lon in cities:
    print(city, "- Latitude:", lat, "Longitude:", lon)

north_city = ""
north_lat = 0
for city, lat, lon in cities:
    if lat > north_lat:
        north_lat = lat
        north_city = city
print("Farthest north:", north_city, "(" + str(north_lat) + ")")

# cities[1][1] = 20.00
# This gives: TypeError: 'tuple' object does not support item assignment
# Reason: tuples are immutable, so their values cannot be changed
# after the tuple is created.


# Q8. Library Book Tracker
print()
print("===== Q8. Library Book Tracker =====")
books = {"Python Basics": 3, "Data Science 101": 0,
         "Machine Learning": 2, "SQL Guide": 1}

book = input("Enter book name to borrow: ")

if book not in books:
    print("Book not found")
elif books[book] == 0:
    print("Currently unavailable")
else:
    books[book] = books[book] - 1
    print("Book issued successfully")

print(books)


# Q9. Group Employees by Department
print()
print("===== Q9. Group Employees by Department =====")
employees = [("Ravi", "IT"), ("Anjali", "HR"),
             ("Suresh", "IT"), ("Meena", "Finance"),
             ("Arun", "HR"), ("Divya", "IT")]

departments = {}
for name, dept in employees:
    if dept in departments:
        departments[dept].append(name)
    else:
        departments[dept] = [name]
print(departments)

for dept, names in departments.items():
    print(dept, ":", len(names), "employees")


# Q10. Quiz Answer Checker
print()
print("===== Q10. Quiz Answer Checker =====")
answer_key = ("B", "C", "A", "D", "B")

wrong = set()
score = 0

for i in range(5):
    answer = input("Enter answer for question " + str(i + 1) + ": ")
    if answer == answer_key[i]:
        print("Question", i + 1, "is correct")
        score = score + 1
    else:
        print("Question", i + 1, "is wrong")
        wrong.add(i + 1)

print("Wrong questions:", wrong)
print("Score:", score, "out of 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Needs improvement")
