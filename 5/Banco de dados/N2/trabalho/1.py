import sys
sys.dont_write_bytecode = True
from db import *
from tabulate import tabulate
#1 – Nome dos pacientes de gênero F
conn = db_connect()
cursor = conn.cursor()
sql = """
SELECT pac_nome
FROM paciente
WHERE pac_genero = 'F';   
"""
cursor.execute(sql)
rows = cursor.fetchall()
print(tabulate(rows, headers=['Nome Paciente'], tablefmt="fancy_grid", numalign="center", stralign="center"))
cursor.close()