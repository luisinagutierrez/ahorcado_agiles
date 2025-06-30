from multiprocessing import context
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


@given('launch chrome browser')
def launchBrowser(context):
    options = webdriver.ChromeOptions()
    if os.getenv('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://ahorcado-agiles-1acq.vercel.app/")

@when('Ingreso a la pagina del juego')
def step_ingreso_pagina(context):
    context.driver.get("https://ahorcado-agiles-1acq.vercel.app/")
    time.sleep(5)

@then('el usuario elige la dificultad "{nivel}"')
def step_impl(context, nivel):
    button = context.driver.find_element(By.CLASS_NAME, nivel)
    button.click()
    time.sleep(5)

@then('el numero de intentos debe ser 7')
def numero_de_intentos(context):
    intentos = context.driver.find_element(By.CLASS_NAME, "heart-x")
    texto_completo = intentos.text
    numero_intentos = int(texto_completo.replace('×', ''))
    assert numero_intentos == 7
    time.sleep(3)


@given('un juego de Ahorcado con la palabra "{palabra}", "{pista}"')
def inicio_juego_con_palabra(context, palabra, pista):
    options = webdriver.ChromeOptions()
    if os.getenv('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(f"https://ahorcado-agiles-1acq.vercel.app/inicio?palabra={palabra}&pista={pista}")
    time.sleep(5)

@when('valido la letra "{letra}"')
def ingreso_una_letra(context, letra):
    input_letra = context.driver.find_element(By.NAME, "letra")
    submit_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    input_letra.clear()
    input_letra.send_keys(letra)
    submit_button.click()
    time.sleep(2)

@then('la letra es correcta')
def letra_correcta(context):
    palabra_mostrada = context.driver.find_element(By.CLASS_NAME, "word-display")
    texto_completo = palabra_mostrada.text
    assert 's' in texto_completo and '_' in texto_completo
    time.sleep(3)

@then('el numero de intentos restantes debe ser 7')
def numero_de_intentos2(context):
    intentos = context.driver.find_element(By.CLASS_NAME, "heart-x")
    texto_completo = intentos.text
    numero_intentos = int(texto_completo.replace('×', ''))
    assert numero_intentos == 7
    time.sleep(3)

@then('la letra "{letra}" esta en la lista de letras usadas')
def letra_usada2(context,letra):
    letras_usadas = context.driver.find_element(By.CSS_SELECTOR, ".highlight.small")
    texto_completo = letras_usadas.text
    assert letra in texto_completo
    time.sleep(4)
    

@given('un juego de Ahorcado con la palabra "{palabra}", "{pista}" para validar letra incorrecta')
def inicio_juego_con_palabra(context, palabra, pista):
    options = webdriver.ChromeOptions()
    if os.getenv('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(f"https://ahorcado-agiles-1acq.vercel.app/inicio?palabra={palabra}&pista={pista}")
    time.sleep(5)

@when('valido la letra "{letra}" incorrecta')
def ingreso_una_letra(context, letra):
    input_letra = context.driver.find_element(By.NAME, "letra")
    submit_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    input_letra.clear()
    input_letra.send_keys(letra)
    submit_button.click()
    time.sleep(2)

@then('la letra es incorrecta')
def letra_incorrecta(context):
    palabra_mostrada = context.driver.find_element(By.CLASS_NAME, "word-display")
    texto_completo = palabra_mostrada.text
    assert 's' not in texto_completo and '_' in texto_completo
    time.sleep(3)

@then('el numero de intentos debe ser 6')
def numero_de_intentos_6(context):
    intentos = context.driver.find_element(By.CLASS_NAME, "heart-x")
    texto_completo = intentos.text
    numero_intentos = int(texto_completo.replace('×', ''))
    assert numero_intentos == 6
    time.sleep(3)

@then('la letra "{letra}" esta en letras usadas')
def letra_usada(context,letra):
    letras_usadas = context.driver.find_element(By.CSS_SELECTOR, ".highlight.small")
    texto_completo = letras_usadas.text
    assert letra in texto_completo
    time.sleep(4)


@given('un juego del Ahorcado con la palabra "{palabra}", "{pista}" (Ganar Juego)')
def inicio_juego_con_palabra_2(context, palabra, pista):
    options = webdriver.ChromeOptions()
    if os.getenv('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)    
    context.driver.get(f"https://ahorcado-agiles-1acq.vercel.app/inicio?palabra={palabra}&pista={pista}")
    time.sleep(3)

@when('valido las letras "{letra1}" "{letra2}" "{letra3}" "{letra4}" "{letra5}" "{letra6}" "{letra7}"')
def ingreso_una_letra_In(context, letra1, letra2, letra3, letra4, letra5, letra6, letra7):
    letras = [letra1, letra2, letra3, letra4, letra5, letra6, letra7]
    
    for i, letra in enumerate(letras):
        if context.driver.find_elements(By.CSS_SELECTOR, ".game-screen h2.titulo-arcade"):
            break
        
        try:
            input_letra = context.driver.find_element(By.NAME, "letra")
            submit_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        except:
            break
        
        input_letra.clear()
        input_letra.send_keys(letra)
        submit_button.click()
        time.sleep(2)
        
        try:
            palabra_elem = context.driver.find_element(By.CLASS_NAME, "word-display")
            palabra_actual = palabra_elem.text
            
            if '_' not in palabra_actual:
                time.sleep(3)
                break
        except:
            pass
        
        try:
            intentos_elem = context.driver.find_element(By.CLASS_NAME, "heart-x")
            intentos_despues = int(intentos_elem.text.replace('×', ''))
            
            if intentos_despues == 0:
                time.sleep(3)
                break
        except:
            pass
        
        time.sleep(1)
    
    time.sleep(2)

@then('gano la partida')
def ganar_partida(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "titulo-arcade"))
    )
    frase_mostrada = context.driver.find_element(By.CLASS_NAME, "titulo-arcade").text.strip()
    assert frase_mostrada == '¡GANASTE!'
    time.sleep(3)