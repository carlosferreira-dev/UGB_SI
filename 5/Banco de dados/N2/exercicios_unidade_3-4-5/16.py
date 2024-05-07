import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#16 - Obter a matrícula e o nome de todos os alunos do 1º ano de ENGENHARIA MECÂNICA
# que tiveram no 1º bimestre avaliação em  MATEMÁTICA I e em FÍSICA I.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT 
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Matrícula', 'Nome', 'Média'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()