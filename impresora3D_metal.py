class Impresora3DMetal:
    def __init__(self):
        self._temperatura = 0
        self._velocidad_impresion = 0
        self._nivel_polvo_metal = 100

    def get_temperatura(self):
        return self._temperatura

    def set_temperatura(self, valor):
        if 0 <= valor <= 1500:
            self._temperatura = valor
        else:
            raise ValueError("La temperatura debe estar entre 0 y 1500°C")

    def get_velocidad_impresion(self):
        return self._velocidad_impresion

    def set_velocidad_impresion(self, valor):
        if 1 <= valor <= 10:
            self._velocidad_impresion = valor
        else:
            raise ValueError("La velocidad de impresión debe estar entre 1 y 10 mm/s")

    def get_nivel_polvo_metal(self):
        return self._nivel_polvo_metal

    def set_nivel_polvo_metal(self, valor):
        if 0 <= valor <= 100:
            self._nivel_polvo_metal = valor
        else:
            raise ValueError("El nivel de polvo de metal debe estar entre 0 y 100%")

    def calentar(self, incremento):
        nueva_temperatura = min(self.get_temperatura() + incremento, 1500)
        self.set_temperatura(nueva_temperatura)
        return self.get_temperatura()

    def ajustar_velocidad(self, nueva_velocidad):
        try:
            self.set_velocidad_impresion(nueva_velocidad)
            return self.get_velocidad_impresion()
        except ValueError:
            return None

    def imprimir(self, tiempo):
        consumo_por_segundo = self.get_velocidad_impresion() * 0.1
        consumo_total = consumo_por_segundo * tiempo
        if consumo_total <= self.get_nivel_polvo_metal():
            nuevo_nivel = self.get_nivel_polvo_metal() - consumo_total
            self.set_nivel_polvo_metal(nuevo_nivel)
            return self.get_nivel_polvo_metal()
        return None

    def __str__(self):
        return f"Impresora 3D Metal - Temperatura: {self.get_temperatura()}°C, Velocidad: {self.get_velocidad_impresion()} mm/s, Nivel de polvo: {self.get_nivel_polvo_metal():.2f}%"