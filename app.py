from flask import Flask, render_template, request, redirect, url_for, session
from ahorcado import Ahorcado
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

def guardar_estado_en_session(juego):
    session['palabra']      = juego.palabra_a_adivinar
    session['pista']        = juego.pista
    session['usadas']       = juego.letras_usadas
    session['adivinadas']   = juego.letras_adivinadas
    session['restantes']    = juego.intentos_restantes
    session['palabra_a_mostrar'] = juego.palabra_a_mostrar
    session['juego_finalizado'] = juego.juego_finalizado
    session['estado']       = juego.estado
    session['mostrar_pista']= session.get('show_pista', False)

def cargar_estado_desde_session():
    j = Ahorcado()
    if 'palabra' in session:
        j.palabra_a_adivinar   = session['palabra']
        j.pista                = session.get('pista', '')
        j.letras_usadas        = session.get('usadas', [])
        j.letras_adivinadas    = session.get('adivinadas', [])
        j.intentos_restantes   = session.get('restantes', 7)
        j.juego_finalizado     = session.get('juego_finalizado', False)
        j.estado               = session.get('estado', '')
        j.palabra_a_mostrar    = ['_' if c not in j.letras_adivinadas else c 
                                   for c in j.palabra_a_adivinar]
    return j

#juego = Ahorcado()


@app.route('/')
def elegir_dificultad():
    session.clear()
    #session.pop('show_pista', None)
    return render_template('dificultad.html')


@app.route('/iniciar/<nivel>')
def iniciar(nivel):
    session.pop('show_pista', None)
    juego = Ahorcado()
    juego.iniciar_juego(dificultad=nivel)
    guardar_estado_en_session(juego)
    return redirect(url_for('jugar'))

'''@app.route('/inicio')
def inicio_personalizado():
    session.pop('show_pista', None)
    palabra = request.args.get('palabra', '')
    pista   = request.args.get('pista', '')
    juego = Ahorcado()
    juego.iniciar_juego(palabra=palabra, pista=pista)
    guardar_estado_en_session(juego)
    return redirect(url_for('jugar'))'''

@app.route('/jugar')
def jugar():
    if request.args.get('mostrar_pista') == '1':
        session['show_pista'] = True
    show_pista = session.get('show_pista', False)

    juego = cargar_estado_desde_session()

    if juego.juego_finalizado:
        return render_template(
            'resultado.html',
            estado=juego.estado,
            palabra_secreta=juego.palabra_a_adivinar
        )

    return render_template(
        'juego.html',
        palabra_a_mostrar=" ".join(juego.palabra_a_mostrar),
        pista=juego.pista,
        intentos=juego.intentos_restantes,
        letras_usadas=", ".join(juego.letras_usadas),
        #juego_finalizado=juego.juego_finalizado,
        #estado=juego.estado,
        #palabra_secreta=juego.palabra_a_adivinar if juego.juego_finalizado else "",
        show_pista=show_pista
    )


@app.route('/intentar', methods=['POST'])
def intentar():
    letra = request.form.get('letra', '').lower()
    juego = cargar_estado_desde_session()
    if letra and not juego.juego_finalizado:
        juego.intento(letra)
        juego.validar_fin_del_juego()
    guardar_estado_en_session(juego)
    return redirect(url_for('jugar'))


@app.route('/reiniciar')
def reiniciar():
    session.clear()
    #session.pop('show_pista', None)
    return redirect(url_for('elegir_dificultad'))


if __name__ == '__main__':
    app.run(debug=True)
