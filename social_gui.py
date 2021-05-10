import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#import sqlite3 as sq3
from social_sql import updateUserDB, searchAnUser, createAPost, getPosts, getOnePost, delPost, updatePost, \
     getUserLoggedIn, getAllUsers, registerNewUser

#Función usada para editar un post concreto
def editPostAction(location, id):
    #location ---> el nombre de la interfaz desde donde se llama a esta función
    #id que identifica al post en concreto de la tabla posts de la base de datos
    #Se va a usar el obejo loggedUser, que ya se ha definido previamente como global
    global loggedUser
    #Se crea una nueva ventana --> editPost
    editPost = tk.Toplevel(window)
    #Se le asigna un tamaño de 500x500 px
    editPost.geometry("500x500")
    #Se llama a la función getOnePost, que devuelve una lista de tuplas
    #con el post que tiene un id determinado
    post = getOnePost(id)
    #Del post que se obtiene de la base de datos se obtiene el autor del mismo
    userId = post[0][2]
    print("userId from editPostAction: ", userId)
    print("loggedUser from editPostAction: ", loggedUser[0][0])
    #En caso de que el autor del post sea el mismo usuario que está logueado
    #tiene permiso para editar el post --> se muestra la nueva interfaz
    if userId == loggedUser[0][0]:
        #Se define las variables de control postTitle y postMessage
        postTitle = tk.StringVar()
        postMessage = tk.StringVar()
        print("Post from editPostAction: ", post)
        print("Elementos del post editPostAction: ", post[0][0])
        print("Elementos del post editPostAction: ", post[0][1])
        #Se crea un label en la interfaz que muestra --> Title:
        postTitleLabel = tk.Label(editPost, text="Title: ")
        postTitleLabel.place(x=10, y=10, relwidth=0.15, relheight=0.1)
        #Se crea un entry en la interfaz asoaciado a la variable de control ---> postTitle
        postTitleEntry = tk.Entry(editPost, textvariable=postTitle)
        #Se setea el entry anterior con el valor en post[0][0] ---> el título del post que tiene un determinado id
        postTitle.set(post[0][0])
        postTitleEntry.place(x=70, y=10, relwidth=0.5, relheight=0.1)
        #Se crea un label en la interfaz que muestra --> Message:
        postMessageLabel = tk.Label(editPost, text="Message: ")
        postMessageLabel.place(x=10, y= 60, relwidth=0.15, relheight=0.1)
        #Se crea un entry en la interfaz asociado a la variable de control ---> postMessage
        #postMessageEntry = tk.Entry(editPost, textvariable=postMessage)

        ########################################################################
        postMessageEntry = tk.Text(editPost)
        postMessageEntry.insert(tk.INSERT, post[0][1])
        postMessageEntry.insert(tk.END, f"----end of post-----")
        postMessageEntry.place(x=70, y=60, relwidth=0.7, relheight=0.4)

        ########################################################################
        #Se setea el entry anterior con el valor en post[0][1]   ---> el cuerpo del mensaje del post con
        #determinado id
        #postMessage.set(post[0][1])
        #postMessageEntry.place(x=70, y=60, relwidth=0.5, relheight=0.3)
        #Se crea un botón en la interfaz que llama a la función updatePost ---> para que actualice el post en la base de datos
        postUpdateButton = tk.Button(editPost, text="update", command=lambda h=post: updatePost(showAllPosts, editPost, location, id, postTitleEntry.get(), postMessageEntry.get("1.0", "end-1c")))
        postUpdateButton.place(x=80, y=280, relwidth=0.25, relheight=0.1)
    else:
        #En caso de que el usuario logueado no sea el autor del post no se le permite modificarlo
        #Se muestra un mensaje en pantalla preguntando por una respuesta ---> en cualquier caso la
        #acción es la misma, se usa messagebox.askquestion a modo de práctica
        advise = messagebox.askquestion(title="Error...", message="You can not edit that post, it is not of yours...")
        if advise == "yes":
            #Se usa un método del ciclo de vida de los widgets de tkinter para cerrar
            #La interfaz que se le pasa como parámetro --> location, así como la interfaz que se
            #crea en esta función editPost
            editPost.destroy()
            location.destroy()
        else:
            editPost.destroy()
            location.destroy()

