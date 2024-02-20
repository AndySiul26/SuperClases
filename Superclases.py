class Alimento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def obtener_nombre(self):
        return self.nombre

    def obtener_tipo(self):
        return self.tipo

    def __str__(self):
        return f"{self.nombre} - Tipo: {self.tipo}"

class Fruta(Alimento):
    def __init__(self, nombre, tipo, color):
        super().__init__(nombre, tipo)
        self.color = color

    def obtener_color(self):
        return self.color

    def __str__(self):
        return f"{self.color} {self.nombre} - Tipo: {self.tipo}"

class Manzana(Fruta):
    def __init__(self, color):
        super().__init__("Manzana", "Fruta", color)

class Platano(Fruta):
    def __init__(self, color):
        super().__init__("Plátano", "Fruta", color)

class Pera(Fruta):
    def __init__(self, color):
        super().__init__("Pera", "Fruta", color)

class Carne(Alimento):
    def __init__(self, tipo):
        super().__init__("Carne", tipo)

class Pescado(Alimento):
    def __init__(self, tipo):
        super().__init__("Pescado", tipo)

class Huevo(Alimento):
    def __init__(self, tipo):
        super().__init__("Huevo", tipo)

# Ejemplo de uso
manzana_verde = Manzana("verde")
platano_amarillo = Platano("amarillo")
pera_verde = Pera("verde")
carne_res = Carne("Res")
pescado_salmón = Pescado("Salmón")
huevo_gallina = Huevo("Gallina")

print(manzana_verde)
print(platano_amarillo)
print(pera_verde)
print(carne_res)
print(pescado_salmón)
print(huevo_gallina)
