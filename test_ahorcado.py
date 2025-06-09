# Este es test_ahorcado.py


from ahorcado import Ahorcado


def test_letra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_letra("x") is False


def test_letra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_letra("i") is True


def test_palabra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_palabra("metodologias") is False


def test_palabra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_palabra("agiles") is True


def test_iniciar_juego():
    juego = Ahorcado()
    assert juego.intentos == 7
    assert juego.letras_adivinadas == []


def test_intento_incorrecto():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.intento("t") is False
    assert juego.letras_adivinadas == []
    assert juego.letras_usadas == ["t"]
    assert juego.intentos_restantes == 6


def test_intento_correcto():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.intento("i") is True
    assert juego.letras_adivinadas == ["i"]
    assert juego.letras_usadas == ["i"]
    assert juego.intentos_restantes == 7


def test_estado_del_juego():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    juego.validar_letra("a")
    juego.validar_letra("g")
    assert juego.validar_fin_del_juego() is False


def test_estado_del_juego_ganado():
    juego = Ahorcado()
    juego.palabra_a_mostrar = list("agiles")
    juego.iniciar_juego(palabra="agiles")
    juego.validar_letra("a")
    juego.validar_letra("g")
    juego.validar_letra("i")
    juego.validar_letra("l")
    juego.validar_letra("e")
    juego.validar_letra("s")
    assert juego.validar_fin_del_juego() is True


def test_estado_del_juego_perdido():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="agiles")
    juego.validar_letra("r")
    juego.validar_letra("p")
    juego.validar_letra("q")
    juego.validar_letra("y")
    juego.validar_letra("t")
    juego.validar_letra("z")
    juego.validar_letra("j")
    assert juego.validar_fin_del_juego() is True


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
    print("Test passed!")
