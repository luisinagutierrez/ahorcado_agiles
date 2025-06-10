# Este es test_ahorcado.py

from ahorcado import Ahorcado, palabras_faciles, palabras_intermedias, palabras_dificiles


def test_letra_incorrecta():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert not juego.validar_letra("x")


def test_letra_correcta():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert juego.validar_letra("i")


def test_palabra_incorrecta():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert not juego.validar_palabra("metodologias")


def test_palabra_correcta():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert juego.validar_palabra("agiles")


def test_iniciar_juego():
    juego = Ahorcado()
    assert juego.intentos == 7
    assert juego.letras_adivinadas == []


def test_intento_incorrecto():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert not juego.intento("t")
    assert juego.letras_adivinadas == []
    assert juego.letras_usadas == ["t"]
    assert juego.intentos_restantes == 6


def test_intento_correcto():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert juego.intento("i")
    assert juego.letras_adivinadas == ["i"]
    assert juego.letras_usadas == ["i"]
    assert juego.intentos_restantes == 7


def test_estado_del_juego():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.validar_letra("a")
    juego.validar_letra("g")
    assert not juego.validar_fin_del_juego()


def test_estado_del_juego_ganado():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    for letra in "agiles":
        juego.validar_letra(letra)
    assert juego.validar_fin_del_juego()


def test_estado_del_juego_perdido():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    for letra in ["r", "p", "q", "y", "t", "z", "j"]:
        juego.validar_letra(letra)
    assert juego.validar_fin_del_juego()


def test_elegir_palabra_facil():
    juego = Ahorcado()
    palabra = juego.elegir_palabra("facil")
    assert palabra in palabras_faciles


def test_elegir_palabra_intermedia():
    juego = Ahorcado()
    palabra = juego.elegir_palabra("intermedia")
    assert palabra in palabras_intermedias


def test_elegir_palabra_dificil():
    juego = Ahorcado()
    palabra = juego.elegir_palabra("dificil")
    assert palabra in palabras_dificiles


def test_iniciar_con_dificultad():
    juego = Ahorcado()
    juego.iniciar_juego(dificultad="facil")
    assert juego.palabra_a_adivinar in palabras_faciles
    assert juego.intentos_restantes == 7
    assert len(juego.palabra_a_mostrar) == len(juego.palabra_a_adivinar)
    assert not juego.juego_finalizado

def test_iniciar_con_palabra_directa():
    juego = Ahorcado()
    palabra = "mate"
    pista = "Bebida argentina por excelencia"
    juego.iniciar_juego(palabra=palabra, pista=pista)
    assert juego.palabra_a_adivinar == palabra
    assert juego.obtener_pista() == pista
    assert len(juego.palabra_a_mostrar) == len(palabra)
    assert juego.intentos_restantes == 7
    assert not juego.juego_finalizado

def test_obtener_pista(): 
    juego = Ahorcado()
    pista = "Bebida argentina por excelencia"
    juego.iniciar_juego(palabra="mate", pista=pista)
    assert juego.obtener_pista() == pista  




if __name__ == "__main__":
    test_letra_incorrecta()
    test_letra_correcta()
    test_palabra_incorrecta()
    test_palabra_correcta()
    test_iniciar_juego()
    test_intento_incorrecto()
    test_intento_correcto()
    test_estado_del_juego()
    test_estado_del_juego_ganado()
    test_estado_del_juego_perdido()
    test_elegir_palabra_facil()
    test_elegir_palabra_intermedia()
    test_elegir_palabra_dificil()
    test_iniciar_con_dificultad()
    test_iniciar_con_palabra_directa()
    test_obtener_pista()
    
    print("Test passed!")
