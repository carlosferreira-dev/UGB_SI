import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#5 – Nome de cada medicamento acompanhado do nome do seu laboratório
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.mdc_nome, l.lab_nome
FROM medicamento m 
JOIN laboratorio l ON (l.lab_cod = m.lab_cod);           
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Medicamento', 'Nome Laboratório'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()