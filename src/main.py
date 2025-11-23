from planner import add_subject, view_plan
from progress import log_progress
from reports import show_report

def menu():
    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add Subje ct & Topics")
        print("2. View Study Plan")
        print("3. Log Progress")
        print("4. Show Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_subject()
        elif choice == "2":
            view_plan()
        elif choice == "3":
            log_progress()
        elif choice == "4":
            show_report()
        elif choice == "5":
            print("Goodbyeeeee!")
            break
        else:
            print("Invalid choice. Try again:( ")

menu()
