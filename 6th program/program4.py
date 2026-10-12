import tkinter as tk
def calculate():
 try:
 a = float(entry1.get())
 b = float(entry2.get())
 op = operator.get()
 if op == "+":
 ans = a + b
 elif op == "-":
 ans = a - b
 elif op == "*":
 ans = a * b
 elif op == "/":
 ans = a / b
 result.config(text="Result = " + str(ans))
 except:
 result.config(text="Invalid Input")
root = tk.Tk()
root.title("Four Function Calculator")
root.geometry("400x350")
tk.Label(root, text="GUI Calculator",
 font=("Arial", 18)).pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
operator = tk.StringVar()
operator.set("+")
tk.Radiobutton(root, text="+", variable=operator,
 value="+").pack()
tk.Radiobutton(root, text="-", variable=operator,
 value="-").pack()
tk.Radiobutton(root, text="*", variable=operator,
 value="*").pack()
tk.Radiobutton(root, text="/", variable=operator,
 value="/").pack()
tk.Button(root, text="Calculate",
 command=calculate).pack(pady=10)
result = tk.Label(root, text="Result = ")
result.pack()
root.mainloop()