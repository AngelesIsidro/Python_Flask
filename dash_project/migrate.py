import os
import pandas as pd
from sqlalchemy import create_engine, inspect

# Datos de conexion MySQL
mysql_user = 'root'
mysql_password = '12345678'
mysql_host = 'localhost'
mysql_db = 'sociodemografico'

# Ruta al archivo SQLite
sqlite_file = '/var/www/dash_project/db_project/sociodemografico.db'

# Asegurarse de que el directorio de SQLite existe
sqlite_dir = os.path.dirname(sqlite_file)
if not os.path.exists(sqlite_dir):
    os.makedirs(sqlite_dir)

# Conectar a la base de datos MySQL
mysql_engine = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}')

# Conectar a la base de datos SQLite
sqlite_engine = create_engine(f'sqlite:///{sqlite_file}')

# Crear un inspector para MySQL
inspector = inspect(mysql_engine)

# Obtener las tablas de MySQL
mysql_tables = inspector.get_table_names()

for table in mysql_tables:
    # Leer los datos de MySQL
    df = pd.read_sql_table(table, mysql_engine)

    # Escribir los datos en SQLite
    df.to_sql(table, sqlite_engine, index=False, if_exists='replace')

print("Migracion completada.")
