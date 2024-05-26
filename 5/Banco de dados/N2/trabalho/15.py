import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#15 - Nome dos medicamentos que causam HIPOTENSÃO.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.mdc_nome
FROM medicamento m 
JOIN efeito_colateral ef ON (ef.mdc_cod = m.mdc_cod)
JOIN sintoma s ON (s.sin_cod = ef.sin_cod)
where s.sin_nome = 'Hipotensao'; 
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Medicamento'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()