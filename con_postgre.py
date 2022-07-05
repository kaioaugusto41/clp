

import psycopg2
from datetime import datetime



def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         port='5432',
                         database='clp',
                         user='postgres', 
                         password='admin')
  return con

def cadastra_dado(valor):
  con = conecta_db()
  cursor = con.cursor()
  data_atual = datetime.now()
  print(str(data_atual)[:16])
  cursor.execute("UPDATE dados SET valor='{}', status='{}' WHERE status='testando' AND linha='A'".format(valor, 'testado'))
  con.commit()
  print('Registro salvo com sucesso.')
  print('___________________________________')
  con.close()





 
