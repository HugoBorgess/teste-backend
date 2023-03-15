import pandas as pd
import pyodbc
from azure.storage.blob import BlobServiceClient

def process_csv_blob():
    
    # Defina as informações de conexão do Azure Blob Storage e do banco de dados do Azure.
    blob_account_name = 'sua_conta_blob'
    blob_account_key = 'sua_chave_de_acesso'
    blob_container_name = 'seu_container'
    blob_name = 'seu_arquivo.csv'
    server = 'seu_servidor.database.windows.net'
    database = 'seu_banco_de_dados'
    username = 'seu_usuario'
    password = 'sua_senha'
    table_name = 'seu_tabela'
    
    # Conecte-se ao Azure Blob Storage e leia o arquivo CSV para um dataframe do pandas.
    blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={blob_account_name};AccountKey={blob_account_key};EndpointSuffix=core.windows.net")
    blob_client = blob_service_client.get_blob_client(container=blob_container_name, blob=blob_name)
    blob_data = blob_client.download_blob().content_as_text()
    df = pd.read_csv(pd.compat.StringIO(blob_data))
    
    # Remova a máscara da coluna 'CPF/CNPJ' e converta as colunas de datas no padrão yyyy-MM-dd.
    df['CPF/CNPJ'] = df['CPF/CNPJ'].str.replace('[^0-9]+', '')
    df['Data de Emissão'] = pd.to_datetime(df['Data de Emissão'], dayfirst=True).dt.strftime('%Y-%m-%d')
    df['Data de Vencimento'] = pd.to_datetime(df['Data de Vencimento'], dayfirst=True).dt.strftime('%Y-%m-%d')
    df['Data de Compra CCB'] = pd.to_datetime(df['Data de Compra CCB'], dayfirst=True).dt.strftime('%Y-%m-%d')
    
    # Conecte-se ao banco de dados do Azure usando o pyodbc e crie uma conexão com o cursor.
    conn = pyodbc.connect(f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Uid={username};Pwd={password}")
    cursor = conn.cursor()
    
    # Use o método to_sql do pandas para criar a tabela no banco de dados do Azure e inserir os dados do dataframe.
    df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
    
    # Feche a conexão com o banco de dados do Azure.
    conn.close()