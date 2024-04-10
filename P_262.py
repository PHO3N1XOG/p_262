import tkinter as tk
from tkinter import messagebox
import requests

def simplify_expression():
    equation = expression_entry.get()

    if equation.strip() == "":
        messagebox.showerror("Error", "Please enter a mathematical expression")
        return

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
root.title("Math Expression Simplifier")

# Create and place widgets
expression_label = tk.Label(root, text="Enter the mathematical expression:")
expression_label.pack()

expression_entry = tk.Entry(root)
expression_entry.pack()

simplify_button = tk.Button(root, text="Simplify", command=simplify_expression)
simplify_button.pack()

operation_label = tk.Label(root, text="")
operation_label.pack()

expression_label = tk.Label(root, text="")
expression_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the main event loop
root.mainloop()
