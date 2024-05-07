import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#3 - Obter o nome de cada aluno acompanhado das suas médias bimestre a bimestre em cada disciplina,
# ordenado por código da disciplina.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_nome,
    d.dis_nome,
    av.ava_bim,
    av.ava_media,
    d.dis_cod
FROM aluno a
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
ORDER BY d.dis_cod
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome', 'Disciplina','Bimestre', 'Média', 'Código disciplina'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()