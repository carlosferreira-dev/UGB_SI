import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#25 - Nome dos medicamentos que todos os pacientes podem tomar. 
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT mdc_nome
FROM medicamento
WHERE mdc_cod NOT IN (SELECT mdc_cod FROM efeito_colateral);
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Medicamento'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()