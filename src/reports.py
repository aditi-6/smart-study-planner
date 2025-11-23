from storage import load_data

def show_report():
    data = load_data()
    logs = data["logs"]

    if not logs:
        print("No progress logged yet.")
        return
    summary = {}
  
    for entry in logs:
        sub = entry["subject"]
        summary[sub] = summary.get(sub, 0) + entry["hours"]

    print("\n--- Progress Summary ---")
  
    for sub, hrs in summary.items():
        print(f"{sub}: {hrs} hours")
