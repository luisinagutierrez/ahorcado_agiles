import random

palabras_faciles = {
    "sol": "Astro que ilumina el día",
    "gato": "Animal doméstico que maúlla",
    "arbol": "Planta grande con tronco y ramas",
    "helado": "Postre frío ideal en verano",
    "pelota": "Objeto redondo que se usa para jugar",
    "luna": "Satélite natural de la Tierra",
    "silla": "Mueble donde te sentás",
    "pan": "Alimento básico hecho de harina",
    "agua": "Líquido esencial para la vida",
    "flor": "Parte colorida de algunas plantas"
}

palabras_intermedias = {
    "misterio": "Algo que no se puede explicar fácilmente",
    "cautela": "Precaución o cuidado al actuar",
    "brujula": "Instrumento para orientarse",
    "murmullo": "Sonido bajo y continuo de voces",
    "destino": "Lugar o meta a la que se quiere llegar",
    "legado": "Herencia cultural o material que se deja",
    "refugio": "Lugar seguro donde protegerse",
    "espejismo": "Ilusión óptica, especialmente en el desierto",
    "abismo": "Profundidad grande y peligrosa",
    "fragancia": "Olor agradable y suave"
}

palabras_dificiles = {
    "efervescente": "Que desprende burbujas o entusiasmo",
    "inefable": "Tan increíble que no se puede describir con palabras",
    "arcano": "Muy secreto o difícil de comprender",
    "quimera": "Criatura mitológica compuesta por partes de diferentes animales",
    "elucidar": "Aclarar o explicar algo confuso",
    "parsimonia": "Calma y lentitud excesiva",
    "melancolia": "Tristeza suave y reflexiva",
    "procrastinar": "Postergar o dejar para más tarde una tarea",
    "subrepticio": "Que se hace a escondidas o con disimulo",
    "obnubilar": "Nublar el entendimiento o la claridad mental; confundir o aturdir"
}


class Ahorcado:
    def __init__(self):
        self.palabra_a_adivinar = ""
        self.letras_usadas = []
        self.intentos = 7
        self.letras_adivinadas = []
        self.intentos_restantes = 7
        self.palabra_a_mostrar = []
        self.juego_finalizado = False
        self.pista = ""
        self.estado = ""

    def validar_letra(self, letra):
        if len(self.palabra_a_mostrar) != len(self.palabra_a_adivinar):
            self.palabra_a_mostrar = ['_'] * len(self.palabra_a_adivinar)

        if letra not in self.palabra_a_adivinar:
            self.intentos_restantes -= 1
            return False
        else:
            for i, char in enumerate(self.palabra_a_adivinar):
                if char == letra:
                    self.palabra_a_mostrar[i] = letra
            return True

    def validar_palabra(self, palabra):
        return palabra == self.palabra_a_adivinar

    def iniciar_juego(self, palabra=None, dificultad=None, pista=None):
        self.intentos = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.juego_finalizado = False
        self.pista = ""

        if palabra is None or palabra == "":
            palabra_elegida = self.elegir_palabra(dificultad)
            self.palabra_a_adivinar = palabra_elegida
        else:
            self.palabra_a_adivinar = palabra
            self.pista = pista if pista else ""

        self.palabra_a_mostrar = ['_' for _ in self.palabra_a_adivinar]
        self.intentos_restantes = 7

    def intento(self, letra):
        if letra in self.letras_usadas:
            return False

        self.letras_usadas.append(letra)
        if self.validar_letra(letra):
            self.letras_adivinadas.append(letra)
            return True

        return False

    def validar_fin_del_juego(self):
        if self.intentos_restantes == 0:
            self.juego_finalizado = True
            self.estado = "Perdiste"
        elif "".join(self.palabra_a_mostrar) == self.palabra_a_adivinar:
            self.juego_finalizado = True
            self.estado = "Ganaste"
        return self.juego_finalizado

    def elegir_palabra(self, dificultad):
        if dificultad == "facil":
            dic = palabras_faciles
        elif dificultad == "intermedia":
            dic = palabras_intermedias
        else:
            dic = palabras_dificiles

        palabra = random.choice(list(dic.keys()))
        self.pista = dic[palabra]
        return palabra

    def obtener_pista(self):
        return self.pista

    def letras_utilizadas(self, letra):
        return letra in self.letras_adivinadas
