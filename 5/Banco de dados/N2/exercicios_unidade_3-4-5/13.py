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
        AVG(av.ava_media)
FROM aluno a
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
WHERE d.dis_nome = 'Calculo III'
GROUP BY a.alu_mat
HAVING AVG(av.ava_media) > (SELECT AVG(ava_media)
                                FROM avaliacao av
                                JOIN disciplina d ON (av.dis_cod = d.dis_cod)
                                WHERE dis_nome = 'Calculo III')
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matrícula', 'Nome', 'Média'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()