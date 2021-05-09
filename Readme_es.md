#Pequeña red social desarrollada en python + tkinter
##El directorio de archivos de este repositorio es el siguiente:
|     Nombre archivo.          |  Descripcion                                          |
|------------------------------|-------------------------------------------------------|
|   social.db                  |  Base de datos que contiene:                          |
|                              | -users: tabla donde se almacena los usuarios          |
|                              | -posts: tabla donde se almacena los posts             |
|                              | -comments: tabla donde se almacena los comments .     |
|                              | -likes: tabla donde almacena los likes.               |
|   social_slq.py              | Archivo donde se tiene todas las funciones que atacan |
|                              | la base de datos, como por ejemplo:                   |
|                              | - createDB: función para inicialiar la base de datos  |
|                              | - updateUserDB: función para actualizar el perfin de  |
|                              |   un usuario de la tabla users de la base de datos    |
|                              | - searchAnUser: función para buscar por user_id a un  |
|                              |   usuario en la tabla users de la base de datos       |
|                              | - createAPost: función para añadir un pots a la tabla |
|                              |   tabla posts de la base de datos                     |
|                              | - updatePost: función para actualizar un post con un  |
|                              |   determinado id de la tabla posts de la base de datos|
|                              | - getOnePost: función para obtener un determinado post|
|                              |   por id de la tabla posts de la base de datos        |
|                              | - getPosts: función para obtener todos los posts de la|
|                              |   tabla posts de la base de datos                     |
|                              | - delPost: función para eliminar un determinado post  |
|                              |   por id de la tabla posts de la base de datos        |
|                              | - getUserId: función para obtener el user_id apartir  |
|                              |   del nickname y password de la tabla users de la base|
|                              |   de datos                                            |
|                              | - getUserLoggedIn: función para obtener el user_id del|
|                              |   usuario logueado a partir del nickname y password   |
|                              |   que ese usuario tiene en la tabla post de la base de|
|                              |   datos                                               |
|                              | - getAllUsers: función para obtener todos los usuarios|
|                              |   de la tabla users de la base de datos               |
|                              | - registerNewUser: función para añadir un nuevo       |
|                              |   usuario a la tabla users en la base de datos        |
|------------------------------|-------------------------------------------------------|
