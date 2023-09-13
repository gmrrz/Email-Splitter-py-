import tkinter as tk

root = tk.Tk()

# Making the window
root.title("Email Splitter")

root.geometry("500x115")

root.resizable(False,False)

root.configure(bg = "white")

# Splitting the name from the domain
def splitter():
    split.delete(0, tk.END)
    x = emailEntry.get()
    if '@' in x:
        res = x.replace('@',' and ')
        print(split.insert(0, f"Your username is {res} is the domain"))
    else:
        print(split.insert(0, "This isnt an email"))


# Adding & resizing the widgets
Font_tuple = ('Consolas',10)

email = tk.Label(root, text = "Enter your email:",bg = "white", fg = "black", font = Font_tuple).pack()

emailEntry = tk.Entry(root, font = (Font_tuple,8),fg = "black",borderwidth=2,justify='center')

splitButton = tk.Button(root, text = "Split" ,fg = "black", font = Font_tuple , command = splitter)

split = tk.Entry(root, font = (Font_tuple,8),borderwidth=0,fg = "red",justify='center')

emailEntry.place(relx=0.5, rely=0.3,width = 150, anchor='center')
splitButton.place(relx=0.5, rely=0.6, anchor='center')
split.place(relx=0.5, rely=0.8,width = 375, height = 15,anchor='center')

# Looping the app
root.mainloop()
