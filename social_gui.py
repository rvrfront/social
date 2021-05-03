import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as sq3


def updateUser(id, name, age, gender, nationality, nickname, password, password2):
    if password == password2:
        try:
            connection = sq3.connect("social.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET name=? WHERE id=?",(name, id))
            cursor.execute("UPDATE users SET age=? WHERE id=?", (age, id))
            cursor.execute("UPDATE users SET gender=? WHERE id=?", (gender, id))
            cursor.execute("UPDATE users SET nationality=? WHERE id=?", (nationality, id))
            cursor.execute("UPDATE users SET nick=? WHERE id=?", (nickname, id))
            cursor.execute("UPDATE users SET password=? WHERE id=?", (password, id))
            connection.commit()
            connection.close()
            messagebox.showinfo(title="User updated", message=f"user: {id} updated successfully")
        except:
            messagebox.showerror(title="Error...", message="There was an error...")
    else:
        messagebox.showwarning(title="Passwords...", message="Passwords are not the same value...")

def editProfileAction(id, nick, name):
    countries = ["Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus", "Czech Republic", "Denmark",
                 "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
                 "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
                 "Spain", "Sweden"]
    gender = tk.IntVar()
    editProfile = tk.Toplevel(window)
    editProfile.geometry("250x650")
    nameLabel = tk.Label(editProfile, text="Please, insert your new name: ")
    nameLabel.place(x=10, y=10, relwidth=0.8, relheight=0.08)
    nameEntry = tk.Entry(editProfile)
    nameEntry.place(x=10, y=40, relwidth=0.8, relheight=0.08)
    ageLabel = tk.Label(editProfile, text="Please, insert your new age: ")
    ageLabel.place(x=10, y=80, relwidth=0.8, relheight=0.08)
    ageEntry = tk.Entry(editProfile)
    ageEntry.place(x=10, y=110, relwidth=0.8, relheight=0.08)
    genderLabel = tk.Label(editProfile, text="Please, select your gender: ")
    genderLabel.place(x=10, y=150, relwidth=0.8, relheight=0.08)
    tk.Radiobutton(editProfile, text="Mujer", variable=gender, value=1).place(x=10, y=180, relwidth=0.25, relheight=0.08)
    tk.Radiobutton(editProfile, text="Hombre", variable=gender, value=2).place(x=120, y=180, relwidth=0.25, relheight=0.08)
    nationalityLabel = tk.Label(editProfile, text="Please, select your country")
    nationalityLabel.place(x=10, y=220, relwidth=0.8, relheight=0.08)
    nationality = ttk.Combobox(editProfile, state="readonly")
    nationality.place(x=10, y=250, relwidth=0.8, relheight=0.1)
    nationality["values"] = countries
    nickLabel = tk.Label(editProfile, text="Please, insert your new nickname: ")
    nickLabel.place(x=10, y= 290, relwidth=0.8, relheight=0.08)
    nickEntry = tk.Entry(editProfile)
    nickEntry.place(x=10, y=330, relwidth=0.8, relheight=0.08)
    passwordLabel = tk.Label(editProfile, text="Please, entry your new password: ")
    passwordLabel.place(x=10, y= 360, relwidth=0.8, relheight=0.08)
    passwordEntry = tk.Entry(editProfile, show="*")
    passwordEntry.place(x=10, y=400, relwidth=0.8, relheight=0.08)
    passwordLabel2 = tk.Label(editProfile, text="Please, confirm your password: ")
    passwordLabel2.place(x = 10, y=440, relwidth=0.8, relheight=0.08)
    passwordEntry2 = tk.Entry(editProfile, show="*")
    passwordEntry2.place(x=10, y=470, relwidth=0.8, relheight=0.08)
    buttonToSave = tk.Button(editProfile, text="update user", command=lambda: updateUser(id, nameEntry.get(), ageEntry.get(), gender.get(), nationality.get(), nickEntry.get(), passwordEntry.get(), passwordEntry2.get()))
    buttonToSave.place(x=10, y=510, relwidth=0.8, relheight=0.08)


def showUserAction(id, nick, password):
    userProfile = tk.Toplevel(window)
    userProfile.geometry("500x350")
    createPostFrame = tk.Frame(userProfile)
    createPostFrame.pack()
    createPostFrame.place(x=25, y=25, relwidth=0.25, height= 35)
    createPostButton = tk.Button(createPostFrame, text="create a new post", command=lambda: print("This is a mock action!"))
    createPostButton.pack()
    editProfileFrame = tk.Frame(userProfile)
    editProfileFrame.place(x=190, y=25, relwidth=0.25, height=35)
    editProfileButton = tk.Button(editProfileFrame, text="edit profile", command=lambda: editProfileAction(id, nick, password))
    editProfileButton.pack()


