class Cuenta:
    def _init_(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    def setTitular(self, titular):
        self.titular = titular

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def getTitular(self):
        return self.titular

    def getCantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def _init_(self, titular, cantidad=0, bonificacion=0):
        super()._init_(titular, cantidad)
        self.__bonificacion = bonificacion

    def setBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def getBonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        edad = datetime.date.today().year - self.titular.getFechaNacimiento().year
        return edad >= 18 and edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print(f"Cuenta Joven: Titular: {self.titular}, Cantidad: {self.getCantidad()}, Bonificación: {self.__bonificacion}%")



