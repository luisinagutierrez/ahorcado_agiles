class Ahorcado:
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ""
        self.letras_usadas = []
    
    def validar_letra(self, letra):
        if letra not in self.palabra_a_adivinar:
            self.letras_usadas.append(letra)
            print (f"Letra incorrecta: {letra}")
            return False
        else:
            self.letras_usadas.append(letra)
            print (f"Letra correcta: {letra}")
            return True
    
    
    





    
        
