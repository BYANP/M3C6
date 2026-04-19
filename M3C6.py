class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

usuario1 = Usuario("Iker", "1234")

print("Usuario:", usuario1.nombre_usuario)
print("Contraseña:", usuario1.contraseña)