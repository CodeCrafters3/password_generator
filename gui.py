from tkinter import *

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

generate_password_button = Button(root, text="Generate password")
generate_password_button.config(
    font= ("Courier New", 15),
    padx=5,
    pady=7,
    bg="grey",
    fg="black",
    activebackground="#6f1919"
)
generate_password_button.place(relx=.5, rely=.5, anchor="center")

label_generated_password = Label(
    root,
    text="Your password:",
    font=("Courier New", 10),
    padx=4,
    pady=4,
    bg=('#282828'),
    fg="white"
)
label_generated_password.place(relx=0.5, y=50, anchor="center")


entry_generated_password = Entry(
    root,
    bd=3,
    font=("Courier New", 10),
    bg="#444444",
    fg="#bd3131",
    width=70
)
entry_generated_password.place(relx=0.5, y=80, anchor="center")
 
root.mainloop()