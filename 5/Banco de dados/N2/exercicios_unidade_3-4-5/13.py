import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#13 - Obter a matrícula, o nome e a média em CÁLCULO III de todos os alunos cuja média foi superior à média geral desta disciplina.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_mat,
        a.alu_nome,
        av.ava_media
FROM aluno a
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
WHERE d.dis_nome = 'Calculo III'
GROUP BY a.alu_mat
HAVING av.ava_media > AVG(av.ava_media)
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matrícula', 'Nome', 'Média'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()