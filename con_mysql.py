import pymysql
import datetime

def conecta_db():
    con = pymysql.connect(
        host='192.168.1.77', 
        db='ac_nova', user='root', 
        passwd='wo!P@A5n')

    return con

def cadastra_dado(valor):
  con = conecta_db()
  cursor = con.cursor()
  data_atual = datetime.now()
  print(str(data_atual)[:16])
  cursor.execute("UPDATE op_teste SET vl_teste={}, teste_clp={} WHERE status='testando' AND linha='A'".format(valor, 2))
  con.commit()
  print('Registro salvo com sucesso.')
  print('___________________________________')
  con.close()

cadastra_dado()