import sys
import ipaddress

def prefijo_a_mascara(prefijo):
    try:
        if prefijo.startswith('/'):
            prefijo = prefijo[1:]

        prefijo = int(prefijo)

        if not (0 <= prefijo <= 32):
            raise ValueError("El prefijo debe estar entre 0 y 32")

        red = ipaddress.IPv4Network(f'0.0.0.0/{prefijo}')
        return red.netmask
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python3 subnetmask.py <prefijo>  (ej: /25 o 25)")
    else:
        entrada = sys.argv[1]
        mascara = prefijo_a_mascara(entrada)
        print(f"Máscara de subred para {entrada}: {mascara}")
