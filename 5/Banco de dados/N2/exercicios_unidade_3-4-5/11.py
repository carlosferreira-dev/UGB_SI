import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#11 - Obter a matrícula e o nome dos alunos que não fizeram nenhuma avaliação no 1º bimestre.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT alu_mat,
        alu_nome
FROM aluno
WHERE alu_mat NOT IN (SELECT alu_mat 
                                FROM
                                avaliacao
                                WHERE ava_bim = 1)
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matricula', 'Nome', 'Bimestre'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()