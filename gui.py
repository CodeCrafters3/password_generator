from tkinter import *
import tkinter as tk

root = Tk()

root.title("Password Generator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600
window_height = 400
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='klodka1.png'))
root.config(background="#282828")

#Length
label_length_password = Label(
    root,
    text="Choose length of password:",
    font=("Courier New", 8),
    padx=4,
    pady=4,
    bg='#282828',
    fg="white"
)
label_length_password.place(relx=0.5, y=20, anchor="center")

entry_length_password = Entry(
    root,
    bd=3,
    font=("Courier New", 10),
    bg="#444444",
    fg="#bd3131",
    width=5
)
entry_length_password.place(relx=0.5, y=45, anchor="center")

#Button
generate_password_button = Button(root, text="Generate password")
generate_password_button.config(
    font=("Courier New", 15),
    padx=5,
    pady=7,
    bg="grey",
    fg="black",
    activebackground="#6f1919"
)
generate_password_button.place(relx=0.5, y=150, anchor="center")

#Generated pass
label_generated_password = Label(
    root,
    text="Your password:",
    font=("Courier New", 12),
    padx=4,
    pady=4,
    bg=('#282828'),
    fg="white"
)
label_generated_password.place(relx=0.5, y=250, anchor="center")

entry_generated_password = Entry(
    root,
    bd=3,
    font=("Courier New", 10),
    bg="#444444",
    fg="#bd3131",
    width=70
)
entry_generated_password.place(relx=0.5, y=280, anchor="center")




root.mainloop()