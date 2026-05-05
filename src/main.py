import utils

print("Fahim Ferdous")
print("Simple calculator using utils.py")

operations = {
    "1": ("Add", utils.add),
    "2": ("Subtract", utils.subtract),
    "3": ("Multiply", utils.multiply),
    "4": ("Divide", utils.divide),
}

print("\nChoose an operation:")
for key, (label, _) in operations.items():
    print(f"{key}. {label}")

choice = input("Enter choice (1-4): ").strip()
if choice not in operations:
    print("Invalid choice. Please run the program again and choose 1-4.")
else:
    try:
        a = float(input("Enter the first number: ").strip())
        b = float(input("Enter the second number: ").strip())
        label, func = operations[choice]
        result = func(a, b)
        print(f"\n{label} result: {result}")
    except ValueError:
        print("Invalid number entered. Please enter numeric values.")
    except Exception as err:
        print(f"Error: {err}")
