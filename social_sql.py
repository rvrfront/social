# DESAFIO 7: RED SOCIAL. LA INTERFAZ
# Imagina y diseña tu propia red social. Decide qué grado de interacción vas a permitir a los usuarios y
# diseña el esquema de la misma
# Utiliza sqlite3 para crear una conexión a la base de datos de la red social y crea las tablas que sean necesarias
# Crea la interfaz con la que interaccionarán los usuarios. Ésta debe permitir que se introduzcan datos o
# información por parte de los usuarios
# Utiliza la opción de checkbuttons para permitir la interacción de un usuario con la información generada por otro
# Programa que se vaya almacenando en la base de datos la información generada por los usuarios
# Crea la interfaz de forma que muestre la información mínima necesaria para interaccionar.
# Simula la actividad de 3 usuarios en tu red social de forma que quede recogido en la base de datos.

# PUNTUACIÓN:
# 2 PTOS - Creación de la base de datos, esquema coherente, 4 tablas como mínimo
# 2 PTOS - Creación de la interfaz con opción de interacción usuario-interfaz
#	vinculado a generar registro en la base de datos
# 4 PTOS - Habilitación de opción en la interfaz para interacción usuario - usuario,
#	con llamada a la base de datos y almacenamiento en la misma de la interacción resultante
# * PTOS - Cualquier funcionalidad extra que aporte valor a la red social

import sqlite3 as sq3
import tkinter
from tkinter import messagebox

#Función para crear la base de datos en social.db
def createDB(name):
    if isinstance(name, str) and name != '':
        try:
            #Primero se crea la tabla users
            connection = sq3.connect(name)
            cursor = connection.cursor()
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(40) NOT NULL,
                            age INTEGER NOT NULL,
                            gender VARCHAR(8) NOT NULL,
                            nationality VARCHAR(30) NOT NULL,
                            nick VARCHAR(15) NOT NULL,
                            password VARCHAR(20) NOT NULL
                            )
                            ''')

            #Después se crea la tabla posts
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title VARCHAR(50) NOT NULL,
                            description VARCHAR(125) NOT NULL,
                            user_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id)
                            )
                            ''')

            #A continuación se crea la tabla comments
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS comments (
                            id INTEGER NOT NULL,
                            text VARCHAR(500) NOT NULL,
                            user_id INTEGER NOT NULL,
                            post_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id),
                            FOREIGN KEY(post_id) REFERENCES posts(id)
                            )
                            ''')

            #Después se crea la tabla likes
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS likes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            post_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id),
                            FOREIGN KEY(post_id) REFERENCES posts(id)
                            )
                            ''')
            #Después de modificar la base de datos se debe hacer un commit
            #para cerrar la conexión posteriormente
            connection.commit()
            connection.close()
            print("DB created successfully!")
        except:
            #En caso de que haya algún error al crear a base de datos se captura
            #dicho error y se muestra un mensaje descriptivo
            print("There was an error on createDB function!")
    else:
        print("You have typed a wrong DB name!")


#Función para actualizar un determinado usuario de la tabla users de la
#base de datos
def updateUserDB(id, name, age, gender, nationality, nickname, password):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name=? WHERE id=?", (name, id))
        cursor.execute("UPDATE users SET age=? WHERE id=?", (age, id))
        cursor.execute("UPDATE users SET gender=? WHERE id=?", (gender, id))
        cursor.execute("UPDATE users SET nationality=? WHERE id=?", (nationality, id))
        cursor.execute("UPDATE users SET nick=? WHERE id=?", (nickname, id))
        cursor.execute("UPDATE users SET password=? WHERE id=?", (password, id))
        connection.commit()
        connection.close()
    except:
        messagebox.showerror(title="Error from updateUserDB", message=f"I could not update user_id: {id}")

#Función para buscar en la tabla users un usuario con un determinado id
def searchAnUser(id):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM users WHERE id=?", (id,))
        user = cursor.fetchone()
        connection.commit()
        connection.close()
        print("Searched user is: ", user)
        return user
    except:
        messagebox.showerror(title="Error from searchAnUser", message=f"I could not find user_id: {id}")

#Función para ir añadiendo nuevos posts a la tabla posts
#de la base de datos
def createAPost(location, id, title, description):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        postItem = (title, description, id)
        cursor.execute("INSERT INTO posts (title,description, user_id) VALUES (?,?,?)", postItem)
        connection.commit()
        connection.close()
        #Se destruye el interfaz padre (location) que llama a esta función
        location.destroy()
    except:
        messagebox.showerror(title="Error from createAPost", message=f"I could not create new post: {title}")

#Función para actualizar un determinado post de la tabla posts de la
#base de datos
def updatePost(location1, location2,location3, id, title, message):
    try:
        print("id from updatePost sql: ", id)
        print("title from updatepost sql :", title)
        print("message from updatepost sql: ", message)
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE posts SET title=? WHERE id=?", (title, id,))
        cursor.execute("UPDATE posts SET description=? WHERE id=?", (message, id,))
        connection.commit()
        connection.close()
        #Después de actualizar el post en cuestión se destruye los siguientes interfaces
        #que son respectivamente las intefaces padre, abuelo y bisabuelo de la función
        #que llama a updatePost
        location3.destroy()
        location2.destroy()
        location1.destroy()
    except:
        messagebox.showerror(title="Error From updatePost", message=f"I colud not update post: {id}")

#Función que obtiene todos los posts de la table posts de la
#base de datos
def getPosts():
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        connection.commit()
        connection.close()
        return posts
    except:
        messagebox.showerror(title="Error From getPosts", message="I could not get all posts")

#Función que obtiene un determinado post de la tabla posts de la
#base de datos
def getOnePost(id):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT title, description, user_id FROM posts WHERE id=?", (id,))
        post = cursor.fetchall()
        connection.commit()
        connection.close()
        return post
    except:
        messagebox.showerror(title="Error From getOnePost", message=f"I could not get post: {id}")

#Función que elimina un determinado post de la tabla posts de la
#base de datos
def delPost(id):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM posts WHERE id=?", (id,))
        connection.commit()
        connection.close()
    except:
        messagebox.showerror(title="Error From delPost", message=f"I could not del post: {id}")

#Función que obtiene el user_id de un usuario de la tabla
#users en función de su nickname y password
def getUserId(name, password):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM users WHERE nick =? AND password=?", (name, password,))
        id = cursor.fetchall()
        print("Id from getUSer sql: ", id)
        connection.commit()
        connection.close()
        return id
    except:
        messagebox.showerror(title="Error From getUserId", message=f"I could not find user: {user}")

#Función que retorna el user_id del usuario que está logueado
def getUserLoggedIn(user, password):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM users WHERE nick=? AND password=?", (user, password,))
        userData = cursor.fetchall()
        connection.commit()
        connection.close()
        print("UserData from getUserLoggedIn: ", userData)
        return userData
    except:
        messagebox.showerror(title="Error From getUserLoggedIn", message=f"I could not get {user}'s id")

#Función que retorna todos los usuarios de la tabla users
#de la base de datos
def getAllUsers():
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        connection.commit()
        connection.close()
        return users
    except:
        messagebox.showerror(title="Error From getAllUsers", message="I could not get all users")

#Fución que añade un nuevo usuario a la tabla users de la
#base de datoa
def registerNewUser(name, age, gender, nationality, nick, password):
    try:
        connection = sq3.connect("social.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES (null,?,?,?,?,?,?)", (name, age, gender, nationality, nick, password))
        connection.commit()
        connection.close()
    except:
        messagebox.showerror(title="Error From registerNewUser", message=f"I could not register {user} user")


createDB("social.db")
