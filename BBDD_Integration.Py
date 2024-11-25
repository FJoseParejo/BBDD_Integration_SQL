# Integracióin de BBDD SQL

from sqlalchemy import create_engine
import requests
from pyarrow import hdfs
import pandas as pd
import boto3 
from google.cloud import bigquery

# Crear un motor de SQLAlchemy para conectarse a la base de datos
# Cambiar 'dialect+driver://username:password@host:port/database' por los detalles reales de conexión
engine = create_engine('dialect+driver://username:password@host:port/database')
# Leer datos de una tabla SQL directamente a un DataFrame de Pandas
df = pd.read_sql('SELECT * FROM mi_tabla', con=engine)
# Realizar transformaciones en el DataFrame...
# Cargar datos desde Pandas a una nueva tabla en la base de datos
df.to_sql('mi_tabla_transformada', con=engine, if_exists='replace', index=False)

# Integración con APIs web

# Enviar una solicitud GET a una API
response = requests.get('https://api.example.com/data')
# Convierte la respuesta en un Diccionario Python que se llama Data
data = response.json()
# Convertir los datos JSON a un DataFrame
df = pd.json_normalize(data)
# Realizar transformaciones en el DataFrame...
# Integración con Sistemas de Archivos Distribuidos

# Hadoop HDFS

# Conectarse a HDFS
con = hdfs.connect()
# Leer un archivo Parquet desde HDFS en un DataFrame de Pandas
df = pd.read_parquet('hdfs://path/to/myfile.parquet')
# Realizar transformaciones en el DataFrame...
# Guardar un DataFrame como archivo Parquet en HDFS
df.to_parquet('hdfs://path/to/newfile.parquet')

# Integración con Almacenamiento en la Nube 


from io import StringIO
# Configurar cliente S3
s3_client = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')
# Leer CSV desde S3 en un DataFrame
obj = s3_client.get_object(Bucket='my-bucket', Key='path/to/myfile.csv')
df = pd.read_csv(obj['Body'])
# Realizar transformaciones en el DataFrame...
# Guardar un DataFrame en S3 como CSV
csv_buffer = StringIO() # Crea un buffer de memoria 
df.to_csv(csv_buffer, index=False) # Guardamos en el buffer de memoria el dataFrame 
# Colocar el dataFrame y convertir todo el contenido a formato string con getvalue()
s3_client.put_object(Bucket='my-bucket', Key='path/to/newfile.csv', Body=csv_buffer.getvalue())

# Integración con Servicios Big Data

# Configurar cliente de BigQuery
client = bigquery.Client()
# Ejecutar consulta y cargar resultados en DataFrame
query = "SELECT * FROM `project.dataset.table`"
df = client.query(query).to_dataframe()
# Realizar transformaciones en el DataFrame...  