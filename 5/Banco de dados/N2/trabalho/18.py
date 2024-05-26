import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#18 - Nome dos medicamentos que causam HIPOTENSÃO e foram receitados em dezembro de 2023.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT m.mdc_nome
FROM medicamento m
JOIN efeito_colateral e ON (m.mdc_cod = e.mdc_cod)
JOIN sintoma s ON (s.sin_cod = e.sin_cod)
JOIN receita r ON (m.mdc_cod = r.mdc_cod)
JOIN consulta c ON (r.con_num = c.con_num)
WHERE s.sin_nome = 'Hipotensao'
AND c.con_data BETWEEN '2023-12-01' AND '2023-12-31';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Medicamento'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()