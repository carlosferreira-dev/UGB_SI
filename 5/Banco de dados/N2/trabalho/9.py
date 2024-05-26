import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#9 – Nome dos pacientes que tiveram consulta em abril e maio de 2024
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT p.pac_nome
FROM paciente p
JOIN consulta c ON (p.pac_mat = c.pac_mat)
WHERE c.con_data BETWEEN '2024-04-01' AND '2024-04-31'
AND p.pac_nome IN (SELECT p.pac_nome
                    FROM paciente p
                    JOIN consulta c ON (p.pac_mat = c.pac_mat)
                    WHERE c.con_data BETWEEN '2024-05-01' AND '2024-05-31');                    
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()