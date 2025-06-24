from flask import Flask, render_template, request, redirect, url_for, session
from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

def get_juego():
    """Obtiene o crea una instancia del juego para la sesión actual"""
    if 'juego_id' not in session:
        session['juego_id'] = True
        session['juego'] = Ahorcado()
    return session['juego']

def reset_juego():
    """Reinicia completamente el juego creando una nueva instancia"""
    session.pop('juego_id', None)
    session.pop('juego', None)
    session.pop('show_pista', None)


@app.route('/')
def elegir_dificultad():
    reset_juego() 
    return render_template('dificultad.html')


@app.route('/iniciar/<nivel>')
def iniciar(nivel):
    reset_juego()
    juego = get_juego()
    juego.iniciar_juego(dificultad=nivel)
    return redirect(url_for('jugar'))


@app.route('/jugar')
def jugar():
    juego = get_juego()
    if request.args.get('mostrar_pista') == '1':
        session['show_pista'] = True
    show_pista = session.get('show_pista', False)

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
        juego_finalizado=juego.juego_finalizado,
        estado=juego.estado,
        palabra_secreta=juego.palabra_a_adivinar if juego.juego_finalizado else "",
        show_pista=show_pista
    )


@app.route('/intentar', methods=['POST'])
def intentar():
    juego = get_juego()
    letra = request.form.get('letra', '').lower()
    if letra and not juego.juego_finalizado:
        juego.intento(letra)
        juego.validar_fin_del_juego()
    return redirect(url_for('jugar'))


@app.route('/reiniciar')
def reiniciar():
    reset_juego()  
    return redirect(url_for('elegir_dificultad'))



if __name__ == '__main__':
    app.run(debug=True)
else: 
    application = app
