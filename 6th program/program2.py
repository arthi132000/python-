import tkinter as tk
def add():
 result.set(float(num1.get()) + float(num2.get()))
def subtract():
 result.set(float(num1.get()) - float(num2.get()))
def multiply():
 result.set(float(num1.get()) * float(num2.get()))
def divide():
 if float(num2.get()) != 0:
 result.set(float(num1.get()) / float(num2.get()))
 else:
 result.set("Error")
root = tk.Tk()
root.title("Button Calculator")
root.geometry("300x300")
tk.Label(root, text="Number 1").pack()
num1 = tk.Entry(root)
num1.pack()
tk.Label(root, text="Number 2").pack()
num2 = tk.Entry(root)
num2.pack()
tk.Button(root, text="+", command=add).pack()
tk.Button(root, text="-", command=subtract).pack()
tk.Button(root, text="*", command=multiply).pack()
tk.Button(root, text="/", command=divide).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
root.mainloop()