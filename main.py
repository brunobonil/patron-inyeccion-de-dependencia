class Credenciales():
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

class Registrarse():
    def __init__(self, credenciales: Credenciales):
        self.credenciales = Credenciales

if __name__ == '__main__':

    admin = Credenciales('Pepe', 'Gonzalez', 'pepegonzalez@gmail.com', 12345678)
    usuario = Credenciales('Juan', 'Gutierrez', 'juan_gutierrez@gmail.com', 87654321)

    administracion = Registrarse(admin)
    user = Registrarse(usuario)