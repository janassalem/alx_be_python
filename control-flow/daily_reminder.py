# Filename: daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    reminder = f"Reminder: '{task}' is a {priority} priority task"
    
    match priority:
        case "high":
            reminder += " that requires immediate attention"
        case "medium":
            reminder += "."
        case "low":
            reminder += ". Consider completing it when you have free time."
        case _:
            reminder += ". Note: The priority level is not recognized."

    if time_bound == "yes":
        reminder += " today!"

    print(reminder)

if __name__ == "__main__":
    main()