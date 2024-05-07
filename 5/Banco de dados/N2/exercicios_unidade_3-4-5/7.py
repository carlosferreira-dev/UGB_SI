import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#7 - Obter o nome de todos os cursos da área TECNOLÓGICA, acompanhados dos nomes de suas disciplinas, série a série.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT c.cur_nome,
        d.dis_nome,
        g.gra_serie
FROM curso c
JOIN area a ON (a.are_cod = c.are_cod)
JOIN grade g ON (g.cur_cod = c.cur_cod)
JOIN disciplina d ON (d.dis_cod = g.dis_cod)
WHERE a.are_nome = 'Tecnologica'
ORDER BY g.gra_serie
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome', 'Disciplina', 'Série'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()