#Función que se usa para eliminar un post con un determinado id de la tabla
# de posts de la base de datos
def deletePost(location, id):
    #Se usa el objeto loggedUser definido ya previamente como global
    global loggedUser
    #Se llama a la función getOnePost para obtener desde la tabla posts de la
    #base de datos el post con el id en concreto
    selectedPost = getOnePost(id)
    #El valor del autor del post se define como ---> user_id
    user_id = selectedPost[0][2]
    #Si el usuario autor del post es el mismo que el usuario que
    #que está logueado se le permite eliminar el post
    if user_id == loggedUser[0][0]:
        #Antes de eliminar el post se le pregunta al usuario si está seguro de eliminar el post
        decision = messagebox.askquestion(title="Delete post...", message=f"Are you sure to del post {id}", icon="warning")
        #En caso de que responda si, se elimina el post y se destruyen las interfaces location y delPost
        if decision == "yes":
            delPost(id)
            messagebox.showwarning(title="Post deleted...", message=f"You have just deleted post: {id}")
            location.destroy()
            showAllPosts.destroy()
        else:
            #En caso de que el usuario responda NO, se destruyen las interfaces location y delPost igualmente
            location.destroy()
            showAllPosts.destroy()
    else:
        messagebox.showwarning(title="Error...", message="You are not the owner of this post!")
    location.destroy()
    showAllPosts.destroy()

#Función que se usa para mostrar una plantilla para ver un post en concreto
#Se puede ver el post en cuestión , así como editarla a posteriori o eliminarla
def showOnePost(id):
    #Se llama a la función getOnePost para obtener el post con su id de
    #la tabla posts de la base de datos
    post = getOnePost(id)
    #Se identifica en title el título del post
    title = post[0][0]
    #Se identifica en author al autor del post
    author = post[0][2]
    #Se identifica en message como el mensaje del post
    message = f"Message: {post[0][1]}"
    print("Post: ", post)
    #Se crea una nueva interfaz ---> postWindow cuyo padre es Window definido como global
    postWindow = tk.Toplevel(window)
    #La interfaz postWindow tendrá unas dimensiones de 700x700 px
    postWindow.geometry("700x700")
    #Se crea un label en postWindow ---> Title:
    postTitle = tk.Label(postWindow, text=f"Title: {title}")
    postTitle.place(x=10, y=10, relwidth=0.7, relheight=0.1)
    #Se crea un campo de texto postMessage con el cuerpo del mensaje
    #del post
    postMessage = tk.Text(postWindow)
    postMessage.insert(tk.INSERT, message)
    #Se le añade la firma como una nueva linea al final del mensaje:
    #developed with python & tkinter
    postMessage.insert(tk.END, f"\ndeveloped with python & tkinter")
    #Se le espcifica state = disabled para que el cuerpo del mensaje
    #no pueda ser editado
    postMessage.config(state=tk.DISABLED)
    postMessage.place(x=10, y=50, relwidth=0.7, relheight=0.1)
    #Se crea un label ---> Author id: con el nombre del autor del post
    postAuthor = tk.Label(postWindow, text=f"Author id: {author}")
    postAuthor.place(x=10, y=130, relwidth=0.4, relheight=0.05)
    #Se define un botón para borrar el post que llama a la función deletePost
    buttonToDelete = tk.Button(postWindow, text="delete", command=lambda f=id: deletePost(postWindow,f))
    buttonToDelete.place(x=10, y=170, relwidth=0.25, relheight=0.05)
    #Se define un botón para editar un determinado post que llama a la función editPostAction
    buttonToEdit = tk.Button(postWindow, text="edit post", command=lambda g=id: editPostAction(postWindow,g))
    buttonToEdit.place(x=250, y=170, relwidth=0.25, relheight=0.05)
    buttonLikes = tk.Button(postWindow, text="likes!", command=lambda: print("Likes..."))
    buttonLikes.place(x=10, y=240, relwidth=0.7, relheight=0.05)


