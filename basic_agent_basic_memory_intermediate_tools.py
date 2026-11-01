#######################
# Agente Basico De IA #
# Agente              #
#######################

# Importacion para el ambiente
from dotenv import load_dotenv

# Importacion para el LLM
from groq import Groq

# Importacion para el manejo de sistema
import os

# Importacion para el uso de formato JSON
import json

# Importacion para el manejo de fechas y zonas horarias
from datetime import datetime
from zoneinfo import ZoneInfo

# Importacion para el manejo memoria y herramientas#
from basic_memory import BasicMemory
from intermediate_tools import IntermediateTools



# Cargar variables de entorno #
load_dotenv()

# Inicializar el cliente de Groq con la clave de API
api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Captura la hora actual en la zona horaria de Guatemala
now = datetime.now(ZoneInfo("America/Guatemala"))

# Inicializar herramientas y memoria #
MEMORY_MAX_MESSAGES = 10
memory = BasicMemory(max_messages=MEMORY_MAX_MESSAGES)


SYSTEM_PROMPT = f"""
Eres un agente económico que habla en español.

Tu objetivo es ayudar al usuario a consultar, analizar y comparar información
macroeconómica de distintos países utilizando datos obtenidos mediante APIs.

Cuentas con las siguientes herramientas:

- consultar_tipo_cambio_api:
  Consulta el tipo de cambio de una moneda respecto al quetzal de Guatemala.

- obtener_pib_api:
  Consulta el Producto Interno Bruto (PIB) de un país.

- obtener_pib_per_capita_api:
  Consulta el PIB per cápita de un país.

- obtener_inflacion_api:
  Consulta la inflación anual de un país.

- obtener_deuda_publica_api:
  Consulta la deuda pública como porcentaje del PIB.

- obtener_crecimiento_pib_api:
  Consulta el crecimiento anual del PIB.

Para utilizar las herramientas del Banco Mundial debes utilizar códigos ISO3.

Ejemplos:
Guatemala = GTM
Estados Unidos = USA
México = MEX
Costa Rica = CRI
El Salvador = SLV
Honduras = HND
Panamá = PAN

Si el usuario proporciona el nombre de un país,
convierte automáticamente el nombre al código ISO3 correspondiente.

Cuando el usuario solicite varios indicadores,
utiliza todas las herramientas necesarias.

Cuando se comparen varios países o varios años,
presenta los resultados de manera ordenada, preferiblemente en una tabla.

Después de presentar los datos,
da una explicación económica breve y clara.

No generes gráficos mediante URLs, QuickChart, Markdown ni servicios externos.
Cuando el usuario solicite una gráfica, entrega los datos en una tabla con la primera columna "Año".
La interfaz web se encargará automáticamente de generar la gráfica a partir de la tabla.

No inventes datos económicos.
Utiliza los datos obtenidos mediante las APIs.
"""

TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "consultar_tipo_cambio_api",
            "description": (
                "Consulta el tipo de cambio de una moneda "
                "respecto al quetzal de Guatemala."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "moneda": {
                        "type": "string",
                        "description": (
                            "Codigo de moneda, por ejemplo USD, EUR o MXN"
                        )
                    }
                },
                "required": ["moneda"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "obtener_pib_api",
            "description": (
                "Consulta el Producto Interno Bruto PIB de un pais "
                "para un rango de años."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pais": {
                        "type": "string",
                        "description": (
                            "Codigo ISO3 del pais, por ejemplo GTM, USA o MEX"
                        )
                    },
                    "anio_inicio": {
                        "type": "string",
                        "description": (
                            "Año inicial de la consulta, por ejemplo 2020"
                        )
                    },
                    "anio_fin": {
                        "type": "string",
                        "description": (
                            "Año final de la consulta, por ejemplo 2024"
                        )
                    }
                },
                "required": [
                    "pais",
                    "anio_inicio",
                    "anio_fin"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "obtener_pib_per_capita_api",
            "description": (
                "Consulta el PIB per capita de un pais "
                "para un rango de años."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pais": {
                        "type": "string",
                        "description": "Codigo ISO3 del pais"
                    },
                    "anio_inicio": {
                        "type": "string",
                        "description": "Año inicial"
                    },
                    "anio_fin": {
                        "type": "string",
                        "description": "Año final"
                    }
                },
                "required": [
                    "pais",
                    "anio_inicio",
                    "anio_fin"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "obtener_inflacion_api",
            "description": (
                "Consulta la tasa de inflacion anual de un pais "
                "para un rango de años."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pais": {
                        "type": "string",
                        "description": "Codigo ISO3 del pais"
                    },
                    "anio_inicio": {
                        "type": "string",
                        "description": "Año inicial"
                    },
                    "anio_fin": {
                        "type": "string",
                        "description": "Año final"
                    }
                },
                "required": [
                    "pais",
                    "anio_inicio",
                    "anio_fin"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "obtener_deuda_publica_api",
            "description": (
                "Consulta la deuda publica como porcentaje del PIB "
                "de un pais para un rango de años."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pais": {
                        "type": "string",
                        "description": "Codigo ISO3 del pais"
                    },
                    "anio_inicio": {
                        "type": "string",
                        "description": "Año inicial"
                    },
                    "anio_fin": {
                        "type": "string",
                        "description": "Año final"
                    }
                },
                "required": [
                    "pais",
                    "anio_inicio",
                    "anio_fin"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "obtener_crecimiento_pib_api",
            "description": (
                "Consulta el crecimiento anual del PIB de un pais "
                "para un rango de años."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pais": {
                        "type": "string",
                        "description": "Codigo ISO3 del pais"
                    },
                    "anio_inicio": {
                        "type": "string",
                        "description": "Año inicial"
                    },
                    "anio_fin": {
                        "type": "string",
                        "description": "Año final"
                    }
                },
                "required": [
                    "pais",
                    "anio_inicio",
                    "anio_fin"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "obtener_balanza_comercial_bilateral_api",
            "description": (
                "Obtiene la balanza comercial bilateral entre dos países "
                "para un rango de años. Devuelve exportaciones, importaciones "
                "y balanza comercial en dólares."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pais_reportante": {
                        "type": "string",
                        "description": (
                            "Código ISO3 del país desde cuya perspectiva "
                            "se analiza la balanza comercial. Ejemplo: GTM."
                        )
                    },
                    "pais_socio": {
                        "type": "string",
                        "description": (
                            "Código ISO3 del país socio comercial. "
                            "Ejemplo: SLV."
                        )
                    },
                    "anio_inicio": {
                        "type": "string",
                        "description": "Año inicial de la consulta."
                    },
                    "anio_fin": {
                        "type": "string",
                        "description": "Año final de la consulta."
                    }
                },
                "required": [
                    "pais_reportante",
                    "pais_socio",
                    "anio_inicio",
                    "anio_fin"
                ]
            }
        }
    }

]


