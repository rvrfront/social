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
                            gender VARCHAR(1) NOT NULL,
                            nationality VARCHAR(30) NOT NULL,
                            nick VARCHAR(15) NOT NULL,
                            password VARCHAR(20) NOT NULL
                            )
                            ''')

            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER NOT NULL,
                            title VARCHAR(50) NOT NULL,
                            description VARCHAR(125) NOT NULL,
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT
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


createDB("social.db")
