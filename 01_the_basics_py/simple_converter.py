# simple_converter.py
# A straightforward temperature converter for beginners.


# - Converts between Celsius, Fahrenheit, and Kelvin.
# - Prompts the user for a value and a unit.
# - Includes a loop to allow multiple conversions.
# - Adds basic error handling for non-numeric input.

print("--- Simple Temperature Converter ---")

# This loop lets the user do multiple conversions without restarting the script.
while True:
    # --- Get User Input ---

    # Get the temperature value from the user.
    # We use a try-except block to handle cases where the user types text instead of a number.
    try:
        temp_value_str = input("\nEnter the temperature value: ")
        temp_value = float(temp_value_str)
    except ValueError:
        print("❌ Error: Please enter a valid number for the temperature.")
        continue # Skip the rest of this loop iteration and ask again.

    # Get the unit from the user.
    unit = input("What is the unit? (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    # --- Perform Conversion based on the unit ---

    if unit == 'C':
        # Convert from Celsius to Fahrenheit and Kelvin
        fahrenheit = (temp_value * 9/5) + 32
        kelvin = temp_value + 273.15
        
        print(f"\n✅ Result: {temp_value}°C is:")
        print(f"   -> {fahrenheit:.2f}°F (Fahrenheit)")
        print(f"   -> {kelvin:.2f}K (Kelvin)")

    elif unit == 'F':
        # Convert from Fahrenheit to Celsius and Kelvin
        celsius = (temp_value - 32) * 5/9
        kelvin = celsius + 273.15 # Calculate Kelvin from the new Celsius value
        
        print(f"\n✅ Result: {temp_value}°F is:")
        print(f"   -> {celsius:.2f}°C (Celsius)")
        print(f"   -> {kelvin:.2f}K (Kelvin)")

    elif unit == 'K':
        # Convert from Kelvin to Celsius and Fahrenheit
        celsius = temp_value - 273.15
        fahrenheit = (celsius * 9/5) + 32 # Calculate Fahrenheit from the new Celsius value
        
        print(f"\n✅ Result: {temp_value}K is:")
        print(f"   -> {celsius:.2f}°C (Celsius)")
        print(f"   -> {fahrenheit:.2f}°F (Fahrenheit)")

    else:
        # Handle cases where the user enters an invalid unit
        print(f"❌ Error: Invalid unit '{unit}'. Please use C, F, or K.")

    # --- Ask to Continue ---

    # Ask the user if they want to do another conversion.
    another = input("\nDo you want to convert another temperature? (yes/no): ").lower()
    if another != 'yes' and another != 'y':
        break # Exit the while loop

print("\nThank you for using the converter. Goodbye! 👋")