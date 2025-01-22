import tkinter as tk
from tkinter import filedialog, colorchooser
from tkinter import font

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def change_bg_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(bg=color)

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)

def change_font():
    font_family = font_family_var.get()
    font_size = font_size_var.get()
    if font_family and font_size:
        text_area.config(font=(font_family, int(font_size)))

def clear_text():
    text_area.delete(1.0, tk.END)

def save_shortcut(event):
    save_file()

root = tk.Tk()
root.title("Advanced Text Editor")
root.geometry("800x600")


text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH)


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)


options_menu = tk.Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Change Background Color", command=change_bg_color)
options_menu.add_command(label="Change Text Color", command=change_text_color)
menu_bar.add_cascade(label="Options", menu=options_menu)


font_menu = tk.Menu(menu_bar, tearoff=0)
font_family_var = tk.StringVar(value="Arial")
font_size_var = tk.StringVar(value="12")
font_menu.add_command(label="Apply Font", command=change_font)
menu_bar.add_cascade(label="Font", menu=font_menu)

font_menu.add_separator()
font_menu.add_radiobutton(label="Arial", variable=font_family_var, value="Arial")
font_menu.add_radiobutton(label="Courier", variable=font_family_var, value="Courier")
font_menu.add_radiobutton(label="Times New Roman", variable=font_family_var, value="Times New Roman")
font_menu.add_separator()
font_menu.add_radiobutton(label="12", variable=font_size_var, value="12")
font_menu.add_radiobutton(label="16", variable=font_size_var, value="16")
font_menu.add_radiobutton(label="20", variable=font_size_var, value="20")
font_menu.add_radiobutton(label="24", variable=font_size_var, value="24")


root.bind("<Control-s>", save_shortcut)


root.mainloop()
