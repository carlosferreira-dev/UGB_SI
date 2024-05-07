import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#9 - Obter a matrícula e o nome de todos os alunos da 1ª série do curso de ENFERMAGEM,
# que obtiveram média entre 5,0 e 7,0 no 1º bimestre na disciplina de FISIOLOGIA, com número de faltas superior a 6
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT a.alu_mat,
        a.alu_nome
FROM aluno a
JOIN curso c ON (a.cur_cod = c.cur_cod)
JOIN grade g ON (a.cur_cod = g.cur_cod)
JOIN disciplina d ON (d.dis_cod = g.dis_cod)
JOIN area a ON (a.are_cod = c.are_cod)
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
WHERE c.cur_nome = 'Enfermagem'
    AND g.gra_serie = 1
    AND av.ava_media >= 5.0 AND av.ava_media <= 7.0
    AND av.ava_bim = 1
    AND d.dis_nome = 'Fisiologia'
    AND av.ava_faltas > 6
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matrícula', 'Nome'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()