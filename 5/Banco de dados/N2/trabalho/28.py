import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#28 - Número das consultas que não geraram receita, acompanhado dos nomes do paciente e do médico.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT c.con_num, p.pac_nome, m.med_nome
FROM consulta c
JOIN paciente p ON (c.pac_mat = p.pac_mat)
JOIN medico m ON (c.med_crm = m.med_crm)
WHERE c.con_num NOT IN (SELECT con_num FROM receita);
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Número da Consulta', 'Nome Paciente', 'Nome Médico'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()