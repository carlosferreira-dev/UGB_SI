import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#8 – Nome dos médicos que não atenderam em 25/02/2024
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome
FROM medico m
JOIN consulta c ON (m.med_crm = c.med_crm)
WHERE c.con_data NOT IN (SELECT con_data = 2024-02-25 from consulta)
GROUP BY m.med_nome;               
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()