from browser import (
    prompt, websocket, window, 
    document, html, bind
)


nome=prompt('Insira seu nome')
ws=websocket.WebSocket(
    f'ws://{window.location.host}/{nome}'
)




@bind('#send', 'click')
def send_message(event):
    ws.send(f'{nome}: {document["text"].value}')
    document["text"].value=''


def on_open(event):
    ws.send(f'{nome} entrou na sala')


def on_message(event):
    messages=document["message"]
    messages <= html.P(event.data)
    messages.scrollTop=(
        messages.scrollHeight - messages.clienteHeight
    )



ws.bind('message', on_message)
ws.bind('open', on_open)
