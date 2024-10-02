"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

def main():
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            # Write this section to convert F to C and display the result
            celsius = convert_to_celcius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celcius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def display_menu():
    print(MENU)


main()