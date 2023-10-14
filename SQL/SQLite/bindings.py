import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cuidado: Delete no banco de dados
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# Cria a table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT, '
    'weight REAL '
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela.
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
)
# cursor.execute(sql, ['Joana', '4'])
cursor.executemany(sql, (
    ('Joana', 4), ('Jorge', 6)
)
)
connection.commit()

cursor.close()
connection.close()
