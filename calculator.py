import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        result_var.set(f"Result: {result}")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")
    except ZeroDivisionError as zde:
        messagebox.showerror("Math Error", f"Error: {zde}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Initialize main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Choose operation:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Create result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.grid(row=4, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
