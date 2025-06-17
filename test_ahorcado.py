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


def test_iniciar_juego_intentos():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert juego.intentos == 7


def test_iniciar_juego_letras_adivinadas_vacio():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    assert juego.letras_adivinadas == []


def test_intento_incorrecto_retorno_false():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    resultado = juego.intento("t")
    assert not resultado


def test_intento_incorrecto_letras_adivinadas():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.intento("t")
    assert juego.letras_adivinadas == []


def test_intento_incorrecto_letras_usadas():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.intento("t")
    assert juego.letras_usadas == ["t"]


def test_intento_incorrecto_intentos_restantes():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.intento("t")
    assert juego.intentos_restantes == 6


def test_intento_correcto_retorno_true():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    resultado = juego.intento("i")
    assert resultado


def test_intento_correcto_letras_adivinadas():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.intento("i")
    assert juego.letras_adivinadas == ["i"]


def test_intento_correcto_letras_usadas():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.intento("i")
    assert juego.letras_usadas == ["i"]


def test_intento_correcto_intentos_restantes():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.intento("i")
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


def test_iniciar_con_dificultad_palabra_en_lista():
    juego = Ahorcado()
    juego.iniciar_juego(dificultad="facil")
    assert juego.palabra_a_adivinar in palabras_faciles


def test_iniciar_con_dificultad_intentos_restantes():
    juego = Ahorcado()
    juego.iniciar_juego(dificultad="facil")
    assert juego.intentos_restantes == 7


def test_iniciar_con_dificultad_longitud_palabra_a_mostrar():
    juego = Ahorcado()
    juego.iniciar_juego(dificultad="facil")
    assert len(juego.palabra_a_mostrar) == len(juego.palabra_a_adivinar)


def test_iniciar_con_dificultad_juego_no_finalizado():
    juego = Ahorcado()
    juego.iniciar_juego(dificultad="facil")
    assert not juego.juego_finalizado


def test_iniciar_con_palabra_directa_palabra():
    juego = Ahorcado()
    palabra = "agiles"
    pista = "Metodología de desarrollo flexible y adaptable"
    juego.iniciar_juego(palabra=palabra, pista=pista)
    assert juego.palabra_a_adivinar == palabra


def test_iniciar_con_palabra_directa_pista():
    juego = Ahorcado()
    palabra = "agiles"
    pista = "Metodología de desarrollo flexible y adaptable"
    juego.iniciar_juego(palabra=palabra, pista=pista)
    assert juego.obtener_pista() == pista


def test_iniciar_con_palabra_directa_longitud():
    juego = Ahorcado()
    palabra = "agiles"
    pista = "Metodología de desarrollo flexible y adaptable"
    juego.iniciar_juego(palabra=palabra, pista=pista)
    assert len(juego.palabra_a_mostrar) == len(palabra)


def test_iniciar_con_palabra_directa_intentos():
    juego = Ahorcado()
    palabra = "agiles"
    pista = "Metodología de desarrollo flexible y adaptable"
    juego.iniciar_juego(palabra=palabra, pista=pista)
    assert juego.intentos_restantes == 7


def test_iniciar_con_palabra_directa_juego_no_finalizado():
    juego = Ahorcado()
    palabra = "agiles"
    pista = "Metodología de desarrollo flexible y adaptable"
    juego.iniciar_juego(palabra=palabra, pista=pista)
    assert not juego.juego_finalizado


def test_obtener_pista():
    juego = Ahorcado()
    pista = "Metodología de desarrollo flexible y adaptable"
    juego.iniciar_juego(palabra="agiles", pista=pista)
    assert juego.obtener_pista() == pista


def test_letras_utilizadas_letra_utilizada():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="casa")
    juego.intento("a")
    assert juego.letras_utilizadas("a")


def test_letras_utilizadas_letra_no_utilizada():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="casa")
    juego.intento("a")
    assert not juego.letras_utilizadas("c")


if __name__ == "__main__":

    test_letra_incorrecta()
    test_letra_correcta()
    test_palabra_incorrecta()
    test_palabra_correcta()
    test_iniciar_juego_intentos()
    test_iniciar_juego_letras_adivinadas_vacio()
    test_intento_incorrecto_retorno_false()
    test_intento_incorrecto_letras_adivinadas()
    test_intento_incorrecto_letras_usadas()
    test_intento_incorrecto_intentos_restantes()
    test_intento_correcto_retorno_true()
    test_intento_correcto_letras_adivinadas()
    test_intento_correcto_letras_usadas()
    test_intento_correcto_intentos_restantes()
    test_estado_del_juego()
    test_estado_del_juego_ganado()
    test_estado_del_juego_perdido()
    test_elegir_palabra_facil()
    test_elegir_palabra_intermedia()
    test_iniciar_con_dificultad_palabra_en_lista()
    test_iniciar_con_dificultad_intentos_restantes()
    test_iniciar_con_dificultad_longitud_palabra_a_mostrar()
    test_iniciar_con_dificultad_juego_no_finalizado()
    test_iniciar_con_palabra_directa_palabra()
    test_iniciar_con_palabra_directa_pista()
    test_iniciar_con_palabra_directa_longitud()
    test_iniciar_con_palabra_directa_intentos()
    test_iniciar_con_palabra_directa_juego_no_finalizado()
    test_obtener_pista()
    test_letras_utilizadas_letra_utilizada()
    test_letras_utilizadas_letra_no_utilizada()
    print("Test passed!")
