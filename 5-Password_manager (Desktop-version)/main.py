from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from tkinter import filedialog
import json
import os 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20,bg="black")
# Icon setup is OS-specific; handled below after computing base_dir
base_dir = os.path.dirname(os.path.abspath(__file__))

#Canvas to display the logo
canvas = Canvas(height=200, width=200,borderwidth=10,bg='black') 
if os.name == 'nt':
    # On Windows, use .ico with iconbitmap
    try:
        window.iconbitmap(os.path.join(base_dir, 'Photos', 'security.ico'))
    except Exception:
        pass
else:
    # On Linux/macOS, use a PNG with iconphoto
    try:
        icon_png_path = os.path.join(base_dir, 'Photos', 'security.png')
        icon_image = PhotoImage(file=icon_png_path)
        window.iconphoto(True, icon_image)
        window._icon_ref = icon_image  # keep a reference to avoid GC
    except Exception:
        pass
#Display The Logo in The Canvas 
file_name = os.path.join(base_dir,'Photos','security.png')
logo_img = PhotoImage(file=file_name)
canvas.create_image(110, 110, image=logo_img)
canvas.grid(row=0, column=1,pady=40)

#Labels
website_label = Label(text="Website:",fg="#E2DCC8",bg="black")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:",fg="#E2DCC8",bg="black")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:",fg="#E2DCC8",bg="black")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=24)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14,fg="#0F3D3E",borderwidth=0,bg="white" ,command=find_password)
search_button.grid(row=1, column=2,pady=5)

#Generate Password Button
generate_password_button = Button(text="Generate Password",fg="#0F3D3E",borderwidth=0, bg="white",command=generate_password)
generate_password_button.grid(row=3, column=2,pady=5)
add_button = Button(text="Add", width=25,fg="#0F3D3E",borderwidth=0, bg="white",command=save)
add_button.grid(row=4, column=1, columnspan=1,pady=10)


window.mainloop()

