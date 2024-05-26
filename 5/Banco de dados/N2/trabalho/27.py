import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#27 - Nome dos médicos que não atenderam na sala 20 em 18/02/2024.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome
FROM medico m
JOIN consulta c ON (m.med_crm = c.med_crm)
WHERE c.con_data = '2024-02-18'
AND c.con_num_sala != '20';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Medico'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()