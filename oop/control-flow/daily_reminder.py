# Filename: daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task that requires immediate attention"
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            reminder = f"'{task}' priority level is not recognized."

    if time_bound == "yes":
        reminder += " today!"

    print("Reminder:", reminder)

if __name__ == "__main__":
    main()
