from flask import Flask, jsonify
import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
import sqlite3

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

app = Flask(__name__)

# Função para criar a tabela no banco de dados SQLite
def create_table():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingestion_date TEXT,
            weather_type TEXT,
            weather_values TEXT,
            usage TEXT
        )
    ''') 
    conn.commit()
    conn.close()

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
    values = str(weather_data['main'])
    usage = 'OpenWeather API'

    # 3. Conectar ao banco de dados SQLite e inserir os dados
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO weather (ingestion_date, weather_type, weather_values, usage) VALUES (?, ?, ?, ?)',
                   (date_ingestion, weather_type, values, usage))
    conn.commit()
    conn.close()

    return jsonify({'message': 'ETL executado com sucesso!'})

if __name__ == '__main__':
    create_table()  # Cria a tabela quando o aplicativo é iniciado
    app.run(debug=True)
