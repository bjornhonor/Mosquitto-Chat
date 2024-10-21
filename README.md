# 📨 Sistema de Chat em Tempo Real com MQTT e Mosquitto

Bem-vindo ao nosso sistema de chat em tempo real! 📣

## 📋 Descrição

Este projeto é um **sistema de chat em tempo real** desenvolvido em **Python**, utilizando o protocolo **MQTT** com o broker **Mosquitto**. A aplicação permite que múltiplos usuários enviem e recebam mensagens instantaneamente, facilitando a comunicação em redes locais.

## 👥 Integrantes

- **Bruno Penteado Carrara** 
- **Gabriel Henrique da Silva** 
- **Filipe Dias Carvalho de Azevedo**
- **Raphaela de Souza Ribeiro**

### 🎥 Exemplo de Uso

[DEMO](https://youtu.be/PIHTmBmX9ic)

## 🚀 Como Executar

### 🛠️ Pré-requisitos

- **Python 3.x** instalado. [🔗 Download Python](https://www.python.org/downloads/)
- Biblioteca **Paho-MQTT** instalada:
  ```bash
  pip install paho-mqtt
  ```
- **Broker Mosquitto** instalado e em execução. [🔗 Instruções de Instalação](https://mosquitto.org/download/)

### 📦 Passos para Execução

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Iniciar o Broker Mosquitto**

   - **Linux:**

     ```bash
     mosquitto
     ```

   - **Windows:**

     - Abra o Prompt de Comando e execute:
       ```cmd
       mosquitto
       ```

3. **Executar o Cliente de Chat**

   - Em um terminal, execute:
     ```bash
     python client.py
     ```
   - Insira um nome de usuário quando solicitado.

4. **Executar Múltiplos Clientes**

   - Abra novos terminais para cada usuário adicional e repita o passo anterior.
   - Cada instância representará um usuário diferente no chat.

## 📝 Funcionalidades

- ✅ **Comunicação em Tempo Real**: Mensagens são entregues instantaneamente.
- ✅ **Múltiplos Usuários**: Suporta vários usuários simultaneamente.
- ✅ **Interface Simples**: Interação via linha de comando.
- ✅ **Escalabilidade**: Fácil adição de novos usuários e funcionalidades.

## 📚 Tecnologias Utilizadas

| Tecnologia     | Descrição                                      |
| -------------- | ---------------------------------------------- |
| Python         | Linguagem de programação                       |
| MQTT           | Protocolo de comunicação leve                  |
| Paho-MQTT      | Biblioteca MQTT para Python                    |
| Mosquitto      | Broker MQTT para gerenciamento de mensagens    |


