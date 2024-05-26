import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#14 - Nome dos pacientes que cancelaram consultas no mês de fevereiro de 2024
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT p.pac_nome
FROM paciente p 
JOIN consulta c ON (p.pac_mat = c.pac_mat)
WHERE c.con_data BETWEEN '2024-02-01' and '2024-02-29'
AND c.con_situac = 'C';
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()