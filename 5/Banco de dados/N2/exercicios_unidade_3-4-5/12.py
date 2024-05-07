import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#12 - Obter a maior e a menor média na disciplina CÁLCULO III do curso de ENGENHARIA CIVIL no 1º bimestre
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT MAX(av.ava_media),
        MIN(av.ava_media)
FROM avaliacao av
JOIN disciplina d ON (av.dis_cod = d.dis_cod)
JOIN grade g ON (g.dis_cod = av.dis_cod)
JOIN curso c ON (g.cur_cod = c.cur_cod)
WHERE d.dis_nome = 'Calculo III'
    AND c.cur_nome = 'Engenharia Civil'
    AND av.ava_bim = 1
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Max', 'Min'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()