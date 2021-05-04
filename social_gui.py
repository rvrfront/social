import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as sq3
from social_sql import updateUserDB, searchAnUser, CreateAPost, getPosts, getOnePost, delPost

def deletePost(location, id):
    decision = messagebox.askquestion(title="Delete post...", message=f"Are you sure to del post {id}", icon="warning")
    if decision == "yes":
        delPost(id)
        messagebox.showwarning(title="Post deleted...", message=f"You have just deleted post: {id}")
        location.destroy()

def showOnePost(id):
    post = getOnePost(id)
    title = post[0][1]
    author = post[0][2]
    message = f"Message: {post[0][1]}"
    print("Post: ", post)
    postWindow = tk.Toplevel(window)
    postWindow.geometry("700x700")
    postTitle = tk.Label(postWindow, text=f"Title: {title}")
    postTitle.place(x=10, y=10, relwidth=0.7, relheight=0.1)
    postMessage = tk.Text(postWindow)
    postMessage.insert(tk.INSERT, message)
    postMessage.insert(tk.END, f"\ndeveloped with python & tkinter")
    postMessage.config(state=tk.DISABLED)
    postMessage.place(x=10, y=50, relwidth=0.7, relheight=0.1)
    postAuthor = tk.Label(postWindow, text=f"Author id: {author}")
    postAuthor.place(x=10, y=130, relwidth=0.4, relheight=0.05)
    buttonToDelete = tk.Button(postWindow, text="delete", command=lambda: deletePost(postWindow,id))
    buttonToDelete.place(x=10, y=170, relwidth=0.25, relheight=0.05)
    buttonToEdit = tk.Button(postWindow, text="edit post", command=lambda: print("Edit post..."))
    buttonToEdit.place(x=250, y=170, relwidth=0.25, relheight=0.05)
    buttonLikes = tk.Button(postWindow, text="likes!", command=lambda: print("Likes..."))
    buttonLikes.place(x=10, y=240, relwidth=0.7, relheight=0.05)



def showPosts(location):
    posts = getPosts()
    print("Posts: ", posts)
    incx = 125
    incy = 85
    for post in posts:
        id= post[0]
        title = post[1]
        print("id from showPosts:", id)
        print("title from showPosts: ", title)
        tk.Button(location, text=title, command=lambda: showOnePost(id)).place(x=incx, y=incy, relwidth=0.5, relheight=0.1)

def createPostAction(id, nickname, password):
    try:
        getUser = searchAnUser(id)
        print(f"User: {getUser} || type: {type(getUser)}")
    except:
        messagebox.showwarning(title="Warning...", message="There was a problem...")

    post = tk.Toplevel(window)
    post.geometry("500x500")
    postTitleLabel = tk.Label(post, text="Please, insert the tittle: ")
    postTitleLabel.place(x=70, y=25, relwidth=0.7, relheight=0.1)
    postTitleEntry = tk.Entry(post)
    postTitleEntry.place(x=70, y=55, relwidth=0.7, relheight=0.1)
    postLabelMessage = tk.Label(post, text="Please, insert the message: ")
    postLabelMessage.place(x=70, y=95, relwidth=0.7, relheight=0.1)
    postEntryMessage = tk.Entry(post)
    postEntryMessage.place(x=70, y=125, relwidth=0.7, relheight=0.4)
    postAuthorLabel = tk.Label(post, text=getUser[0])
    postAuthorLabel.place(x=70, y=320, relwidth=0.7, relheight=0.1)
    postButton = tk.Button(post, text="submit", command=lambda: CreateAPost(post, id, postTitleEntry.get(),
                                                                            postEntryMessage.get()))
    postButton.place(x=70, y=370, relwidth=0.7, relheight=0.1)

def updateUser(location, id, name, age, gender, nationality, nickname, password, password2):
    if password == password2:
        try:
            updateUserDB(id, name, age, gender, nationality, nickname, password)
            messagebox.showinfo(title="User updated", message=f"user: {id} updated successfully")
        except:
            messagebox.showerror(title="Error...", message="There was an error...")
    else:
        messagebox.showwarning(title="Passwords...", message="Passwords are not the same value...")
    location.destroy()

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
    buttonToSave = tk.Button(editProfile, text="update user", command=lambda: updateUser(editProfile, id, nameEntry.get(), ageEntry.get(), gender.get(), nationality.get(), nickEntry.get(), passwordEntry.get(), passwordEntry2.get()))
    buttonToSave.place(x=10, y=510, relwidth=0.8, relheight=0.08)



def showUserAction(id, nick, password):
    userProfile = tk.Toplevel(window)
    userProfile.geometry("500x350")
    createPostFrame = tk.Frame(userProfile)
    createPostFrame.pack()
    createPostFrame.place(x=25, y=25, relwidth=0.25, height= 35)
    createPostButton = tk.Button(createPostFrame, text="create a new post", command=lambda: createPostAction(id, nick, password))
    createPostButton.pack()
    editProfileFrame = tk.Frame(userProfile)
    editProfileFrame.place(x=190, y=25, relwidth=0.25, height=35)
    editProfileButton = tk.Button(editProfileFrame, text="edit profile", command=lambda: editProfileAction(id, nick, password))
    editProfileButton.pack()
    showPosts(userProfile)


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
    passwordLabel = tk.Label(passwordFrame, text="Please, insert your password")
    passwordLabel.pack(side="top")
    passwordEntry = tk.Entry(passwordFrame, show="*")
    passwordEntry.pack(side="top")
    passwordLabel2 = tk.Label(passwordFrame, text="Please, confirm password: ")
    passwordLabel2.pack(side="top")
    passwordEntry2 = tk.Entry(passwordFrame, show="*")
    passwordEntry2.pack(side="top")
    buttonFrame = tk.Frame(register)
    buttonFrame.pack(side="top")
    if gender.get() == 1:
        gender.set("Mujer")
    elif gender.get() == 2:
        gender.set("Hombre")
    print("Gender: ", gender.get())
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