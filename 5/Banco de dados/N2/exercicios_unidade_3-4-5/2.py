import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate

#2 - Obter o nome de todas as disciplinas da 2ª série do curso de MEDICINA.

conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT d.dis_nome
FROM disciplina d
JOIN grade g ON (d.dis_cod = g.dis_cod)
JOIN curso c ON (g.cur_cod = c.cur_cod)
WHERE c.cur_nome = 'Medicina'
    AND g.gra_serie = 2
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Disciplina'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()