#Pequeña red social desarrollada en python + tkinter
##El directorio de archivos de este repositorio es el siguiente:
|     Nombre archivo.          |  Descripcion                                                                                                                   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|   social.db                  |Base de datos que contiene:                                                                                                     |
|                              | users: tabla donde se almacena los usuarios                                                                                    |
|                              | posts: tabla donde se almacena los posts                                                                                       |
|                              | comments: tabla donde se almacena los comments                                                                                 |
|                              | lkes: tabla donde almacena los likes                                                                                           |
|   social_slq.py              | Archivo donde se tiene todas las funciones que atacan                                                                          |
|                              | la base de datos, como por ejemplo:                                                                                            |
|                              | createDB: función para inicialiar la base de datos                                                                             |
|                              | updateUserDB: función para actualizar el perfin de un usuario de la tabla users de la base de datos                            |
|                              | searchAnUser: función para buscar por user_id a un usuario en la tabla users de la base de datos                               |
|                              | createAPost: función para añadir un pots a la tabla tabla posts de la base de datos                                            |
|                              | updatePost: función para actualizar un post con un determinado id de la tabla posts de la base de datos                        |
|                              | getOnePost: función para obtener un determinado post por id de la tabla posts de la base de datos                              |
|                              | getPosts: función para obtener todos los posts de la tabla posts de la base de datos                                           |
|                              | delPost: función para eliminar un determinado post por id de la tabla posts de la base de datos                                |
|                              | getUserId: función para obtener el user_id apartir del nickname y password de la tabla users de la base de datos               |
|                              | getUserLoggedIn: función para obtener el user_id del usuario logueado a partir del nickname y password de la tabla users de    |
|                              | la base de datos                                                                                                               | 
|                              | getAllUsers: función para obtener todos los usuarios de la tabla users de la base de datos                                     |
|                              | registerNewUser: función para añadir un nuevo usuario a la tabla users en la base de datos                                     |
|   social_gui.py              | Archivo que contiene el diseño de la GUI junto con el uso de las funciones anteriormente descritas                             |
|                              | editPostAction: función que se usa para editar un post en concreto de la tabla posts de la base de datos                       |
|                              | deletePost: función que se usa para eliminar un post en concreto de la tabla posts de la base de datos                         |
|                              | showOnePost: función que se usa para mostrar un post en concreto de la tabla posts de la base dedatos                          |
|                              | showPosts: funciónq que se usa para mostrar todos los posts de la tbala posts de la base de datos                              |
|                              | createPostAction: función que se usa para crear un post en la tabla posts de la base de datos                                  |
|                              | updateUser: función que se usa para editar/actualizar los datos de un usuario en la tabla users de la base de datos            |
|                              | editProfileAction: función para mostrar la interfaz para crear un nuevo usuario en la tabla users de la base de datos          |
|                              | showUserAction: función que se usa para mostrar las distintas acciones que tiene un usuario logueado                           |
|                              | signInUser: función que se usa para hacer el proceso de login de un usuario                                                    |
|                              | registerUser: función que se usa registrar un nuevo usuario en la tabla users de la base de datos                              |
|                              | registerAction: función que crea la interfaz para el proceso de registro de un nuevo usuario                                   | |                              | signInAction: función crea la interfaz para el proceso de login de un usuario                                                  | |------------------------------|--------------------------------------------------------------------------------------------------------------------------------| 
A continuación se muestra las siguientes capturas de pantalla:
-Interfaz inicial register/login:

https://user-images.githubusercontent.com/65725383/117575535-95f6a980-b0e2-11eb-83ae-49597ddb1942.mp4

-Registro de un nuevo usuario

https://user-images.githubusercontent.com/65725383/117575614-e40bad00-b0e2-11eb-9a81-c70d80f85a24.mp4

-Proceso detallado de registro de un nuevo usuario

https://user-images.githubusercontent.com/65725383/117575681-2fbe5680-b0e3-11eb-94f8-270faed01c6d.mp4


-Proceso de logueo de un usuario ya existente

https://user-images.githubusercontent.com/65725383/117575638-f685e680-b0e2-11eb-974f-1040015a5ce0.mp4

-Continuación de proceso de logueo de un usuario ya existente

https://user-images.githubusercontent.com/65725383/117575703-554b6000-b0e3-11eb-9139-c0f2c007e0a4.mp4

-Proceso de creacion de un nuevo post

https://user-images.githubusercontent.com/65725383/117575715-61cfb880-b0e3-11eb-968e-18e61e09273a.mp4

-Como se muestran los posts

https://user-images.githubusercontent.com/65725383/117575744-790ea600-b0e3-11eb-8d9a-e5f18ef3ee9d.mp4

-Proceso de edicion de un post

https://user-images.githubusercontent.com/65725383/117575765-8af04900-b0e3-11eb-8f64-92741151241d.mp4

-Continuación del proceso de edicion de un post

https://user-images.githubusercontent.com/65725383/117575788-9d6a8280-b0e3-11eb-9868-fcb5197c9e86.mp4

-Proceso de eliminación de un post

https://user-images.githubusercontent.com/65725383/117575799-a9eedb00-b0e3-11eb-88d6-5127077f2a0e.mp4





