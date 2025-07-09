#function that calculates factorial of given number
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

import tkinter as tk
from tkinter import messagebox

def show_factorial():
    try:
        n = int(entry.get())
        result = factorial(n)
        result_label.config(text=f"Factorial: {result}", fg="green")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Factorial Calculator")

entry = tk.Entry(root)
entry.pack(pady=10)

calc_button = tk.Button(root, text="Calculate Factorial", command=show_factorial)
calc_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
