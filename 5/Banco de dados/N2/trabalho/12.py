import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#12 - Nome dos laboratórios que tiveram medicamentos seus receitados em 01/03/2024
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT l.lab_nome
FROM medicamento m 
JOIN receita r ON (m.mdc_cod = r.mdc_cod)
JOIN laboratorio l ON (l.lab_cod = m.lab_cod)
JOIN consulta c ON (r.con_num = c.con_num)
WHERE c.con_data = '2024-03-01';
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Laboratório'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()