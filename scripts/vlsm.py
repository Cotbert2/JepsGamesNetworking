import ipaddress
import math
import pandas as pd

def calcular_subredes(ip_base, hosts_por_subred):
    hosts_ordenados = sorted(hosts_por_subred, reverse=True)
    red_actual = ipaddress.IPv4Network(ip_base, strict=False)
    resultado = []

    for i, hosts in enumerate(hosts_ordenados):
        bits_necesarios = math.ceil(math.log2(hosts + 2))
        prefijo = 32 - bits_necesarios

        subred = ipaddress.ip_network((red_actual.network_address, prefijo), strict=False)
        gateway = list(subred.hosts())[0]
        broadcast = subred.broadcast_address
        mascara_decimal = subred.netmask  

        resultado.append({
            'Subred': f'Red {i+1}',
            'IP de red': str(subred.network_address),
            'Prefijo': f'/{subred.prefixlen}',
            'Máscara': str(mascara_decimal), 
            'Gateway': str(gateway),
            'Broadcast': str(broadcast),
            'Número de Hosts': hosts
        })

        siguiente_red = int(subred.network_address) + subred.num_addresses
        red_actual = ipaddress.ip_network((siguiente_red, 32), strict=False)

    return resultado

ip_base = '9.9.9.0/24'

# Game design : 50
# Game development : 30
# sales : 20
# marketing : 10
#datacenter : 4
# IT : 4


#Matriz
# hosts = [50,30, 20, 10, 4, 4,2]

#New york
hosts = [2 , 2, 2, 2, 2, 2, 2 ,2 ,2 ,2 ,2 ,2 ]

#Montreal

# hosts = [ 70, 20,10 ]

subredes = calcular_subredes(ip_base, hosts)

df = pd.DataFrame(subredes)
print(df.to_string(index=False))
