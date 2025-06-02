# ahorcado.py

class Ahorcado:
    def __init__(self):
        self.palabra_a_adivinar = ""
        self.letras_usadas = []
        self.intentos = 7
        self.letras_adivinadas = []
        self.intentos_restantes = 7

    def validar_letra(self, letra):

        return letra in self.palabra_a_adivinar

    def validar_palabra(self, palabra):

        return palabra == self.palabra_a_adivinar

    def iniciar_juego(self, palabra):

        self.intentos = 7
        self.intentos_restantes = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.palabra_a_adivinar = palabra

    def intento(self, letra):
        if letra in self.letras_usadas:
            return False

        self.letras_usadas.append(letra)

        if self.validar_letra(letra):
            self.letras_adivinadas.append(letra)
            return True
        else:
            self.intentos_restantes -= 1
            return False
