
students = {}

def add_student():
    name = input("Enter student name: ")
    score = float(input("Enter score: "))
    students[name] = score
    print("✔ Student added!\n")

def view_students():
    print("\n--- All Students ---")
    for n, s in students.items():
        print(f"{n} : {s}")
    print()

def update_score():
    name = input("Enter name to update: ")
    if name in students:
        new_score = float(input("Enter new score: "))
        students[name] = new_score
        print("✔ Score updated!\n")
    else:
        print("❌ Student not found!\n")

def search_student():
    name = input("Search name: ")
    print(f"Score: {students.get(name, 'Not found')}\n")

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Deleted!\n")
    else:
        print(" Student not found!\n")

while True:
    print("1. Add Student")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Score")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1": add_student()
    elif choice == "2": view_students()
    elif choice == "3": update_score()
    elif choice == "4": search_student()
    elif choice == "5": delete_student()
    elif choice == "6": break
    else: print("Invalid choice!\n")