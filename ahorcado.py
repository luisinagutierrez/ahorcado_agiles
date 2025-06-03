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
        if letra not in self.palabra_a_adivinar:
            print (f"Letra incorrecta: {letra}")
            self.intentos_restantes -= 1
            return False
        else:
            print (f"Letra correcta: {letra}")
            return True
        
    def validar_palabra(self, palabra):
        if palabra != self.palabra_a_adivinar:
            print (f"Palabra incorrecta: {palabra}")
            return False
        else:
            print (f"Palabra correcta: {palabra}")
            return True

    def iniciar_juego(self, palabra):
        self.intentos = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.palabra_a_adivinar = palabra

    def intento(self, letra):
        """
        Hace un intento con una letra:
        - Si ya se usó, devuelve False directamente.
        - Si no se usó:
            * Agrega a letras_usadas.
            * Si es correcta, la guarda en letras_adivinadas y devuelve True.
            * Si es incorrecta, resta 1 a intentos_restantes y devuelve False.
        """
        if letra in self.letras_usadas:
            return False

        # Marco la letra como usada
        self.letras_usadas.append(letra)

        if self.validar_letra(letra):
            # Letra correcta: guardo en adivinadas
            self.letras_adivinadas.append(letra)
            return True
        else:
            # Letra incorrecta: pierdo un intento
            return False

    def validar_fin_del_juego(self):
        if self.intentos_restantes == 0 or "".join(self.palabra_a_mostrar) == self.palabra_a_adivinar:
            self.juego_finalizado = True
        return self.juego_finalizado
