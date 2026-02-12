import sys

estado_inicial = "q1"
estados_aceptacion = {"q2"}

def evaluar_cadena(cadena):
    estado_actual = estado_inicial
    
    for simbolo in cadena.strip():
        if simbolo not in ["0", "1"]:
            return False
        
        if estado_actual == "q1":
            if simbolo == "0":
                estado_actual = "q2"
            elif simbolo == "1":
                estado_actual = "q3"

        elif estado_actual == "q2":
            if simbolo == "0":
                estado_actual = "q2"
            elif simbolo == "1":
                estado_actual = "q2"

        elif estado_actual == "q3":
            if simbolo == "0":
                estado_actual = "q3"
            elif simbolo == "1":
                estado_actual = "q3"
    
    return estado_actual in estados_aceptacion


def main():
    if len(sys.argv) != 2:
        print("Uso: python AFD.py entrada.txt")
        return
    
    archivo = sys.argv[1]

    try:
        with open(archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                
                if evaluar_cadena(cadena):
                    print("ACEPTA")
                else:
                    print("NO ACEPTA")
                    
    except FileNotFoundError:
        print("No se encontro el archivo")

main()

