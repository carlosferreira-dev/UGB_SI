import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#6 - Obter o nome de todos os alunos que cursam MEDICINA ou ENFERMAGEM
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_nome
FROM aluno a
JOIN curso c ON (a.cur_cod = c.cur_cod)
WHERE c.cur_nome = 'Medicina' or c.cur_nome = 'Enfermagem'
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()