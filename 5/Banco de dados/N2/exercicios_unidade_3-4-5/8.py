import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#8 - Obter a matrícula e o nome de todos os alunos matriculados em cursos da área TECNOLÓGICA, acompanhados do nome do curso, em ordem de matrícula.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_mat,
        a.alu_nome,
        c.cur_nome
FROM aluno a
JOIN curso c ON (a.cur_cod = c.cur_cod)
JOIN area a ON (a.are_cod = c.are_cod)
WHERE a.are_nome = 'Tecnologica'
ORDER BY a.alu_mat
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matrícula', 'Nome', 'Curso'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()