import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#13 - Nome dos pneumologistas que não atenderam em 19/02/2024
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome
FROM medico m 
JOIN formacao f ON (m.med_crm = f.med_crm)
JOIN especialidade e ON (e.esp_cod = f.esp_cod)
JOIN consulta c ON (c.med_crm = m.med_crm)
WHERE e.esp_nome = 'Pneumologista'
and c.con_data NOT IN ('2024-02-19');
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Médico'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()