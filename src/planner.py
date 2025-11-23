from storage import load_data, save_data

def add_subject():
    data = load_data()
    subject = input("Enter subject name: ")

    if subject in data["subjects"]:
        print("Subject already exists.")
        return

    topics = input("Enter topics (comma separated): ").split(",")
    topics = [t.strip() for t in topics]

    data["subjects"][subject] = {"topics": topics}
    save_data(data)

    print(f"Subject '{subject}' added successfully.")

def view_plan():
    data = load_data()
    if not data["subjects"]:
        print("No subjects added yet.")
        return

    print("\n--- Study Plan ---")
    for sub, det in data["subjects"].items():
        print(f"\n{sub}:")
        for t in det["topics"]:
            print(f" - {t}")
