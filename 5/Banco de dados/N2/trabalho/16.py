import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#16 - Nome dos medicamentos que causam FEBRE ou GASTRITE. 
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT DISTINCT(m.mdc_nome)
FROM medicamento m
JOIN efeito_colateral e ON (m.mdc_cod = e.mdc_cod)
JOIN sintoma s ON (s.sin_cod = e.sin_cod)
WHERE s.sin_nome = 'Febre' OR s.sin_nome = 'Gastrite';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Medicamento'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()