import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#20 - Nome dos pacientes que não podem tomar PARACETAMOL.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT p.pac_nome
FROM paciente p
JOIN contra_indicacao c ON (p.pac_mat = c.pac_mat)
JOIN medicamento m ON (c.mdc_cod = m.mdc_cod)
WHERE m.mdc_nome = 'Paracetamol';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()