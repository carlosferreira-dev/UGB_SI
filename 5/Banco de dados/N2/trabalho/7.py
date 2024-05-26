import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#7 – Nome dos pacientes que fazem aniversário no mês de SETEMBRO
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT pac_nome
FROM paciente 
WHERE pac_mes_aniv = 7;              
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()