import random

# Define decision types and their options
decision_types = {
    "Binary": ["Yes", "No"],
    "Directional": ["Left", "Right"],
    "Truth Check": ["True", "False"],
    "Action Choice": ["Go", "Stay"],
    "Vertical Motion": ["Up", "Down"]
}

def show_decision_types():
    print("\nSelect a decision type:")
    for i, key in enumerate(decision_types.keys(), start=1):
        print(f"{i}. {key}")

def get_decision_type():
    while True:
        show_decision_types()
        choice = input("Enter the number of your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(decision_types):
                type_name = list(decision_types.keys())[choice - 1]
                return type_name
        print("Invalid choice, try again.")

def ask_question(decision_set, type_name):
    while True:
        question = input("\nType your question (or leave blank and press Enter): ")
        decision = random.choice(decision_set)
        if question:
            print(f"\nYour question: {question}")
        else:
            print("\nNo question entered.")
        print(f"Decision ({type_name}): {decision}")

        # Next action
        print("\nWhat do you want to do next?")
        print("1. Ask another question in the same type")
        print("2. Select a different decision type")
        next_step = input("Enter 1 or 2: ")
        if next_step == "1":
            continue
        elif next_step == "2":
            break
        else:
            print("Invalid input, returning to decision type menu.")
            break

def main():
    print("Welcome to the Decision Generator App!")

    while True:
        type_name = get_decision_type()
        decision_set = decision_types[type_name]
        ask_question(decision_set, type_name)

        # Optional: ask if user wants to exit
        exit_choice = input("\nDo you want to quit the app? (y/n): ").lower()
        if exit_choice == "y":
            print("Thanks for using the Decision Generator App! Goodbye!")
            break

if __name__ == "__main__":
    main()