print("Agente Basico De IA")


def process_response(
    client: Groq,
    memory_messages: list[dict],
    user_text: str
):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(memory_messages)

    messages.append({
        "role": "user",
        "content": user_text
    })

    while True:

        resp = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=TOOLS
        )

        msg = resp.choices[0].message

        # Si no hay llamados a herramientas,
        # regresamos la respuesta final
        if not getattr(msg, "tool_calls", None):
            return msg.content or ""

        messages.append({
            "role": "assistant",
            "content": msg.content or "",
            "tool_calls": [
                tc.model_dump()
                for tc in msg.tool_calls
            ]
        })

        for tool_call in msg.tool_calls:

            name = tool_call.function.name

            args = json.loads(
                tool_call.function.arguments or "{}"
            )

            # Si el usuario no indica años,
            # usamos 2020-2024 por defecto
            if name != "consultar_tipo_cambio_api":
                args.setdefault(
                    "anio_inicio",
                    "2020"
                )

                args.setdefault(
                    "anio_fin",
                    "2024"
                )

            tools = IntermediateTools()

            if name == "consultar_tipo_cambio_api":

                result = tools.consultar_tipo_cambio_api(
                    moneda=args["moneda"]
                )

            elif name == "obtener_pib_api":

                result = tools.obtener_pib_api(
                    pais=args["pais"],
                    anio_inicio=args["anio_inicio"],
                    anio_fin=args["anio_fin"]
                )

            elif name == "obtener_pib_per_capita_api":

                result = tools.obtener_pib_per_capita_api(
                    pais=args["pais"],
                    anio_inicio=args["anio_inicio"],
                    anio_fin=args["anio_fin"]
                )

            elif name == "obtener_inflacion_api":

                result = tools.obtener_inflacion_api(
                    pais=args["pais"],
                    anio_inicio=args["anio_inicio"],
                    anio_fin=args["anio_fin"]
                )

            elif name == "obtener_deuda_publica_api":

                result = tools.obtener_deuda_publica_api(
                    pais=args["pais"],
                    anio_inicio=args["anio_inicio"],
                    anio_fin=args["anio_fin"]
                )

            elif name == "obtener_crecimiento_pib_api":

                result = tools.obtener_crecimiento_pib_api(
                    pais=args["pais"],
                    anio_inicio=args["anio_inicio"],
                    anio_fin=args["anio_fin"]
                )

            elif name == "obtener_balanza_comercial_bilateral_api":

                result = (
                    tools.obtener_balanza_comercial_bilateral_api(
                        pais_reportante=args["pais_reportante"],
                        pais_socio=args["pais_socio"],
                        anio_inicio=args["anio_inicio"],
                        anio_fin=args["anio_fin"]
                    )
                )

            else:

                print(
                    f"Se intentó llamar a una "
                    f"herramienta desconocida {name}"
                )

                result = {
                    "error": (
                        f"Herramienta desconocida: {name}"
                    )
                }

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(
                    result,
                    ensure_ascii=False
                )
            })


if __name__ == "__main__":

    while True:

        user_text = input(
            "Tú: "
        ).strip()

        if not user_text:
            continue

        if user_text.lower() in (
            "exit",
            "salir"
        ):
            print("Hasta luego!")
            break

        assistant_text = process_response(
            client,
            memory.messages(),
            user_text
        )

        print(
            f"Agente: {assistant_text}"
        )

        memory.add(
            "user",
            user_text
        )

        memory.add(
            "assistant",
            assistant_text
        )