import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#5 - Obter o nome dos alunos que não tiveram nenhuma falta na disciplina MATEMÁTICA I, em nenhum bimestre.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_nome
FROM aluno a
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
WHERE d.dis_nome = 'Matematica I'
    AND av.ava_faltas = 0
GROUP BY a.alu_nome
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()