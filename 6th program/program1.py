1. Simple GUI Calculator
import tkinter as tk
def calculate(op):
 a = float(entry1.get())
 b = float(entry2.get())
 if op == "+":
 result = a + b
 elif op == "-":
 result = a - b
 elif op == "*":
 result = a * b
 elif op == "/":
 result = a / b if b != 0 else "Cannot divide by zero"
 result_label.config(text="Result: " + str(result))
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()
tk.Button(root, text="Addition", command=lambda: calculate("+")).pack()
tk.Button(root, text="Subtraction", command=lambda: calculate("-")).pack()
tk.Button(root, text="Multiplication", command=lambda: calculate("*")).pack()
tk.Button(root, text="Division", command=lambda: calculate("/")).pack()
result_label = tk.Label(root, text="Result: ")
result_label.pack()
root.main loop ()