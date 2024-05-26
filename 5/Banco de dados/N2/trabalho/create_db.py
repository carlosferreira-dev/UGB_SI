import sqlite3

# Nome do banco de dados
db_name = 'ugb.db'
# Nome do arquivo SQL
sql_file = 'script_db.sql'

# Conectar ao banco de dados (será criado se não existir)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Ler o conteúdo do arquivo SQL
with open(sql_file, 'r') as file:
    sql_script = file.read()

# Executar o script SQL
cursor.executescript(sql_script)

# Fechar a conexão
conn.commit()
conn.close()

print(f"Banco de dados '{db_name}' criado e script '{sql_file}' executado com sucesso.")
