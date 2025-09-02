import tkinter as tk
def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    entry_text.set(expression)


def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except:
        entry_text.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    entry_text.set("")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
entry_text = tk.StringVar()


entry = tk.Entry(root, textvar=entry_text, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill='both', ipadx=8, pady=10, padx=10)


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for char in row:
        if char == '=':
            btn = tk.Button(frame, text=char, font=("Arial", 18), fg="white", bg="green", bd=5, relief=tk.RIDGE, command=calculate)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18), fg="black", bd=5, relief=tk.RIDGE)
            btn.bind("<Button-1>", click)
        btn.pack(side='left', expand=True, fill='both')


clear_btn = tk.Button(root, text='C', font=("Arial", 18), fg="white", bg="red", bd=5, relief=tk.RIDGE, command=clear)
clear_btn.pack(expand=True, fill='both')

root.mainloop()
