#######################
# Agente Basico De IA #
# Herramientas        #
#######################

# Importacion para el manejo de sistema
import requests


class IntermediateTools:

    def __init__(self):
        pass


    # --------------------------------------------------
    # HERRAMIENTA 1
    # Consultar tipo de cambio
    # API: Exchange Rate API
    # --------------------------------------------------

    def consultar_tipo_cambio_api(self, moneda: str):

        print(
            f"Herramienta consultar_tipo_cambio_api "
            f"llamada con moneda: {moneda}"
        )

        if not moneda:
            return "Error: Se requiere el código de la moneda."

        url = (
            f"https://open.er-api.com/v6/latest/"
            f"{moneda.upper()}"
        )

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            datos = response.json()

            # Obtener únicamente el cambio hacia quetzales
            if "rates" in datos and "GTQ" in datos["rates"]:

                return {
                    "moneda_origen": moneda.upper(),
                    "moneda_destino": "GTQ",
                    "tipo_cambio": datos["rates"]["GTQ"]
                }

            return "ERROR: No se encontró el tipo de cambio."

        except Exception as e:

            print(
                f"Error al consultar tipo de cambio: {e}"
            )

            return (
                f"ERROR: No se pudo obtener el tipo "
                f"de cambio para {moneda}"
            )


    # --------------------------------------------------
    # HERRAMIENTA 2
    # Producto Interno Bruto
    # API: Banco Mundial
    # --------------------------------------------------

    def obtener_pib_api(
        self,
        pais: str,
        anio_inicio: str,
        anio_fin: str
    ):

        print(
            f"Herramienta obtener_pib_api llamada "
            f"con pais: {pais}"
        )

        indicador = "NY.GDP.MKTP.CD"

        url = (
            f"https://api.worldbank.org/v2/country/"
            f"{pais}/indicator/{indicador}"
            f"?date={anio_inicio}:{anio_fin}"
            f"&format=json&per_page=100"
        )

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(f"Error al obtener PIB: {e}")

            return (
                f"ERROR: No se pudo obtener el PIB "
                f"para {pais}"
            )


    # --------------------------------------------------
    # HERRAMIENTA 3
    # PIB per capita
    # API: Banco Mundial
    # --------------------------------------------------

    def obtener_pib_per_capita_api(
        self,
        pais: str,
        anio_inicio: str,
        anio_fin: str
    ):

        print(
            f"Herramienta obtener_pib_per_capita_api "
            f"llamada con pais: {pais}"
        )

        indicador = "NY.GDP.PCAP.CD"

        url = (
            f"https://api.worldbank.org/v2/country/"
            f"{pais}/indicator/{indicador}"
            f"?date={anio_inicio}:{anio_fin}"
            f"&format=json&per_page=100"
        )

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(f"Error al obtener PIB per capita: {e}")

            return (
                f"ERROR: No se pudo obtener el PIB "
                f"per capita para {pais}"
            )


    # --------------------------------------------------
    # HERRAMIENTA 4
    # Inflación
    # API: Banco Mundial
    # --------------------------------------------------

    def obtener_inflacion_api(
        self,
        pais: str,
        anio_inicio: str,
        anio_fin: str
    ):

        print(
            f"Herramienta obtener_inflacion_api "
            f"llamada con pais: {pais}"
        )

        indicador = "FP.CPI.TOTL.ZG"

        url = (
            f"https://api.worldbank.org/v2/country/"
            f"{pais}/indicator/{indicador}"
            f"?date={anio_inicio}:{anio_fin}"
            f"&format=json&per_page=100"
        )

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(f"Error al obtener inflación: {e}")

            return (
                f"ERROR: No se pudo obtener la inflación "
                f"para {pais}"
            )


    # --------------------------------------------------
    # HERRAMIENTA 5
    # Deuda pública como porcentaje del PIB
    # API: Banco Mundial
    # --------------------------------------------------

    def obtener_deuda_publica_api(
        self,
        pais: str,
        anio_inicio: str,
        anio_fin: str
    ):

        print(
            f"Herramienta obtener_deuda_publica_api "
            f"llamada con pais: {pais}"
        )

        indicador = "GC.DOD.TOTL.GD.ZS"

        url = (
            f"https://api.worldbank.org/v2/country/"
            f"{pais}/indicator/{indicador}"
            f"?date={anio_inicio}:{anio_fin}"
            f"&format=json&per_page=100"
        )

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(f"Error al obtener deuda pública: {e}")

            return (
                f"ERROR: No se pudo obtener la deuda "
                f"pública para {pais}"
            )


    # --------------------------------------------------
    # HERRAMIENTA 6
    # Crecimiento anual del PIB
    # API: Banco Mundial
    # --------------------------------------------------

    def obtener_crecimiento_pib_api(
        self,
        pais: str,
        anio_inicio: str,
        anio_fin: str
    ):

        print(
            f"Herramienta obtener_crecimiento_pib_api "
            f"llamada con pais: {pais}"
        )

        indicador = "NY.GDP.MKTP.KD.ZG"

        url = (
            f"https://api.worldbank.org/v2/country/"
            f"{pais}/indicator/{indicador}"
            f"?date={anio_inicio}:{anio_fin}"
            f"&format=json&per_page=100"
        )

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(f"Error al obtener crecimiento del PIB: {e}")

            return (
                f"ERROR: No se pudo obtener el crecimiento "
                f"del PIB para {pais}"
            )
                # --------------------------------------------------
    # HERRAMIENTA 7
    # Balanza comercial bilateral
    # API: UN Comtrade
    # --------------------------------------------------

    def obtener_balanza_comercial_bilateral_api(
        self,
        pais_reportante: str,
        pais_socio: str,
        anio_inicio: str,
        anio_fin: str
    ):

        print(
            f"Herramienta obtener_balanza_comercial_bilateral_api "
            f"llamada con {pais_reportante} y {pais_socio}"
        )

        try:

            # Obtener códigos numéricos M49 a partir de códigos ISO3
            url_paises = (
                "https://comtradeapi.un.org/files/v1/app/"
                "reference/partnerAreas.json"
            )

            response_paises = requests.get(
                url_paises,
                timeout=30
            )

            response_paises.raise_for_status()

            lista_paises = response_paises.json().get(
                "results",
                []
            )

            def buscar_codigo_m49(codigo_iso3):

                codigo_iso3 = codigo_iso3.upper().strip()

                for pais in lista_paises:

                    iso3 = str(
                        pais.get(
                            "PartnerCodeIsoAlpha3",
                            ""
                        )
                    ).strip().upper()

                    if iso3 == codigo_iso3:
                        return pais.get("PartnerCode")

                return None

            codigo_reportante = buscar_codigo_m49(
                pais_reportante
            )

            codigo_socio = buscar_codigo_m49(
                pais_socio
            )

            if codigo_reportante is None:
                return (
                    f"ERROR: No se encontró el país "
                    f"{pais_reportante}"
                )

            if codigo_socio is None:
                return (
                    f"ERROR: No se encontró el país "
                    f"{pais_socio}"
                )

            inicio = int(anio_inicio)
            fin = int(anio_fin)

            resultados = []

            for anio in range(inicio, fin + 1):

                url = (
                    "https://comtradeapi.un.org/"
                    "public/v1/preview/C/A/HS"
                )

                parametros = {
                    "reporterCode": codigo_reportante,
                    "partnerCode": codigo_socio,
                    "period": str(anio),
                    "cmdCode": "TOTAL",
                    "flowCode": "X,M",
                    "maxRecords": 500
                }

                response = requests.get(
                    url,
                    params=parametros,
                    timeout=30
                )

                response.raise_for_status()

                datos = response.json().get(
                    "data",
                    []
                )

                exportaciones = None
                importaciones = None

                for registro in datos:

                    flujo = registro.get("flowCode")
                    valor = registro.get("primaryValue")

                    if valor is None:
                        continue

                    valor = float(valor)

                    if flujo == "X":

                        if exportaciones is None:
                            exportaciones = 0

                        exportaciones += valor

                    elif flujo == "M":

                        if importaciones is None:
                            importaciones = 0

                        importaciones += valor

                if (
                    exportaciones is not None
                    and importaciones is not None
                ):
                    balanza = (
                        exportaciones - importaciones
                    )
                else:
                    balanza = None

                resultados.append({
                    "anio": str(anio),
                    "exportaciones_usd": exportaciones,
                    "importaciones_usd": importaciones,
                    "balanza_comercial_usd": balanza
                })

            return {
                "pais_reportante": pais_reportante.upper(),
                "pais_socio": pais_socio.upper(),
                "resultados": resultados
            }

        except Exception as e:

            print(
                f"Error al obtener balanza comercial: {e}"
            )

            return (
                "ERROR: No se pudo obtener la "
                "balanza comercial bilateral."
            )