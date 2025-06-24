from flask import Flask, render_template, request, redirect, url_for, session
from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

juego = Ahorcado()


@app.route('/')
def elegir_dificultad():
    session.pop('show_pista', None)
    return render_template('dificultad.html')


@app.route('/iniciar/<nivel>')
def iniciar(nivel):
    session.pop('show_pista', None)
    juego.iniciar_juego(dificultad=nivel)
    return redirect(url_for('jugar'))


@app.route('/jugar')
def jugar():
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
    letra = request.form.get('letra', '').lower()
    if letra and not juego.juego_finalizado:
        juego.intento(letra)
        juego.validar_fin_del_juego()
    return redirect(url_for('jugar'))


@app.route('/reiniciar')
def reiniciar():
    session.pop('show_pista', None)    
    juego.iniciar_juego() 
    return redirect(url_for('elegir_dificultad'))



if __name__ == '__main__':
    app.run(debug=True)
else: 
    application = app
