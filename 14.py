name = input("Enter name: ")
birth_year = int(input("Enter year of birth: "))

current_year = 2026
age = current_year - birth_year

print("\nName:", name)
print("Age:", age)

if age >= 60:
    print("The person is a Senior Citizen")
else:
    print("The person is NOT a Senior Citizen")