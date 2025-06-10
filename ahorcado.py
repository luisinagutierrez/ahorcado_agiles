# Este es ahorcado.py
import random

palabras_faciles = ["agua", "gato", "mesa", "libro"]
palabras_intermedias = ["programa", "computadora", "telefono"]
palabras_dificiles = ["algoritmo", "metodologia", "paradigma"]

class Ahorcado:
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ""
        self.letras_usadas = []
        self.intentos = 7
        self.letras_adivinadas = []
        self.intentos_restantes = 7
        self.palabra_a_mostrar = []
        self.juego_finalizado = False

    def validar_letra(self, letra):
        if len(self.palabra_a_mostrar) != len(self.palabra_a_adivinar):
            self.palabra_a_mostrar = ['_'] * len(self.palabra_a_adivinar)
        
        if letra not in self.palabra_a_adivinar:
            print(f"Letra incorrecta: {letra}")
            self.intentos_restantes -= 1
            return False
        else:
            print(f"Letra correcta: {letra}")
            for i, char in enumerate(self.palabra_a_adivinar):
                if char == letra:
                    self.palabra_a_mostrar[i] = letra
            return True

    def validar_palabra(self, palabra):
        if palabra != self.palabra_a_adivinar:
            print(f"Palabra incorrecta: {palabra}")
            return False
        else:
            print(f"Palabra correcta: {palabra}")
            return True

    def iniciar_juego(self, palabra=None, dificultad=None):
        self.intentos = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.juego_finalizado = False
        
        if palabra is None or palabra == "":
            self.palabra_a_adivinar = self.elegir_palabra(dificultad)
        else:
            print(f"Palabra a adivinar: {palabra}")
            self.palabra_a_adivinar = palabra
        self.palabra_a_mostrar = ['_' for _ in self.palabra_a_adivinar]
        self.intentos_restantes = 7

    def intento(self, letra):
        """
        Hace un intento con una letra:
        - Si ya se usó, devuelve False directamente.
        - Si no se usó:
            * Agrega a letras_usadas.
            * Si es correcta, la guarda en letras_adivinadas y devuelve True.
            * Si es incorrecta, ya restó intentos en validar_letra y devuelve False.
        """
        if letra in self.letras_usadas:
            return False

        # Marco la letra como usada
        self.letras_usadas.append(letra)

        if self.validar_letra(letra):
            # Letra correcta: guardo en adivinadas
            self.letras_adivinadas.append(letra)
            return True

        return False

    def validar_fin_del_juego(self):
        if (
            self.intentos_restantes == 0
            or "".join(self.palabra_a_mostrar) == self.palabra_a_adivinar
        ):
            self.juego_finalizado = True
        return self.juego_finalizado

    def elegir_palabra(self, dificultad):
        if dificultad == "facil":
            self.palabra_a_adivinar = random.choice(palabras_faciles)
        elif dificultad == "intermedia":
            self.palabra_a_adivinar = random.choice(palabras_intermedias)
        else:
            self.palabra_a_adivinar = random.choice(palabras_dificiles)
        return self.palabra_a_adivinar

