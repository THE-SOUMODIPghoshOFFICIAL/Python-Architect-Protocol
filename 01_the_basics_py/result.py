# If the marks obtained by a student in five different subjects are input 
# through the keyboard, write a program to find out the aggregate marks 
# and percentage marks obtained by the student. Assume that the 
# maximum marks that can be obtained by a student in each subject is 
# 100.

# --- Configuration Constants ---
NUMBER_OF_SUBJECTS = 5
MAX_MARKS_PER_SUBJECT = 100

def get_subject_marks():
    """
    Prompts the user to enter marks for a specified number of subjects.
    Includes validation to ensure marks are numeric and within the valid range.
    Returns a list of marks or None if the user quits.
    """
    marks_list = []
    print(f"\nEnter marks for {NUMBER_OF_SUBJECTS} subjects (0-{MAX_MARKS_PER_SUBJECT}). Type 'quit' to exit.")
    
    for i in range(1, NUMBER_OF_SUBJECTS + 1):
        while True:
            try:
                mark_str = input(f"  -> Enter marks for Subject {i}: ")
                if mark_str.lower() == 'quit':
                    print("...Input cancelled by user.")
                    return None

                mark = float(mark_str)
                if 0 <= mark <= MAX_MARKS_PER_SUBJECT:
                    marks_list.append(mark)
                    break  # Exit the while loop for the current subject
                else:
                    print(f"❌ Error: Marks must be between 0 and {MAX_MARKS_PER_SUBJECT}.")
            except ValueError:
                print("❌ Error: Invalid input. Please enter a number.")
    return marks_list

def calculate_and_print_results(marks_list):
    """
    Calculates and prints the aggregate and percentage marks.
    """
    # --- Perform Calculations ---
    aggregate_marks = sum(marks_list)
    total_max_marks = NUMBER_OF_SUBJECTS * MAX_MARKS_PER_SUBJECT
    percentage = (aggregate_marks / total_max_marks) * 100

    # --- Print Results ---
    print("\n✅ Student Report Card:")
    print("-" * 25)
    print(f"   Aggregate Marks: {aggregate_marks:.2f} / {total_max_marks}")
    print(f"   Percentage:      {percentage:.2f}%")
    print("-" * 25)

def main():
    """
    Main function to run the student marks calculator.
    """
    print("--- Student Marks Calculator ---")
    while True:
        marks = get_subject_marks()

        if marks:  # Proceed only if a valid list of marks was returned
            calculate_and_print_results(marks)

        another = input("\nCalculate for another student? (yes/no): ").lower()
        if another not in ('y', 'yes'):
            break
    
    print("\nThank you for using the calculator. Goodbye! 👋")

if __name__ == "__main__":
    main()
