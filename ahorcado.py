# Este es ahorcado.py
import random

palabras_faciles = [
    ["sol", "Astro que ilumina el día"],
    ["gato", "Animal doméstico que maúlla"],
    ["árbol", "Planta grande con tronco y ramas"],
    ["helado", "Postre frío ideal en verano"],
    ["pelota", "Objeto redondo que se usa para jugar"],
    ["luna", "Satélite natural de la Tierra"],
    ["silla", "Mueble donde te sentás"],
    ["pan", "Alimento básico hecho de harina"],
    ["agua", "Líquido esencial para la vida"],
    ["flor", "Parte colorida de algunas plantas"]
]

palabras_intermedias = [
    ["misterio", "Algo que no se puede explicar fácilmente"],
    ["cautela", "Precaución o cuidado al actuar"],
    ["brújula", "Instrumento para orientarse"],
    ["murmullo", "Sonido bajo y continuo de voces"],
    ["destino", "Lugar o meta a la que se quiere llegar"],
    ["legado", "Herencia cultural o material que se deja"],
    ["refugio", "Lugar seguro donde protegerse"],
    ["espejismo", "Ilusión óptica, especialmente en el desierto"],
    ["abismo", "Profundidad grande y peligrosa"],
    ["fragancia", "Olor agradable y suave"]
]

palabras_dificiles = [
    ["efervescente", "Que desprende burbujas o entusiasmo"],
    ["inefable", "Tan increíble que no se puede describir con palabras"],
    ["arcano", "Muy secreto o difícil de comprender"],
    ["quimera", "Sueño o ilusión que es casi imposible"],
    ["elucidar", "Aclarar o explicar algo confuso"],
    ["parsimonia", "Calma y lentitud excesiva"],
    ["melancolía", "Tristeza suave y reflexiva"],
    ["procrastinar", "Postergar o dejar para más tarde una tarea"],
    ["subrepticio", "Que se hace a escondidas o con disimulo"],
    ["sagaz", "Que tiene astucia y buen juicio"]
]

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
        self.pista = ""

    def validar_letra(self, letra):
        if len(self.palabra_a_mostrar) != len(self.palabra_a_adivinar):
            self.palabra_a_mostrar = ['_'] * len(self.palabra_a_adivinar)

        if letra not in self.palabra_a_adivinar:
            #print(f"Letra incorrecta: {letra}")
            self.intentos_restantes -= 1
            return False
        else:
            #print(f"Letra correcta: {letra}")
            for i, char in enumerate(self.palabra_a_adivinar):
                if char == letra:
                    self.palabra_a_mostrar[i] = letra
            return True

    def validar_palabra(self, palabra):
        if palabra != self.palabra_a_adivinar:
            #print(f"Palabra incorrecta: {palabra}")
            return False
        else:
            #print(f"Palabra correcta: {palabra}")
            return True

    def iniciar_juego(self, palabra=None, dificultad=None, pista=None):
        self.intentos = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.juego_finalizado = False
        self.pista = ""

        if palabra is None or palabra == "":
            self.palabra_a_adivinar = self.elegir_palabra(dificultad)
            self.pista = "" # no la vamos a dar una pista en este caso 
        else:
            #print(f"Palabra a adivinar: {palabra}")
            self.palabra_a_adivinar = palabra
            self.pista = pista if pista else ""

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

        self.letras_usadas.append(letra)
        if self.validar_letra(letra):
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
    
    def obtener_pista(self):
        return self.pista
    
    def letras_utilizadas(self, letra):
        return letra in self.letras_adivinadas


