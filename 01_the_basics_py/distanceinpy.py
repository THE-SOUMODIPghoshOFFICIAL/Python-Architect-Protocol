# Problem 1.2 
# The distance between two cities (in kilometers) is input through the 
# keyboard. Write a program to convert and print this distance in meters, 
# feet, inches and centimeters.

# --- Conversion Constants ---
# Using constants makes the code more readable and easier to maintain.
KM_TO_METERS = 1000
METERS_TO_CENTIMETERS = 100
METERS_TO_FEET = 3.28084
FEET_TO_INCHES = 12

def get_distance_input():
    """
    Prompts the user for a distance in kilometers and handles input validation.
    Returns the distance as a float or None if input is invalid.
    """
    try:
        distance_str = input("\nEnter the distance in kilometers (km): ")
        distance_km = float(distance_str)
        if distance_km < 0:
            print("❌ Error: Distance cannot be negative. Please enter a positive number.")
            return None
        return distance_km
    except ValueError:
        print("❌ Error: Invalid input. Please enter a valid number.")
        return None

def convert_and_print(distance_km):
    """
    Converts the given kilometers to other units and prints the results.
    """
    # --- Perform Conversions ---
    # We first convert to a base unit (meters) and then derive others.
    meters = distance_km * KM_TO_METERS
    centimeters = meters * METERS_TO_CENTIMETERS
    feet = meters * METERS_TO_FEET
    inches = feet * FEET_TO_INCHES

    # --- Print Results ---
    # Using f-strings with formatting for a clean, aligned output.
    print(f"\n✅ Result: {distance_km} km is equal to:")
    print(f"   -> {meters:,.2f} meters")
    print(f"   -> {centimeters:,.2f} centimeters")
    print(f"   -> {feet:,.2f} feet")
    print(f"   -> {inches:,.2f} inches")

def main():
    """
    Main function to run the distance converter application.
    """
    print("--- Distance Unit Converter ---")

    while True:
        distance_km = get_distance_input()

        if distance_km is not None:
            convert_and_print(distance_km)

        # --- Ask to Continue ---
        another = input("\nDo you want to convert another distance? (yes/no): ").lower()
        if another not in ('yes', 'y'):
            break

    print("\nThank you for using the converter. Goodbye! 👋")

# --- Run the Program ---
# This standard Python construct ensures the main() function is called
# only when the script is executed directly.
if __name__ == "__main__":
    main()
