from flask import Flask, render_template, request, jsonify

from basic_agent_basic_memory_intermediate_tools import (
    process_response,
    client,
    memory
)

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/preguntar", methods=["POST"])
def preguntar():

    datos = request.get_json()
    pregunta = datos.get("mensaje", "")

    if not pregunta:
        return jsonify({
            "respuesta": "Escribe una pregunta."
        })

    respuesta = process_response(
        client,
        memory.messages(),
        pregunta
    )

    memory.add("user", pregunta)
    memory.add("assistant", respuesta)

    return jsonify({
        "respuesta": respuesta
    })


if __name__ == "__main__":
    app.run(debug=True)