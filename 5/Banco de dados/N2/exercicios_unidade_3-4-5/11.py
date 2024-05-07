import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#11 - Obter a matrícula e o nome dos alunos que não fizeram nenhuma avaliação no 1º bimestre.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_mat,
        a.alu_nome,
        av.ava_bim
FROM aluno a
LEFT JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
WHERE av.ava_bim != 1
GROUP BY a.alu_mat
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matricula', 'Nome', 'Bimestre'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()