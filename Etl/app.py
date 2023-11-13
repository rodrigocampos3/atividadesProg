from flask import Flask, jsonify
import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

app = Flask(__name__)

@app.route('/extract_transform_load')
def extract_transform_load():
    # 1. Extrair dados da API OpenWeather
    api_key = os.getenv('OPENWEATHER_API_KEY')
    city = os.getenv('CITY_NAME')
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(api_url)
    weather_data = response.json()

    # 2. Transformar os dados
    date_ingestion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    weather_type = weather_data['weather'][0]['main']
    values = weather_data['main']
    usage = 'OpenWeather API'

    # 3. Criar DataFrame pandas
    df = pd.DataFrame({
        'Data da Ingestão': [date_ingestion],
        'Tipo': [weather_type],
        'Valores': [values],
        'Uso': [usage]
    })

    # 4. Carregar os dados em uma tabela (usando um arquivo CSV)
    df.to_csv('weather_data.csv', mode='a', header=not os.path.exists('weather_data.csv'), index=False)

    return jsonify({'message': 'ETL executado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
