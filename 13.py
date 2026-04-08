name = input("Enter student name: ")
dob = input("Enter Date of Birth: ")
usn = input("Enter USN: ")
dept = input("Enter Department: ")

print("Enter marks of 5 subjects:")
a1 = int(input("Subject 1: "))
a2 = int(input("Subject 2: "))
a3 = int(input("Subject 3: "))
a4 = int(input("Subject 4: "))
a5 = int(input("Subject 5: "))

total = a1 + a2 + a3 + a4 + a5
percentage = total / 5

print("\n--- Student Details ---")
print("Name:", name)
print("DOB:", dob)
print("USN:", usn)
print("Department:", dept)

print("Total Marks:", total)
print("Percentage:", percentage, "%")