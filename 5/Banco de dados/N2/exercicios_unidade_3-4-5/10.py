import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#10 - Obter a média geral da disciplina FÍSICA II do curso de ENGENHARIA MECÂNICA no 1º bimestre
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT avg(av.ava_media)
FROM avaliacao av
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
JOIN grade g ON (g.dis_cod = d.dis_cod)
JOIN curso c ON (g.cur_cod = c.cur_cod)
WHERE d.dis_nome = 'Fisica II'
    AND c.cur_nome = 'Engenharia Mecanica'
    AND av.ava_bim = 1
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Média Geral'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()