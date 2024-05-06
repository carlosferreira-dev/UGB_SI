import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate

#2 - Obter o nome dos alunos do 2º ano de ENGENHARIA CIVIL que ficaram com média inferior a 5,0 
#em alguma disciplina, acompanhado do nome da disciplina e da média obtida.

conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT DISTINCT(a.alu_nome),
    d.dis_nome,
    av.ava_media,
    av.ava_bim
FROM aluno a
JOIN avaliacao av ON (a.alu_mat = av.alu_mat)
JOIN curso c ON (a.cur_cod = c.cur_cod)
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
JOIN grade g ON (d.dis_cod = g.dis_cod)
WHERE c.cur_nome = 'Engenharia Civil'
    AND av.ava_media < 5.0
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome', 'Disciplina','Média', 'Bimestre'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()