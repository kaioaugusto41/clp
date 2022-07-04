from pyModbusTCP.client import ModbusClient
import time
from datetime import datetime

while True:
    c = ModbusClient(host="10.180.1.250", port=502, timeout=2, unit_id=255)
    if not c.open():
        print('Não foi possível obter o status da linha')
        
    if c.is_open():
        status_linha = c.read_coils(40008, 1)
        if status_linha:
            if status_linha[0] == True:
                while status_linha[0] == True:
                    print('Testando...')
                    time.sleep(1)
                    status_linha = c.read_coils(40008, 1)
                    if status_linha[0] == False:
                        break
                print('TESTADO')
            elif status_linha[0] == False:
                print('Ociosa...')
                status_linha = 'Ociosa'
        else:
            print('Não foi possível obter o status da linha')

    time.sleep(2)
    

    

 
