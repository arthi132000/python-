import tkinter as tk
def calculate():
 a = float(first.get())
 b = float(second.get())
 op = operation.get()
 if op == "Addition":
 ans = a + b
 elif op == "Subtraction":
 ans = a - b
 elif op == "Multiplication":
 ans = a * b
 elif op == "Division":
 ans = a / b if b != 0 else "Error"
 output.config(text="Answer: " + str(ans))
root = tk.Tk()
root.title("Menu Calculator")
root.geometry("350x300")
tk.Label(root, text="Enter First Number").pack()
first = tk.Entry(root)
first.pack()
tk.Label(root, text="Enter Second Number").pack()
second = tk.Entry(root)
second.pack()
operation = tk.StringVar()
operation.set("Addition")
menu = tk.OptionMenu(
 root, operation,
 "Addition",
 "Subtraction",
 "Multiplication",
 "Division"
)
menu.pack()
tk.Button(root, text="Calculate", command=calculate).pack()
output = tk.Label(root, text="Answer:")
output.pack()
root.mainloop()
