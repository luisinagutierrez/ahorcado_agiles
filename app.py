from flask import Flask, render_template, request, redirect, url_for
from ahorcado import Ahorcado

app = Flask(__name__)
juego = Ahorcado()


@app.route('/')
def elegir_dificultad():
    return render_template('dificultad.html')


@app.route('/iniciar/<nivel>')
def iniciar(nivel):
    print(f"Iniciando juego con nivel: {nivel}")
    print(f"Palabra a adivinar: {juego.palabra_a_adivinar}")
    # iniciamos según nivel: "facil" | "intermedia" | "dificil"
    juego.iniciar_juego(dificultad=nivel)
    return redirect(url_for('jugar'))


@app.route('/jugar')
def jugar():
    return render_template(
        'juego.html',
        palabra_a_mostrar=" ".join(juego.palabra_a_mostrar),
        pista=juego.pista,
        intentos=juego.intentos_restantes,
        letras_usadas=", ".join(juego.letras_usadas),
        juego_finalizado=juego.juego_finalizado,
        estado=juego.estado,
        palabra_secreta=juego.palabra_a_adivinar if juego.juego_finalizado else ""
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
    return redirect(url_for('elegir_dificultad'))


if __name__ == '__main__':
    app.run(debug=True)
