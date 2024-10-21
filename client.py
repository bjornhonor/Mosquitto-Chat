import paho.mqtt.client as mqtt
import threading

# Configurações do Broker
broker_address = "localhost"
broker_port = 1883
chat_topic = "chat/room1"

username = input("Digite seu nome de usuário: ")

'''Realiza a conexão do cliente ao broker MQTT e se inscreve no tópico de chat. 
Caso a conexão seja bem-sucedida, exibe uma mensagem de sucesso. Caso contrário, 
exibe uma mensagem de falha com o código de erro.'''
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT!")
        client.subscribe(chat_topic)
    else:
        print("Falha na conexão, código de erro: ", rc)

'''Exibe mensagens recebidas de outros usuários no chat. Evitando exibir mensagens 
do próprio client, validando o username. '''
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    
    if not message.startswith(username + ":"):
        print("\n" + message)
        print(f"{username}> ", end="", flush=True)

'''Envia mensagens para o chat. O loop é executado até que o usuário digite um nome'''
def send_messages():
    while True:
        message = input(f"{username}> ")
        full_message = f"{username}: {message}"
        client.publish(chat_topic, full_message)

# Configura o cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker
client.connect(broker_address, broker_port, keepalive=60)

# Inicia um thread para enviar mensagens
threading.Thread(target=send_messages).start()

# Inicia o loop para processar callbacks MQTT
client.loop_forever()