#Función que muestra todos los posts de la tabla posts de la base de datos
def showPosts():
    #Se llama a la función getPosts para obtener todos los posts de la tabla posts
    #de la base de datos
    posts = getPosts()
    print("Posts: ", posts)
    print("Length of Posts: ", len(posts))
    #Se usa la interfaz showAllPosts definida previamente como global
    global showAllPosts
    #Se crea una nueva interfaz showAllPosts cuyo padre es Window, definido previamente3
    #como global
    showAllPosts = tk.Toplevel(window)
    scrollbar = tk.Scrollbar(showAllPosts)
    showAllPostsCanvas = tk.Canvas(showAllPosts, yscrollcommand=scrollbar.set)
    scrollbar.config(command=showAllPostsCanvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    showAllPostsCanvas.place(x=10, y=10, relwidth=0.75, relheight=0.9)
    #Se le asigna unas dimensiones de 500x600 px
    showAllPosts.geometry("500x600")
    #Se establecen las posiciones iniciales de cada uno de los posts
    # que se mostrarán a continuación
    incx = 25
    incy = 25
    #Se inicializa el obejeto postList como lista, para poder usar posteriormente
    #los métodos propios de listas
    postsList = list()
    #Si se obtiene como llamada a la base de datos como mínimo un post
    if len(posts) >= 1:
        #Para cada post que haya en posts
        for post in posts:
            #Se identifica el id del post
            id = post[0]
            #se identifica el titulo del post
            title = post[1]
            #Y se identifica el autor del post
            user_id = post[3]
            print("id from showPosts:", id)
            print("title from showPosts: ", title)
            #A la lista vacia que se tenia en postsList se le va añadiendo un botón por cada post
            #En ese boton se le especifica como texto a mostrar Titulo y usuario del pos
            #En command se le debe pasar una lambda function con un parámetro c que se va
            #actualizando para cada post de la lista de posts que se obtenga de la base de datos
            #para que al hacer click en cada botón se desencadene la acción de abrir un determinado post
            postsList.append(tk.Button(showAllPostsCanvas, text=f"title: {title} || user: {user_id}", command=lambda c=id: showOnePost(c)).place(x=incx, y=incy, relwidth=0.9, relheight=0.1))
            #El valor de incy se incrementa en 85px para que no se solapen los posts mostrados
            incy += 85
    else:
        #En caso de que haya menos de un post se alerta con un mensaje que no se puede mostrar los posts
        decision = messagebox.askquestion(title="No posts...", message="Excuse me, but There is no any post to show!", icon="warning")
        #Se hace uso de message.askquestion con objeto no de no hacer siempre uso de showmessage.showinfo
        if decision == "yes":
            showAllPosts.destroy()
        else:
            showAllPosts.destroy()

#Se define la función para crear un post
def createPostAction(id):
    #Se tiene al asuario logueado en id
    #Se tiene un control de excepciones
    try:
        #Se intenta obtener los datos del usuario desde la tabla users de la
        #base de datos con un determinado id  ---> getUser
        getUser = searchAnUser(id)
        print(f"User: {getUser} || type: {type(getUser)}")
    #En caso de que no encuentre al usuario con un id en concreto muestra un
    #mensaje descriptivo en pantalla
    except:
        messagebox.showwarning(title="Warning...", message=f"I could not find id: {id}")
    #Se crea una nueva interfaz post en el padre Window que se ha definido previamente
    #como global
    post = tk.Toplevel(window)
    #Se le asigna a post unas dimensiones de 500x500 px
    post.geometry("500x500")
    #Se crea un label ----> Please, insert the title:
    postTitleLabel = tk.Label(post, text="Please, insert the tittle: ")
    postTitleLabel.place(x=70, y=25, relwidth=0.7, relheight=0.1)
    #Se define un entry donde se guarda el titulo del post
    postTitleEntry = tk.Entry(post)
    postTitleEntry.place(x=70, y=55, relwidth=0.7, relheight=0.1)
    #Se define un label ---> Please, insert the message
    postLabelMessage = tk.Label(post, text="Please, insert the message: ")
    postLabelMessage.place(x=70, y=115, relwidth=0.7, relheight=0.1)
    #Se define un entry donde se guarda el cuerpo del mensaje del post
    #postEntryMessage = tk.Entry(post)
    #postEntryMessage.place(x=70, y=125, relwidth=0.7, relheight=0.4)

    message = "Please, delete this text and type something of yours!"
    postEntryMessage = tk.Text(post)
    postEntryMessage.insert(tk.INSERT, message)
    postEntryMessage.insert(tk.END, f"----end of post-----")
    postEntryMessage.place(x=70, y=145, relwidth=0.7, relheight=0.4)

    #Se crea un label con un texto ya especificado como el autor que es el usuario logueado
    postAuthorLabel = tk.Label(post, text=getUser[0])
    postAuthorLabel.place(x=70, y=365, relwidth=0.7, relheight=0.1)
    #Se define un botón con el texto --> submit y que llama a la función
    #createAPost para almacenar el post en la tabla posts de la base de datos
    postButton = tk.Button(post, text="submit", command=lambda: createAPost(post, id, postTitleEntry.get(),
                                                                            postEntryMessage.get("1.0", "end-1c")))
    postButton.place(x=70, y=415, relwidth=0.7, relheight=0.1)

#Función que se usa para editar los datos de un usuario ya existente en la tabla usaers de la
#base de datos
def updateUser(location, id, name, age, gender, nationality, nickname, password, password2):
    #Si las dos nuevas contraseñas son iguales ...
    if password == password2:
        try:
            #Se llama a la función updateUserDB con los cmapos necesarioa para actualizar
            #los datos de ese usuario en la tabla users de la base de datos
            updateUserDB(id, name, age, gender, nationality, nickname, password)
            messagebox.showinfo(title="User updated", message=f"user: {id} updated successfully")
        #En caso que la llamada a la función updateUserDB de algún error se captura y se
        #muestra un mensaje descriptivo
        except:
            messagebox.showerror(title="Error...", message="There was an error...")
    else:
        #En caso de que las dos nuevas contraseñas no sean iguales se muestra un mensaje
        #descriptivo
        messagebox.showwarning(title="Passwords...", message="Passwords are not the same value...")
    #Cuando se ha terminado de actualizar los datos del usuario en la tabla users de la base
    #de datos se procede a destruir a la interfaz padre que llama a updateUSer
    location.destroy()

#Función que se usa para mostrar la interfaz para crear un usuario
def editProfileAction(id):
    #Se define una lista de paises, en este caso a modo de ejemplo
    #paises de Europa
    countries = ["Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus", "Czech Republic", "Denmark",
                 "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
                 "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
                 "Spain", "Sweden"]
    #Se define el género del nuevo usuario como una variable de control
    gender = tk.IntVar()
    #Se define una nueva interfaz editProfile cuyo padre es Window
    #definida como global previamente
    editProfile = tk.Toplevel(window)
    #LA interfaz editProfile tiene unas dimensiones de 250x650px
    editProfile.geometry("250x650")
    #Se define una label ---> Please, insert your new name:
    nameLabel = tk.Label(editProfile, text="Please, insert your new name: ")
    nameLabel.place(x=10, y=10, relwidth=0.8, relheight=0.08)
    #Se defina un entry para guardar el nombre el usuario
    nameEntry = tk.Entry(editProfile)
    nameEntry.place(x=10, y=50, relwidth=0.8, relheight=0.08)
    #Se define un label ---> Please, insert your new age:
    ageLabel = tk.Label(editProfile, text="Please, insert your new age: ")
    ageLabel.place(x=10, y=90, relwidth=0.8, relheight=0.08)
    #Se define un entry donde se almacena la edad del usuario
    ageEntry = tk.Entry(editProfile)
    ageEntry.place(x=10, y=130, relwidth=0.8, relheight=0.08)
    #Se define un label ---> Please, select your gender:
    genderLabel = tk.Label(editProfile, text="Please, select your gender: ")
    genderLabel.place(x=10, y=170, relwidth=0.8, relheight=0.08)
    #En este caso se usa a modo de ejemplo radiobuttons
    tk.Radiobutton(editProfile, text="Mujer", variable=gender, value=1).place(x=10, y=180, relwidth=0.25, relheight=0.08)
    tk.Radiobutton(editProfile, text="Hombre", variable=gender, value=2).place(x=120, y=180, relwidth=0.25, relheight=0.08)
    #Se define un label ----> Please, select your country
    nationalityLabel = tk.Label(editProfile, text="Please, select your country")
    nationalityLabel.place(x=10, y=240, relwidth=0.8, relheight=0.08)
    #En este caso el pais se selecciona desde una lista desplegable
    #cuyos valores posibles son los definidos previemante en el objeto
    #countries
    nationality = ttk.Combobox(editProfile, state="readonly")
    nationality.place(x=10, y=270, relwidth=0.8, relheight=0.1)
    nationality["values"] = countries
    #Se define un label ----> Please, insert your new nickname
    nickLabel = tk.Label(editProfile, text="Please, insert your new nickname: ")
    nickLabel.place(x=10, y=310, relwidth=0.8, relheight=0.08)
    #Se define un entry para almacenar el valor de nickname
    nickEntry = tk.Entry(editProfile)
    nickEntry.place(x=10, y=350, relwidth=0.8, relheight=0.08)
    #Se define un label ---> Please, entry your new password
    passwordLabel = tk.Label(editProfile, text="Please, entry your new password: ")
    passwordLabel.place(x=10, y=380, relwidth=0.8, relheight=0.08)
    #Se define un entry para almacenar la contraseña
    #Se usa el argumento show="*" para que no muestra la contraseña y la
    #oculte con *****
    passwordEntry = tk.Entry(editProfile, show="*")
    passwordEntry.place(x=10, y=420, relwidth=0.8, relheight=0.08)
    #Se define un label para confirmar contraseña ----> Please, confirm your password
    passwordLabel2 = tk.Label(editProfile, text="Please, confirm your password: ")
    passwordLabel2.place(x = 10, y=460, relwidth=0.8, relheight=0.08)
    #Se define un entry para almacenar el valor de la confirmacion de contraseña
    passwordEntry2 = tk.Entry(editProfile, show="*")
    passwordEntry2.place(x=10, y=490, relwidth=0.8, relheight=0.08)
    #Se define un botón con el texto "update user" y que llama a la función updateUser
    #para actualizar los datos de ese usuario en la tabla users en la base de datos
    buttonToSave = tk.Button(editProfile, text="update user", command=lambda: updateUser(editProfile, id, nameEntry.get(), ageEntry.get(), gender.get(), nationality.get(), nickEntry.get(), passwordEntry.get(), passwordEntry2.get()))
    buttonToSave.place(x=10, y=530, relwidth=0.8, relheight=0.08)


#Función que se usa para mostrar las distintas acciones que tiene un
#usuario
def showUserAction(id, nick, password):
    #Se define una interfaz userProfile cuyo padre es window definido
    #previamente como global
    userProfile = tk.Toplevel(window)
    #editProfile tiene unas dimensiones de 500x350px
    userProfile.geometry("500x350")
    #Se define un frame createPostFrame cuyo padre es userProfile
    createPostFrame = tk.Frame(userProfile)
    createPostFrame.pack()
    createPostFrame.place(x=25, y=25, relwidth=0.25, height= 35)
    #Se define un botoón con el texto create a new post y que llama a la función
    #createPostAction que inicia otra interfaz para crear el post
    createPostButton = tk.Button(createPostFrame, text="create a new post", command=lambda: createPostAction(id))
    createPostButton.pack()
    #Se define un frame editProfileFrame cuyo padre es userProfile
    editProfileFrame = tk.Frame(userProfile)
    editProfileFrame.place(x=190, y=25, relwidth=0.25, height=35)
    #Se define un botón con el texto edit profile y que llama a la función editProfileAction
    #que inicia otra interfaz para editar los datos de perfil de un usuario
    editProfileButton = tk.Button(editProfileFrame, text="edit profile", command=lambda: editProfileAction(id))
    editProfileButton.pack()
    # showPosts(userProfile)
    #Se defina un botón con el texto show posts que llama a la función showPosts
    #que inicia otra interfaz para mostar todos los posts de la tabla posts de la
    #base de datos
    buttonToShowPosts = tk.Button(userProfile, text="show posts", command=lambda: showPosts())
    buttonToShowPosts.place(x=60, y=65, relwidth=0.7, height=35)


#Función para hacer el proceso de logging de un usuario
def signInUser(location, name, password):
    #Se le pasa como parámetro la interfaz padre desde donde se
    #llama a la función, así como el nickname del usuario y
    #la contraseña
    global loggedUser
    #Se hace un control de excepciones,,,
    try:
        #connection = sq3.connect("social.db")
        #cursor = connection.cursor()
        #cursor.execute("SELECT * FROM users")
        #users = cursor.fetchall()
        #Se llama a la función getAllUsers para almacenar en
        #users todos los usuarios de la tabla users de la
        #base de datos
        users = getAllUsers()
        print(users)
        nick = False
        logged = False
        for user in users:
            #Se comprueba si el nickname y contraseña que se pasan como argumento son
            #los correspondientes para ese usuario almacenado en la tabla users de la base
            #de datos
            if user[5] == name and user[6] == password:
                #Si el nickname y contraseña introducidos con los correctos se
                #muestra un mensaje descriptivo y se sale del bucle con "break"
                messagebox.showinfo(title="signed in...", message=f"User: {name} has been signed id properly!")
                #En este caso se actualiza el valor de nick y logged ambos a True
                nick = True
                logged = True
                loggedUser = getUserLoggedIn(name, password)
                print("loggedUser from signInUser: ", loggedUser)
                showUserAction(user[0], user[5], user[6])
                break
            elif user[5] == name and user[6] != password:
                #Si sólo se ha intorducido correctamente el nickname se muestra
                #un mensaje descriptivo y se sale del bucle con "break"
                messagebox.showwarning(title="Password...", message="wrong password")
                #En este caso se actualiza el valor de nick a True
                nick = True
                break
            elif user[5] != name and user[6] == password:
                #En caso de que sólo se haya introducido correctamente la contraseña
                #se muestra un mensaje descriptivo
                logged = True
                #Se actualiza el valor de logged a True
                messagebox.showinfo(title="nick...", message="wrong nickname")
                break
        if not logged and not nick:
            #En caso de que tanto nick como logged sean False se muestra un mensaje descriptivo
            messagebox.showerror(title="Error...", message="There is not any user with this nickname")
        #Y se destruye la interfaz padre que llama a signInUSer
        location.destroy()
    except:
        #En caso de que haya un error en el momento de leer los usuarios de la tabla
        #users de la base de datos se muestra un mensaje descriptivo
        messagebox.showerror(title="Error From signInUser" ,message="From sigInUser: There was an error!!")


#Función para registrar un nuevo usuario en la tabal users de la base de datos
def registerUser(location, name, age, gender, nationality, nick, password, password2):
    #Se le pasa como argumentos todos la información necesaria
    #Si las password y password2 procedentes de registerAction son iguales se
    #procede a registrar al nuevo usuario
    if password == password2:
        try:
            #connection = sq3.connect("social.db")
            #cursor = connection.cursor()
            #cursor.execute("INSERT INTO users VALUES (null,?,?,?,?,?,?)", (name, age, gender, nationality, nick, password))
            #connection.commit()
            #connection.close()
            registerNewUser(name, age, gender, nationality, nick, password)
            #Y se procede a destruir la interfaz padre que ha llamado a registerUser
            location.destroy()
            #Se muestra un mensaje descriptivo en consola
            print("You have just registered a new user!")
            #Se muestra un mensaje descriptivo en pantalla
            messagebox.showinfo(title="New user registered", message=f"You have just registered {name} user")
        except:
            #En caso de error a la hora de axctualizar la tabla users de la base de
            #datos se muestra un mensaje descriptivo
            messagebox.showerror(title="Error From registerUserThere was a problem...", message="I could not register this user")
    else:
        #En caso de que la contraseña y la confirmación de contraseña no sean iguales
        #se muestra un mensaje descriptivo
        messagebox.showwarning(title="Error From registerUser", message="Passwords must be the same")


#Se define la función registerAction que crea la interfaz para registrar un nuevo usuario
def registerAction(location):
    #Se le pasa como argumento la interfaz padre que llama a esta función

    #Se define una lista de paises, en este caso paises de Europa
    countries = ["Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus", "Czech Republic", "Denmark",
                 "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
                 "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
                 "Spain", "Sweden"]
    #Se almacena el género del nuevo usuario como variable de control
    #en gender
    gender = tk.IntVar()
    #Se define una nuvea interfaz register cuyo padre es location
    register = tk.Toplevel(location)
    #Se define un frame nameFrame para el label y entry de name
    nameFrame = tk.Frame(register)
    nameFrame.pack(side="top")
    #En nameFrame se crea un label ---> Please, insert your name
    nameLabel = tk.Label(nameFrame, text="Please insert your name")
    nameLabel.pack(side="top")
    #En nameFrame se define un entry para almacenar el nombre del nuevo usuario
    nameEntry = tk.Entry(nameFrame)
    nameEntry.pack(side="top")
    #Se define un frame ageFrame, para el label y entry de age
    ageFrame = tk.Frame(register)
    ageFrame.pack(side="top")
    #Se define en ageFrame un label ---> Please, inset your age
    ageLabel = tk.Label(ageFrame, text="Please, insert your age")
    ageLabel.pack(side="top")
    #Se define un entry en ageFrame para almacenar la edad del nuevo usuario
    ageEntry = tk.Entry(ageFrame)
    ageEntry.pack(side="top")
    #SE define un nuevo frame nationalityFrama para el label y entry de nationality
    nationalityFrame = tk.Frame(register)
    #Se define en nationalityFrame un label ---> Please, select your country
    nationalityLabel = tk.Label(nationalityFrame, text="Please, select your country")
    nationalityLabel.pack(side="top")
    nationalityFrame.pack(side="top")
    #Se define un combobox para seleccionar el pais del nuevo usuario
    nationality = ttk.Combobox(nationalityFrame, state="readonly")
    nationality.pack(side="top")
    #Los posibles paises mostrados son los de la lista countries
    nationality["values"] = countries
    genderFrame = tk.Frame(register)
    #Se define un frame genderFrame para los radiobuttons para
    #almacenar el género del nuevo usuario
    genderFrame.pack(side="top")
    tk.Radiobutton(genderFrame, text="Mujer", variable=gender, value=1).pack()
    tk.Radiobutton(genderFrame, text="Hombre", variable=gender, value=2).pack()
    #Se define un frame nickFrama para el label y entry del nickname del nuevo usuario
    nickFrame = tk.Frame(register)
    nickFrame.pack(side="top")
    #Se define en nickFrame un label ---> Please, inser a nickname
    nickLabel = tk.Label(nickFrame, text="Please, insert a nickname: ")
    nickLabel.pack(side="top")
    #Se define en nickFrame un entry para almacenar el nickname del nuevo usuario
    nickEntry = tk.Entry(nickFrame)
    nickEntry.pack(side="top")
    #Se define passwordFrame como frame para el label y entry del password del nuevo
    #usuario
    passwordFrame = tk.Frame(register)
    passwordFrame.pack(side="top")
    #Se define en passwordFrame un label ---> Please, insert your password
    passwordLabel = tk.Label(passwordFrame, text="Please, insert your password")
    passwordLabel.pack(side="top")
    #Se define en passwordFrame un entry para almacenar el password del nuevo usuario
    passwordEntry = tk.Entry(passwordFrame, show="*")
    passwordEntry.pack(side="top")
    #Se define otro label en passwordFrame para confirmar contraseña --->
    #Please, confirm your password
    passwordLabel2 = tk.Label(passwordFrame, text="Please, confirm password ")
    passwordLabel2.pack(side="top")
    #Se define un entry en passwordFrame para almacenar la confirmación de contraseña
    #del nuevo usuario
    passwordEntry2 = tk.Entry(passwordFrame, show="*")
    passwordEntry2.pack(side="top")
    #Se define un frame buttonFrame para el botón que permite registrar el nuevo usuario
    buttonFrame = tk.Frame(register)
    buttonFrame.pack(side="top")
    #Si gender.get() == 1 se setea gender como "Mujer"
    if gender.get() == 1:
        gender.set("Mujer")
    #Si gender.get() == 2 se setea gender como "Hombre"
    elif gender.get() == 2:
        gender.set("Hombre")
    print("Gender: ", gender.get())
    #Se define un butón con el texto register y que llama a la función registerUser para registrar el nuevo usuario
    registerButton = tk.Button(buttonFrame, text="register", command=lambda: registerUser(register, nameEntry.get(),ageEntry.get(), gender.get(),nationality.get(), nickEntry.get(), passwordEntry.get(), passwordEntry2.get()))
    registerButton.pack(side="top")

#Función para loguear a un usuario
def signInAction():
    #Se define una nueva interfaz signIn cuyo padre es window definido
    #previamente como global
    signIn = tk.Toplevel(window)
    #Se define un nameFrame como un nuevo frame cuyo padre es signIn
    nameFrame = tk.Frame(signIn)
    nameFrame.pack(side="top")
    #Se define en nameFrame un label ---> Please, insert your name
    nameLabel = tk.Label(nameFrame, text="Please, insert your name: ")
    nameLabel.pack(side="top")
    #Se define un entry en nameFrame para almacenar el nickname del usuario a loguear
    nameEntry = tk.Entry(nameFrame)
    nameEntry.pack(side="top")
    #Se define passwordFrame como nuevo cuyo padre es signIn
    passwordFrame = tk.Frame(signIn)
    passwordFrame.pack(side="top")
    #Se define en passwordFrame un label ---> Please, insert your password
    passwordLabel = tk.Label(passwordFrame, text="Please, insert your password: ")
    passwordLabel.pack()
    #Se define un entry en passwordFrame para almacenar la contraseña del
    #usuario a loguear
    passwordEntry = tk.Entry(passwordFrame, show="*")
    passwordEntry.pack()
    #Se define buttonFrame como Frame en signIn
    buttonFrame = tk.Frame(signIn)
    buttonFrame.pack(side="top")
    #Se define dentro de buttonFrame un botón con el texto "sign in" y que llama
    #a la funciónn signInUser
    buttonSignIn = tk.Button(buttonFrame, text="sign in", command=lambda: signInUser(signIn, nameEntry.get(), passwordEntry.get()))
    buttonSignIn.pack(side="top")

#Se inicializa la variable loggerUser --> dice que usuario esta logueado
loggedUser = list()
#Se establece el menu inicial
window = tk.Tk()
#Se le asigna al menu inicial un tamaño de 350x150px
window.geometry("350x150")
window.title("Python social network")
#Se define un botón para registrar un nuevo usuario
registerButton = tk.Button(window, text='register', command=lambda: registerAction(window))
registerButton.pack(side="top")
registerButton.config(bg="grey", relief="sunken", padx=15, pady=15, width=15)
#Se define un botón para que un usuario ya eixstente se loguee
signinButton = tk.Button(window, text='sign in', command=signInAction)
signinButton.pack(side="top")
signinButton.config(bg="grey", relief="sunken", padx=15, pady=15, width=15)
print(window.configure().keys())
window.mainloop()