import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#4 – Nome dos pacientes que receberam receita do medicamento AMOXIL e quantidade receitada
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT p.pac_nome, r.rec_quant
FROM paciente p
JOIN consulta c ON (p.pac_mat = c.pac_mat)
JOIN receita r ON (r.con_num = c.con_num)
JOIN medicamento m ON (m.mdc_cod = r.mdc_cod)
WHERE m.mdc_nome = 'Amoxil';          
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente', 'Quantidade receitada'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()