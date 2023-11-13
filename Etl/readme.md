# ETL Flask App

Este é um aplicativo Flask simples para realizar o processo ETL (Extração, Transformação e Carga) a partir da API OpenWeather e armazenamento dos dados no PostgreSQL.

## Configuração

Antes de executar o aplicativo, é necessário configurar algumas variáveis de ambiente. Crie um arquivo `.env` na raiz do seu projeto com as seguintes variáveis:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
CITY_NAME=your_city_name

Substitua pelos valores seus valores de api e nome de cidade

#Instalação

## Instale as dependências do Python:
    ```env
    pip install -r requirements.txt

## Execute o aplicativo Flask:
    ```env
    python app.py
O aplicativo estará disponível em http://127.0.0.1:5000/.

#Testes de integração
Para executar os testes de integração, execute:
    ```env
    python test_app.py
