# Processamento de arquivo CSV do Azure Blob Storage para Banco de Dados do Azure usando Python

## Descrição do projeto
Este projeto é uma demonstração de como processar um arquivo CSV armazenado no Azure Blob Storage e inserir seus dados em uma tabela do Banco de Dados do Azure usando Python.

## Como funciona
O script Python se conecta ao Azure Blob Storage usando a biblioteca BlobServiceClient do Azure Storage, faz o download do arquivo CSV, converte-o em um dataframe do pandas e remove a máscara da coluna 'CPF/CNPJ' e converte as colunas de datas no padrão yyyy-MM-dd. Em seguida, ele se conecta ao banco de dados do Azure usando o pyodbc e cria uma conexão com o cursor. Por fim, usa o método to_sql do pandas para criar a tabela no banco de dados do Azure e inserir os dados do dataframe.

## Requisitos
- Python 3.x
- Bibliotecas: pandas, pyodbc, azure-storage-blob
## Como utilizar
- Clone o repositório para sua máquina local.
- Defina as informações de conexão do Azure Blob Storage e do banco de dados do Azure no arquivo init.py.
- Abra um terminal e navegue até o diretório clonado.


### Crie e ative uma virtualenv:
```
python -m venv env
.\env\Scripts\activate
```

### Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

### Execute o script:

```
python __init__.py
```

## Autor
Nome: Hugo Borges

LinkedIn: https://www.linkedin.com/in/hugoborgess/

GitHub: https://github.com/HugoBorgess
