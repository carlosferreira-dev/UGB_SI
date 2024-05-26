import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#24 - Nome das especialidades que não possuem nenhum médico habilitado.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT esp_nome
FROM especialidade
WHERE esp_cod NOT IN (SELECT esp_cod FROM formacao);
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Especialidade'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()