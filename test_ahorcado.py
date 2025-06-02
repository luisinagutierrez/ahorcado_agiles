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
    
def test_iniciar_juego():
    juego = Ahorcado()
    assert juego.intentos == 7
    assert juego.letras_adivinadas == []
    
def test_intento_incorrecto():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.intento("t") == False
    assert juego.letras_adivinadas == []
    assert juego.letras_usadas == ["t"]
    assert juego.intentos_restantes == 6  
    
def test_intento_correcto():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "agiles"
    assert juego.intento("i") == True
    assert juego.letras_adivinadas == ["i"]
    assert juego.letras_usadas == ["i"]
    assert juego.intentos_restantes == 7  

        

if __name__ == "__main__":
    test_letra_incorrecta()
    test_letra_correcta()
    test_palabra_incorrecta()
    test_palabra_correcta()
    test_iniciar_juego()
    test_intento_incorrecto()
    test_intento_correcto()
    print("Test passed!")