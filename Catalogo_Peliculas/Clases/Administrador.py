class Administrador(Usuario):
    def __init__(self, nombre_usuario, contraseña):
        super().__init__(nombre_usuario, contraseña, es_admin=True)

    def agregar_pelicula(self, titulo, año, genero):
        # Lógica para agregar una nueva película
        pass

    def editar_pelicula(self, pelicula, nuevos_datos):
        # Lógica para editar los datos de una película existente
        pass

    def eliminar_comentario(self, lista, comentario):
        # Lógica para eliminar un comentario inadecuado
        pass