def signInUser(location, name, password):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)
        nick = False
        logged = False
        for user in users:
            if user[5] == name and user[6] == password:
                messagebox.showinfo(title="signed in...", message=f"User: {name} has been signed id properly!")
                nick = True
                logged = True
                showUserAction(user[0], user[5], user[6])
                break
            elif user[5] == name and user[6] != password:
                messagebox.showwarning(title="Password...", message="wrong password")
                nick = True
                break
            elif user[5] != name and user[6] == password:
                logged = True
                messagebox.showinfo(title="nick...", message="wrong nickname")
                break
        if not logged and not nick:
            messagebox.showerror(title="Error...", message="There is not any user with this nickname")
        location.destroy()
    except:
        print("There was an error!!")

def registerUser(location, name, age, gender, nationality, nick, password, password2):
    if password == password2:
        try:
            connection = sq3.connect("social.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users VALUES (null,?,?,?,?,?,?)", (name, age, gender, nationality, nick, password))
            connection.commit()
            connection.close()
            location.destroy()
            print("You have just registered a new user!")
            messagebox.showinfo(title="New user registered", message=f"You have just registered {name} user")
        except:
            print("There was a problem...")
    else:
        messagebox.showwarning(title="Error", message="Passwords must be the same")

def registerAction(location):
    countries = ["Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus", "Czech Republic", "Denmark",
                 "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
                 "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
                 "Spain", "Sweden"]
    gender = tk.IntVar()
    register = tk.Toplevel(location)
    nameFrame = tk.Frame(register)
    nameFrame.pack(side="top")
    nameLabel = tk.Label(nameFrame, text="Please insert your name")
    nameLabel.pack(side="top")
    nameEntry = tk.Entry(nameFrame)
    nameEntry.pack(side="top")
    ageFrame = tk.Frame(register)
    ageFrame.pack(side="top")
    ageLabel = tk.Label(ageFrame, text="Please, insert your age")
    ageLabel.pack(side="top")
    ageEntry = tk.Entry(ageFrame)
    ageEntry.pack(side="top")
    nationalityFrame = tk.Frame(register)
    nationalityLabel = tk.Label(nationalityFrame, text="Please, select your country")
    nationalityLabel.pack(side="top")
    nationalityFrame.pack(side="top")
    nationality = ttk.Combobox(nationalityFrame, state="readonly")
    nationality.pack(side="top")
    nationality["values"] = countries
    genderFrame = tk.Frame(register)
    genderFrame.pack(side="top")
    tk.Radiobutton(genderFrame, text="Mujer", variable=gender, value=1).pack()
    tk.Radiobutton(genderFrame, text="Hombre", variable=gender, value=2).pack()
    nickFrame = tk.Frame(register)
    nickFrame.pack(side="top")
    nickLabel = tk.Label(nickFrame, text="Please, insert a nickname: ")
    nickLabel.pack(side="top")
    nickEntry = tk.Entry(nickFrame)
    nickEntry.pack(side="top")
    passwordFrame = tk.Frame(register)
    passwordFrame.pack(side="top")
    passwordLabel = tk.Label(passwordFrame, text="Please, insert your passwprd")
    passwordLabel.pack(side="top")
    passwordEntry = tk.Entry(passwordFrame, show="*")
    passwordEntry.pack(side="top")
    passwordLabel2 = tk.Label(passwordFrame, text="Please, confirm password: ")
    passwordLabel2.pack(side="top")
    passwordEntry2 = tk.Entry(passwordFrame, show="*")
    passwordEntry2.pack(side="top")
    buttonFrame = tk.Frame(register)
    buttonFrame.pack(side="top")
    registerButton = tk.Button(buttonFrame, text="register", command=lambda: registerUser(register, nameEntry.get(),ageEntry.get(), gender.get(),nationality.get(), nickEntry.get(), passwordEntry.get(), passwordEntry2.get()))
    registerButton.pack(side="top")

def signInAction():
    signIn = tk.Toplevel(window)
    nameFrame = tk.Frame(signIn)
    nameFrame.pack(side="top")
    nameLabel = tk.Label(nameFrame, text="Please, insert your name: ")
    nameLabel.pack(side="top")
    nameEntry = tk.Entry(nameFrame)
    nameEntry.pack(side="top")
    passwordFrame = tk.Frame(signIn)
    passwordFrame.pack(side="top")
    passwordLabel = tk.Label(passwordFrame, text="Please, insert your password: ")
    passwordLabel.pack()
    passwordEntry = tk.Entry(passwordFrame, show="*")
    passwordEntry.pack()
    buttonFrame = tk.Frame(signIn)
    buttonFrame.pack(side="top")
    buttonSignIn = tk.Button(buttonFrame, text="sign in", command=lambda: signInUser(signIn, nameEntry.get(), passwordEntry.get()))
    buttonSignIn.pack(side="top")


window = tk.Tk()
window.geometry("350x150")
window.title("Python social network")
registerButton = tk.Button(window, text='register', command=lambda: registerAction(window))
registerButton.pack(side="top")
registerButton.config(bg="grey", relief="sunken", padx=15, pady=15, width=15)
signinButton = tk.Button(window, text='sign in', command=signInAction)
signinButton.pack(side="top")
signinButton.config(bg="grey", relief="sunken", padx=15, pady=15, width=15)
print(window.configure().keys())
window.mainloop()