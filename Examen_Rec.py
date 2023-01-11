import csv
nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
            "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
            "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
            "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}

countries_dict = {"30": "Grecia", "33": "Francia", "34":"España", "351": "Portugal",
                  "380": "Ucrania", "39": "Italia", "41": "Suiza", "44": "Reino Unido",
                  "49": "Alemania", "7": "Rusia"}

def check_username(persona):
    """ Esta funcion comprueba y corrige si el formato del nombre o del
    apellido no estan en formato capitalizado.
    Parametros:
        - Persona: Es un str que constara del nombre o apellido
    Salida:
        - Un str corregido en formato capitalizado.
    """
    return persona.title()
def check_nif(num_nif):
    """ Esta funcion corrige la letra asociada al resto del numero nif
    Parametros:
        - num_nif: es un valor str que su formato es de 8 numeros y una letra.
    Salida:
        - Un str con el nif corregido
    """
    resto = int(num_nif[0:8]) % 23
    return print(num_nif[0:8] + nif_dict.get(str(resto)))

def check_phone(num_tel):
    """ Esta funcion chequea e identifica si el numero esta bien escrito y a que pais corresponde.
    Parametros:
        - num_tel: Es un valor str con un numero telefonico con formato "(XYZ)ABC-DEFGHI"
    Salida:
        - pais: variable str que correspondera al pais consultado en el diccionario
        - telefono: variable str, que sera el numero de telefono reformateado correctamente.
    """
    list_tel = [num_tel[:-10], num_tel[-10:]]
    prefijo = list_tel[0][1:-1]
    pais = countries_dict.get(str(prefijo))
    num_sep = list_tel[1].split("-")
    numero = num_sep[0] + num_sep[1]
    telefono = prefijo + "-" + numero
    return telefono, pais
def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """ Esta funcion suma la cantidad de multas y devuelve el pago total
    Parametros:
        - multas_radar: numero tipo int
        - multas_ITV: numero tipo int
        - multas_estupefacientes: numero tipo int
    Salida:
        - La suma de los numeros, variable tipo int.
    """
    return int(multas_radar + multas_ITV + multas_estupefacientes)

def check_DGT():
    """ Esta funcion abrira un fichero de texto, comprobaara los datos llamando a las otras funciones,
    despues sobreescribira los datos en el mismo fichero.
    Parametros:
        - : Una cadena str con la ruta del fichero (.csv)
    Salida:
        - El mismo fichero pero sobre-escribiendo los datos
    """
    with open("DGT.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
    return


