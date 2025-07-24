import csv
from datetime import datetime

FILENAME = "attendance.csv"

def initialize_csv():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Student Name", "Status"])
    except FileExistsError:
        pass  # File already exists

def mark_attendance():
    date = datetime.now().strftime("%Y-%m-%d")
    student_name = input("Enter student name: ").strip()
    status = input("Enter status (P for Present / A for Absent): ").strip().upper()
    if status not in ["P", "A"]:
        print("Invalid status. Use P or A.")
        return
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, student_name, "Present" if status == "P" else "Absent"])
    print("Attendance marked!")

def view_attendance():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No attendance records found.")

def main():
    initialize_csv()
    while True:
        print("\n--- Student Attendance Tracker ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
