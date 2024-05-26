import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#11 – Nome dos médicos com suas respectivas especialidades
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome, e.esp_nome
FROM medico m 
JOIN formacao f ON (m.med_crm = f.med_crm)
JOIN especialidade e ON (e.esp_cod = f.esp_cod);
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Médido', 'Especialidade'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()