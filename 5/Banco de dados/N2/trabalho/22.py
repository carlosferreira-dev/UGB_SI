import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#22 - Nome dos médicos que receitaram algum medicamento que causa URTICÁRIA.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.med_nome
FROM medico m
JOIN consulta c ON (m.med_crm = c.med_crm)
JOIN receita r ON (c.con_num = r.con_num)
JOIN medicamento md ON (r.mdc_cod = md.mdc_cod)
JOIN efeito_colateral e ON (md.mdc_cod = e.mdc_cod)
JOIN sintoma s ON (e.sin_cod = s.sin_cod)
WHERE s.sin_nome = 'Urticaria';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Medico'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()