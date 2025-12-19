# ==========================================
# GUI + AI POWERED CALCULATOR
# ==========================================

import tkinter as tk
import math
import re

# ---------- AI LOGIC ----------
def ai_calculate(text):
    text = text.lower()

    try:
        if "add" in text or "+" in text:
            nums = list(map(float, re.findall(r"-?\d+\.?\d*", text)))
            return sum(nums)

        elif "subtract" in text or "-" in text:
            nums = list(map(float, re.findall(r"-?\d+\.?\d*", text)))
            return nums[0] - nums[1]

        elif "multiply" in text or "x" in text or "*" in text:
            nums = list(map(float, re.findall(r"-?\d+\.?\d*", text)))
            return nums[0] * nums[1]

        elif "divide" in text or "/" in text:
            nums = list(map(float, re.findall(r"-?\d+\.?\d*", text)))
            if nums[1] == 0:
                return "Error: Division by zero"
            return nums[0] / nums[1]

        elif "square root" in text:
            num = float(re.findall(r"\d+\.?\d*", text)[0])
            return math.sqrt(num)

        elif "power" in text or "^" in text:
            nums = list(map(float, re.findall(r"-?\d+\.?\d*", text)))
            return nums[0] ** nums[1]

        else:
            return "I don't understand 😕"

    except:
        return "Invalid input"


# ---------- GUI LOGIC ----------
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    text = entry.get()
    result = ai_calculate(text)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))


# ---------- GUI DESIGN ----------
root = tk.Tk()
root.title("AI Powered Calculator")
root.geometry("350x450")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), bd=5, relief=tk.RIDGE)
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "/", "C"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    action = clear if button == "C" else lambda x=button: button_click(x)
    tk.Button(frame, text=button, width=6, height=2,
              font=("Arial", 14), command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(root, text="AI CALCULATE",
          font=("Arial", 14),
          bg="lightblue",
          command=calculate).pack(fill=tk.BOTH, padx=10, pady=10)

root.mainloop()
