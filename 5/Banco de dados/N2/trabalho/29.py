import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#29 - Nome dos laboratórios que não tiveram nenhum medicamento receitado no mês de dezembro de 2023.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT lab_nome
FROM laboratorio
WHERE lab_cod NOT in (SELECT l.lab_cod from laboratorio l
                    JOIN medicamento m ON (l.lab_cod = m.lab_cod)
                    JOIN receita r ON (m.mdc_cod = r.mdc_cod)
                    JOIN consulta c ON (r.con_num = c.con_num)
                    WHERE c.con_data BETWEEN '2023-12-01' AND '2023-12-31'
                    );
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Laboratório'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()