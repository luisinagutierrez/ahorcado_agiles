Feature: Juego de Ahorcado

  Scenario: Elegir dificultad fácil
      Given launch chrome browser
      When  Ingreso a la pagina del juego
      Then  el usuario elige la dificultad "facil"
      And el numero de intentos debe ser 7

  Scenario: Validar letra correcta
      Given un juego de Ahorcado con la palabra "sol", "Astro que ilumina el día"
      When valido la letra "s"
      Then la letra es correcta
      And el numero de intentos restantes debe ser 7
      And la letra "s" esta en la lista de letras usadas

  Scenario: Validar letra incorrecta
      Given un juego de Ahorcado con la palabra "gato", "Animal doméstico que maúlla" para validar letra incorrecta
      When valido la letra "z" incorrecta
      Then la letra es incorrecta
      And el numero de intentos debe ser 6 
      And la letra "z" esta en letras usadas

  Scenario: Ganar Juego
      Given un juego del Ahorcado con la palabra "luna", "Satélite natural de la Tierra"
      When valido las letras "l" "u" "n" "a"
      Then gano la partida

  Scenario: Perder Juego
      Given un juego del Ahorcado con la palabra "subrepticio", "Que se hace a escondidas o con disimulo" (Perder Juego)
      When valido las letras "a" "h" "z" "y" "m" "u" "x" hasta no tener intentos
      Then pierde la partida