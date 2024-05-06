import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate

#1 - Obter o nome de todos os cursos (alfabeticamente) e a matrícula, 
#o nome e a série de seus alunos (por ordem de matrícula).

conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT c.cur_nome,
        a.alu_mat,
        a.alu_nome,
        a.alu_serie
FROM curso c
JOIN aluno a ON (c.cur_cod = a.cur_cod)
ORDER BY a.alu_mat, c.cur_nome
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Curso', 'Matricula', 'Nome', 'Serie'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()