import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#17 - Obter a matrícula e o nome de todos os alunos do 1º ano de ENGENHARIA MECÂNICA 
#que tiveram no 1º bimestre avaliação em  MATEMÁTICA I ou em FÍSICA I.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT DISTINCT(a.alu_mat),
        a.alu_nome
FROM aluno a
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
JOIN curso c ON (a.cur_cod = c.cur_cod)
WHERE c.cur_nome = 'Engenharia Mecanica'
        AND av.ava_bim = 1
        AND (d.dis_nome = 'Matematica I' OR d.dis_nome = 'Fisica I')
        AND a.alu_serie = 1
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matrícula', 'Nome', 'Média'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()