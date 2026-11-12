# Ohm's Law and Power Calculator
# ND1 Python Mini Project
# Author: Samuel Godwin

# OWN TWIST: Power Safety Check + Calculation History
# - After each calculation, it warns if power is too high
# - It saves all calculations in a history list you can view

# This list stores all past calculations for the history feature
history = []

def show_menu():
    # This function shows the main menu to the user
    print("\n===== OHM'S LAW & POWER CALCULATOR =====")
    print("What do you want to find?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Power (P)")
    print("5. View Calculation History")
    print("6. Exit")

def get_value(prompt):
    # This function gets a number from the user
    # It uses float() to convert input to a decimal number
    # It keeps asking until the user types a valid number
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number, e.g. 10 or 2.5")

def safety_check(power):
    # OWN TWIST: This function warns if power is too high
    # This helps prevent burning a resistor in real life
    if power > 100:
        print("⚠️  SAFETY WARNING: Power is very HIGH (>100W). Use a bigger resistor / check circuit!")
    elif power > 50:
        print("⚠️  Caution: Power is high (>50W). Be careful.")
    else:
        print("✅ Power is safe for a normal small circuit.")

def main():
    # Main loop - program repeats until user chooses Exit
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        # Decision: if/elif/else to choose what to calculate
        if choice == '1':
            # Find Voltage using V = I x R
            print("\n--- Find Voltage ---")
            i = get_value("Enter Current (A): ")
            r = get_value("Enter Resistance (Ohms): ")
            if r == 0:
                print("Error: Resistance cannot be 0 for this calculation.")
                continue
            v = i * r
            # Calculate power also for safety check
            p = v * i
            print(f"\n>>> Voltage (V) = {v:.2f} Volts")
            safety_check(p)
            history.append(f"V = {v:.2f}V (I={i}A, R={r} Ohms)")

        elif choice == '2':
            # Find Current using I = V / R
            print("\n--- Find Current ---")
            v = get_value("Enter Voltage (V): ")
            r = get_value("Enter Resistance (Ohms): ")
            if r == 0:
                print("Error: Cannot divide by zero! Resistance cannot be 0.")
                continue
            i = v / r
            p = v * i
            print(f"\n>>> Current (I) = {i:.2f} Amps")
            safety_check(p)
            history.append(f"I = {i:.2f}A (V={v}V, R={r} Ohms)")

        elif choice == '3':
            # Find Resistance using R = V / I
            print("\n--- Find Resistance ---")
            v = get_value("Enter Voltage (V): ")
            i = get_value("Enter Current (A): ")
            if i == 0:
                print("Error: Cannot divide by zero! Current cannot be 0.")
                continue
            r = v / i
            p = v * i
            print(f"\n>>> Resistance (R) = {r:.2f} Ohms")
            safety_check(p)
            history.append(f"R = {r:.2f} Ohms (V={v}V, I={i}A)")

        elif choice == '4':
            # Find Power using P = V x I
            print("\n--- Find Power ---")
            v = get_value("Enter Voltage (V): ")
            i = get_value("Enter Current (A): ")
            p = v * i
            print(f"\n>>> Power (P) = {p:.2f} Watts")
            safety_check(p)
            history.append(f"P = {p:.2f}W (V={v}V, I={i}A)")

        elif choice == '5':
            # OWN TWIST: Show history
            print("\n--- Calculation History ---")
            if len(history) == 0:
                print("No calculations yet.")
            else:
                for item in history:
                    print("- " + item)

        elif choice == '6':
            print("Thank you for using the calculator! Goodbye.")
            break

        else:
            # Sensible message if user types wrong choice
            print("Invalid choice! Please enter a number from 1 to 6.")

# This starts the program
if __name__ == "__main__":
    main()
