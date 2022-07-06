
from socket import timeout
from pymodbus.client.sync import ModbusTcpClient
import time
from con_postgre import cadastra_dado
from converte_valoes import converte_valores




while True:
    
    c = ModbusTcpClient(host='10.180.1.250', port=502, timeout=99999)                                                                # Faz a conexão com o CLP
    
    
    
    if not c.connect():                                                                                               # Se não houver conexão com o CLP...
        print('Não foi possível obter o status da linha')                                                             # Printa erro.
    
    if c.connect():                                                                                                   # Se ocorrer tudo bem na conexão...
        
        status_linha = c.read_coils(40008, 1)                                                                         # Variável do status da linha (Ociosa ou Testando)
        
        if status_linha:                                                                                              # Se houver algum valor no 'status_linha'...
            if not status_linha.isError():                                                                            # Se não ocorrer nenhum erro na leitura do valor...                                                      
                if status_linha.bits[0] == True and not status_linha.isError():                                       # Se o índice 0 do valor retornado for verdadeiro e tiver algum erro...
                    while status_linha.bits[0] == True or status_linha.isError():                                     # Enquanto o índice 0 do valor retornado for verdadeiro ou tiver algum erro...
                        print('Testando...')                                                                          # Printa "Testando"
                        time.sleep(1)                                                                                 # Pausa no código de 1 segundo.  
                        status_linha = c.read_coils(40008, 1)                                                         # Variável que atualiza o status da linha dentro do loop.                                   
                        if not status_linha.isError():                                                                # Se não tiver nenhum erro na variável do status da linha...
                            status_linha = status_linha                                                               # A variável status_linha vai receber o valor concedido anteriormente.  
                            if status_linha.bits[0] == False:                                                         # Se o índice 0 do status_linha for igual a False...
                                break                                                                                 # Para o loop
                        else:                                                                                         # Mas se tiver erro na variável status_linha...
                            print('****************************DEU ERRO MAS FOI CONTORNADO')
                            while status_linha.isError():                                                             # Enquanto houver erro na variável status_linha...
                                print('erro1')
                                status_linha = c.read_coils(40008, 1)                                                 # a variável status_linha receberá novo valor atualizado.
                                if not status_linha.isError():                                                        # Se não houver erro no novo valor...
                                    break                                                                             # Para o loop
                    print('***Testado***')                                                                            # Printa 'testando' 
                    corrente_media = c.read_holding_registers(12004, 10)                                              # Variável com a corrente média do motor.
                    if not corrente_media.isError() and converte_valores(corrente_media) != 'nan':                    # Se não tiver erro na variável corrente_media e a corrente média não for igual a 'nan'...
                        cadastra_dado(converte_valores(corrente_media))                                               # Cadastra no banco a corrente média
                    else:                                                                                             # Mas se tiver problema na variável da corrente média...
                        while True:                                                                                   # Enquanto verdadeiro...  
                            print('erro2', converte_valores(corrente_media))
                            corrente_media = c.read_holding_registers(12004, 10)                                      # Atualiza a variável corrente_media
                            if not corrente_media.isError() and converte_valores(corrente_media) != 'nan':            # Verifica novamente se não há nenhum erro na variável correte_media
                                cadastra_dado(converte_valores(corrente_media))                                       # Cadastra no banco de dados a corrente média do motor
                                break                                                                                 # Para o loop
                else:                                                                                                 # Mas se o índice 0 do valor retornado for falso...
                    print('Ociosa...')                                                                                # Printa "Ociosa"
            else:                                                                                                     # Mas se ocorrer um erro...
                print('+++++++++++++++++++++++++++++++++++++++++')                                                    # Printa uma linha qualquer para identificar que houve um erro
        else:                                                                                                         # Mas se não houver êxito na conexão com o CLP...    
            print('Não foi possível ler o registro solicitado')                                                       # Printa uma mensagem de erro
    
    c.close()                                                                                                         # Fechando a conexão com o CLP
    time.sleep(1)                                                                                                     # Espera 2 segundos antes de voltar o código do início
