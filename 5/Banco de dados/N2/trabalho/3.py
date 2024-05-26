import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#3 – Nomes dos médicos de especialidade PEDIATRIA
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome
FROM medico m 
JOIN formacao f ON (m.med_crm = f.med_crm)
JOIN especialidade e ON (e.esp_cod = f.esp_cod)
WHERE e.esp_nome = 'Pediatria';         
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Médico'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()