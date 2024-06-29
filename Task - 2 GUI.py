import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # Strength criteria
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper and has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def assess_password_strength():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return
    
    strength = check_password_strength(password)
    if strength == 0:
        strength_text = "Very Weak"
    elif strength == 1:
        strength_text = "Weak"
    elif strength == 2:
        strength_text = "Moderate"
    elif strength == 3:
        strength_text = "Strong"
    elif strength == 4:
        strength_text = "Very Strong"
    
    messagebox.showinfo("Password Strength", f"Password Strength: {strength_text}")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter your password:")
label.grid(row=0, column=0, padx=10, pady=10)

password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(frame, text="Check Strength", command=assess_password_strength)
check_button.grid(row=1, columnspan=2, padx=10, pady=10)

root.mainloop()


