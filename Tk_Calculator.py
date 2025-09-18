import tkinter as tk

# ===== Functions =====
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

# ===== Main Window =====
root = tk.Tk()
root.title("Calculator")
root.geometry("380x560")
root.configure(bg="#1e272e")  

expression = ""
entry_text = tk.StringVar()

# ===== Entry (Screen) =====
entry_frame = tk.Frame(root, bg="#1e272e")
entry_frame.pack(pady=20, padx=20, fill='x')

entry = tk.Entry(
    entry_frame,
    textvar=entry_text,
    font=("Arial", 28, "bold"),
    bd=0,
    bg="#d2dae2",
    fg="#1e272e",
    justify='right',
    relief=tk.FLAT
)
entry.pack(ipady=15, fill='x')
entry_frame.configure(bg="#1e272e")

# ===== Button Layout =====
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

btn_colors = {
    '/': "#34ace0",
    '*': "#34ace0",
    '-': "#34ace0",
    '+': "#34ace0",
    '=': "#33d9b2",
    'C': "#ff5252"
}

def create_button(parent, text, bg_color, command=None):
    """Helper to create styled button"""
    btn = tk.Button(
        parent,
        text=text,
        font=("Arial", 20, "bold"),
        fg="white",
        bg=bg_color,
        activebackground="#57606f",
        bd=0,
        relief=tk.FLAT,
        width=3,
        height=1
    )
    if command:
        btn.config(command=command)
    else:
        btn.bind("<Button-1>", click)
 
    def on_enter(e): btn.config(bg="#747d8c")
    def on_leave(e): btn.config(bg=bg_color)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(side='left', expand=True, fill='both', padx=6, pady=6)
    return btn

# ===== Create Buttons =====
for row in buttons:
    frame = tk.Frame(root, bg="#1e272e")
    frame.pack(expand=True, fill='both', padx=10, pady=5)
    for char in row:
        color = btn_colors.get(char, "#2f3640")
        if char == '=':
            create_button(frame, char, color, command=calculate)
        else:
            create_button(frame, char, color)

# ===== Clear Button =====
clear_frame = tk.Frame(root, bg="#1e272e")
clear_frame.pack(expand=True, fill='both', padx=10, pady=10)

clear_btn = tk.Button(
    clear_frame,
    text='C',
    font=("Arial", 20, "bold"),
    fg="white",
    bg=btn_colors['C'],
    activebackground="#ff7675",
    bd=0,
    relief=tk.FLAT
)
clear_btn.bind("<Button-1>", lambda e: clear())
# Hover for Clear
def on_enter_clear(e): clear_btn.config(bg="#ff7675")
def on_leave_clear(e): clear_btn.config(bg=btn_colors['C'])
clear_btn.bind("<Enter>", on_enter_clear)
clear_btn.bind("<Leave>", on_leave_clear)
clear_btn.pack(expand=True, fill='both', padx=6, pady=6)

root.mainloop()
