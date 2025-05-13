from ahorcado import Ahorcado

def test_letra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_letra("x") == False

def test_letra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.validar_letra("i") == True

if __name__ == "__main__":
    test_letra_incorrecta()
    test_letra_correcta()
    print("Test passed!")