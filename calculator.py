
import tkinter as tk

# Function: Add text to the input box
def press_key(key):
    global calc_input
    calc_input += str(key)
    user_text.set(calc_input)

# Function: Clear the screen
def clear_screen():
    global calc_input
    calc_input = ""
    user_text.set("")

# Function: Calculate the result
def get_result():
    global calc_input
    try:
        answer = str(eval(calc_input))
        user_text.set(answer)
        calc_input = answer
    except:
        user_text.set("Error")
        calc_input = ""

# Main Window Setup
window = tk.Tk()
window.title("simple Calculator")
window.geometry("320x400")
window.resizable(False, False)

calc_input = ""
user_text = tk.StringVar()

# Input field
entry_box = tk.Entry(window, textvariable=user_text, font=('Arial', 18), bg="#f5f5f5", bd=8, relief=tk.GROOVE, justify="right")
entry_box.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for btn in buttons:
    if btn == "=":
        tk.Button(window, text=btn, width=7, height=3, command=get_result).grid(row=row, column=col)
    else:
        tk.Button(window, text=btn, width=7, height=3, command=lambda b=btn: press_key(b)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear Button
tk.Button(window, text='Clear', width=31, height=3, command=clear_screen).grid(row=row, column=0, columnspan=4)

window.mainloop()
