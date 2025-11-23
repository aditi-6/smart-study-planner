from storage import load_data, save_data

def log_progress():
    data = load_data()
    subject = input("Enter subject: ")
  
    if subject not in data["subjects"]:
        print("Subject not found.")
      
        return

    hours = float(input("How many hours studied today? "))
    entry = {"subject": subject, "hours": hours}

    data["logs"].append(entry)
    save_data(data)

    print("Progress logged successfully.")

