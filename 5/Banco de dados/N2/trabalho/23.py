import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#23 - Nome dos medicamentos que podem causar FEBRE, acompanhados do nome de seus respectivos laboratórios.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.mdc_nome, l.lab_nome
FROM medicamento m
JOIN efeito_colateral e ON (m.mdc_cod = e.mdc_cod)
JOIN sintoma s ON (s.sin_cod = e.sin_cod)
JOIN laboratorio l ON (m.lab_cod = l.lab_cod)
WHERE s.sin_nome = 'Febre';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Medicamento', 'Laboratorio'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()