from ahorcado import Ahorcado

def test_letra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_letra("x") == False

def test_letra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_letra("i") == True

def test_palabra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_palabra("metodologias") == False

def test_palabra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_palabra("agiles") == True

if __name__ == "__main__":
    test_letra_incorrecta()
    test_letra_correcta()
    test_palabra_incorrecta()
    test_palabra_correcta()
    print("Test passed!")