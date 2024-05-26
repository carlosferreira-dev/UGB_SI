import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#10 –Nome dos médicos que não são obstetras.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome
FROM medico m 
JOIN formacao f ON (m.med_crm = f.med_crm)
JOIN especialidade e ON (e.esp_cod = f.esp_cod)
WHERE esp_nome NOT IN ('obstetras')
GROUP BY med_nome;
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Médido'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()