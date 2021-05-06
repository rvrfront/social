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

def createDB(name):
    if isinstance(name, str) and name != '':
        try:
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

            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title VARCHAR(50) NOT NULL,
                            description VARCHAR(125) NOT NULL,
                            user_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id)
                            )
                            ''')

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

            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS likes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            post_id INTEGER NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id),
                            FOREIGN KEY(post_id) REFERENCES posts(id)
                            )
                            ''')
            connection.commit()
            connection.close()
            print("DB created successfully!")
        except:
            print("There was an error on createDB function!")
    else:
        print("You have typed a wrong DB name!")


def updateUserDB(id, name, age, gender, nationality, nickname, password):
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

def searchAnUser(id):
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users WHERE id=?", (id,))
    user = cursor.fetchone()
    print("Searched user is: ", user)
    return user

def CreateAPost(location, id, title, description,):
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    postItem = (title, description, id)
    cursor.execute("INSERT INTO posts (title,description, user_id) VALUES (?,?,?)", postItem)
    connection.commit()
    connection.close()
    location.destroy()

def updatePost(location1, location2,location3, id, title, message):
    print("id from updatePost sql: ", id)
    print("title from updatepost sql :", title)
    print("message from updatepost sql: ", message)
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE posts SET title=? WHERE id=?", (title, id,))
    cursor.execute("UPDATE posts SET description=? WHERE id=?", (message, id,))
    connection.commit()
    connection.close()
    location3.destroy()
    location2.destroy()
    location1.destroy()

def getPost(id):
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts WHERE id=?", (id,))
    post = cursor.fetchall()
    print("Post from getPost social_sql: ", post)
    connection.commit()
    connection.close()
    return post

def getPosts():
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    connection.commit()
    connection.close()
    return posts

def getOnePost(id):
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, user_id FROM posts WHERE id=?", (id,))
    post = cursor.fetchall()
    connection.commit()
    connection.close()
    return post

def delPost(id):
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE id=?", (id,))
    connection.commit()
    connection.close()

def getUserId(name, password):
    connection = sq3.connect("social.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE nick =? AND password=?", (name, password,))
    id = cursor.fetchall()
    print("Id from getUSer sql: ", id)
    connection.commit()
    connection.close()
    return id

createDB("social.db")
