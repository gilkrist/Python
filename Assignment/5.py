# QUESTION:
# College Result: 1.Add 2.Mark 3.Report

# Data
students = {}

def add():
    name = input("name: ")
    students[name] = []
    print("added!")

def mark():
    name = input("name: ")
    if name in students:
        students[name].append(int(input("mark: ")))
        print("done!")
    else: print("not found!")

def view():
    for name, marks in students.items():
        if marks:
            avg = sum(marks) / len(marks)
            print(f"{name}: Avg {avg}, GPA {avg/10:.1f}")
        else: print(f"{name}: No marks")

# Loop
while True:
    print("\n1.Add 2.Mark 3.View 4.Exit")
    c = input("choice: ")
    if c == '1': add()
    elif c == '2': mark()
    elif c == '3': view()
    elif c == '4': break
    else: print("invalid!")