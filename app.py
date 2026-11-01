from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from supabase import create_client

from basic_agent_basic_memory_intermediate_tools import (
    process_response,
    client,
    memory
)
load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SECRET_KEY")



supabase = create_client(
    supabase_url,
    supabase_key
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

    try:
        supabase.table("consultas").insert({
            "pregunta": pregunta,
            "respuesta": respuesta
        }).execute()

    except Exception as e:
        print(f"Error al guardar en Supabase: {e}")

    return jsonify({
        "respuesta": respuesta
    })


if __name__ == "__main__":
    app.run(debug=True)