class Pasajero:
    rutas_validas = ["Iquitos-Nauta", "Iquitos-Yurimaguas", "Iquitos-Pucallpa", "Iquitos-Sta. Rosa"]

    def __init__(self, dni, nombre_completo, edad, peso_equipaje, ruta):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.peso_equipaje = peso_equipaje
        self.ruta = ruta

#Properties con validación (Getter & Setter)

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
        if len(valor) == 8 and valor.isdigit():
            self.__dni = valor
        else:
            raise ValueError("El DNI debe tener exactamente 8 dígitos y estos deben ser numéricos.")

    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor):
        limpio = valor.strip().title()
        if len(limpio) >= 5:
            self.__nombre_completo = limpio
        else:
            raise ValueError("El nombre debe poseer menos 5 caracteres.")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 120:
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser un numero entero entre 0 y 120.")


    @property
    def peso_equipaje(self):
        return self.__peso_equipaje

    @peso_equipaje.setter
    def peso_equipaje(self, valor):
        if 0 <= valor <= 25:
            self.__peso_equipaje = float(valor)
        else:
            raise ValueError("El peso del equipaje debe estar entre 0 y 25 kg.")

    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, valor):
        if valor in self.rutas_validas:
            self.__ruta = valor
        else:
            raise ValueError(f"Esta ruta no esta permitida. Estas son las disponibles: {', '.join(self.rutas_validas)}")
        
    #Properties Calculadas/de solo lectura:

    @property
    def categoria_edad(self):
        if self.edad < 12: return "Niño"
        elif 12 <= self.edad <= 17: return "Adolescente"
        elif 18 <= self.edad <= 59: return "Adulto"
        else: return "Adulto mayor"

    @property
    def tarifa_base(self):
        tarifas = {
            "Iquitos-Nauta": 25,
            "Iquitos-Sta. Rosa": 80,
            "Iquitos-Yurimaguas": 120,
            "Iquitos-Pucallpa": 180
        }
        return tarifas.get(self.ruta, 0)

    @property
    def recargo_equipaje(self):
        if self.peso_equipaje > 15:
            return (self.peso_equipaje - 15) * 2
        return 0

    @property
    def tarifa_total(self):
        tarifa_b = self.tarifa_base
        # Aplicacion del descuento de 50% de la tarifa base por ser un niño o mayor
        if self.categoria_edad in ["Niño", "Adulto mayor"]:
            tarifa_b *= 0.5
        
        return tarifa_b + self.recargo_equipaje

    # Boleta legible

    def __str__(self):
        return (
            f"\n{'='*40}\n"
            f"      <<BOLETO DE PASAJE FLUVIAL>>\n"
            f"{'='*40}\n"
            f"Pasajero:     {self.nombre_completo}\n"
            f"DNI:          {self.dni}\n"
            f"Edad:         {self.edad} ({self.categoria_edad})\n"
            f"Ruta:         {self.ruta}\n"
            f"Equipaje:     {self.peso_equipaje} kg\n"
            f"{'-'*40}\n"
            f"Tarifa Base:  S/. {self.tarifa_base:.2f}\n"
            f"Recargo Eq.:  S/. {self.recargo_equipaje:.2f}\n"
            f"TOTAL A PAGAR: S/. {self.tarifa_total:.2f}\n"
            f"{'='*40}\n"
        )


try:
    pasajero1 = Pasajero("77669842", "joao marcos", 21, 17.6, "Iquitos-Nauta")
    print(pasajero1)
except ValueError as e:
    print(e)

