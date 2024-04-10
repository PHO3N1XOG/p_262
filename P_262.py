import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

def perform_operation():
    equation = expression_entry.get()

    if equation.strip() == "":
        messagebox.showerror("Error", "Please enter a mathematical expression")
        return

    operation = operation_var.get()

    if operation == "Simplify":
        simplify_expression(equation)
    else:
        messagebox.showerror("Error", "Invalid operation selected")

def simplify_expression(equation):
    # Construct the API URL
    api_url = 'https://newton.now.sh/api/v2/simplify/' + equation

    try:
        # Get the result from the API
        response = requests.get(api_url)
        data = response.json()

        # Display the operation
        operation_label.config(text="Operation for given equation: " + data['operation'])

        # Display the expression
        expression_label.config(text="Expression for given equation: " + data['expression'])

        # Display the result
        result_label.config(text="Result of given equation: " + data['result'])

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to retrieve data from the API")

# Create the main window
root = tk.Tk()
root.title("Math Expression Solver")
root.geometry("400x300")

# Set background color
root.configure(bg="#f0f0f0")

# Create and place widgets
expression_label = tk.Label(root, text="Enter the mathematical expression:", bg="#f0f0f0")
expression_label.pack()

expression_entry = tk.Entry(root)
expression_entry.pack()

operation_label = tk.Label(root, text="Select operation:", bg="#f0f0f0")
operation_label.pack()

operation_var = tk.StringVar()
operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=["Simplify"])
operation_dropdown.pack()

operation_dropdown.current(0)

perform_button = tk.Button(root, text="Perform Operation", command=perform_operation)
perform_button.pack()

result_frame = tk.Frame(root, bg="#f0f0f0")
result_frame.pack(pady=10)

operation_label = tk.Label(result_frame, text="", bg="#f0f0f0")
operation_label.pack()

expression_label = tk.Label(result_frame, text="", bg="#f0f0f0")
expression_label.pack()

result_label = tk.Label(result_frame, text="", bg="#f0f0f0")
result_label.pack()

# Run the main event loop
root.mainloop()
