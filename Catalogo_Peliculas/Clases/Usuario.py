class Usuario:
    def __init__(self, nombre_usuario, contraseña, es_admin=False):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.es_admin = es_admin
        self.listas_creadas = []  # Listas de reproducción creadas por el usuario
        self.resenias = []  # Reseñas realizadas por el usuario

    def crear_lista(self, titulo, etiquetas, peliculas):
        # Lógica para crear una nueva lista de reproducción
        pass

    def dejar_resenia(self, pelicula, resenia, calificacion):
        # Lógica para dejar una reseña y calificación de una película
        pass
