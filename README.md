# Projeto FastAPI WebSockets

Este é um projeto simples que utiliza FastAPI para criar uma aplicação que suporta comunicação bidirecional através de WebSockets.

## Instalação

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).
2. Clone este repositório:

```bash
git clone https://github.com/ze-fernando/Web-sockets.git
```
Navegue até o diretório do projeto:
```bash
cd Web-sockets
```
Instale as dependências utilizando pip:
```bash
pip install -r requirements.txt
```
## Como Usar
Após a instalação das dependências, você pode iniciar o servidor executando o seguinte comando:
```bash
uvicorn app:app --reload
```
Abra um navegador e acesse http://localhost:8000/. Você verá uma página da web com um campo de entrada de texto.

Insira uma mensagem no campo de texto e pressione "Enviar". A mensagem será enviada via WebSocket para o servidor.

O servidor irá responder com a mensagem recebida, que será exibida na página da web.

## Estrutura do Projeto
- app/
  - **\_\_init\_\_.py**: Este arquivo é onde a aplicação FastAPI é criada e as rotas são definidas.
  - **main.py**: Configuração do servidor WebSockets e manipuladores de conexão.
  - **manager.py**: Classe ConnectionManager para gerenciar conexões WebSocket.
- templates/
  - **base.html**: Arquivo HTML base para a interface do usuário.
- static/
  - **conf.py**: Arquivo de configuração para o script Brython.

## Dependências
- **FastAPI**: Um framework web assíncrono para Python.
- **uvicorn**: Um servidor ASGI de alta performance, para aplicações ASGI, como aquelas escritas com o FastAPI.
- **websockets**: Uma biblioteca para implementar comunicação WebSocket em Python.

## Licença
Este projeto está licenciado sob a Licença Pública Geral GNU versão 3.
