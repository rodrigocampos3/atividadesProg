from kafka import KafkaConsumer

# Configurações do Kafka
bootstrap_servers = 'localhost:9092'
topic_name = 'meu_topico'

# Cria o consumidor Kafka
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# Lê as mensagens do tópico
for message in consumer:
    print(f'Mensagem recebida: {message.value.decode("utf-8")}')

# Fecha a conexão do consumidor Kafka
consumer.close()