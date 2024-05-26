import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#21 - Nome dos pacientes do sexo F que consultaram em janeiro de 2024 com médico cardiologista.
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT p.pac_nome
FROM paciente p
JOIN consulta c ON (p.pac_mat = c.pac_mat)
JOIN medico m ON (c.med_crm = m.med_crm)
JOIN formacao f ON (m.med_crm = f.med_crm)
JOIN especialidade e ON (f.esp_cod = e.esp_cod)
WHERE p.pac_genero = 'F'
AND c.con_data BETWEEN '2024-01-01' AND '2024-01-31'
AND e.esp_nome = 'Cardiologia';
"""
cursor.execute(sql)
conn.commit()
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()