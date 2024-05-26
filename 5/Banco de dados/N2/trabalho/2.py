import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#2 – Nome dos pacientes e dos médicos das consultas do dia 19/02/2024
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT p.pac_nome, m.med_nome
FROM paciente p
JOIN consulta c ON (p.pac_mat = c.pac_mat)
JOIN medico m ON (m.med_crm = c.med_crm)
WHERE c.con_data = '2024-02-19';       
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente', 'Nome Médico'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()