import openai
chave_api = "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"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role":"user","content":mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = lista_mensagens
    )

    return response["choices"][0]["message"]


lista_mensagens=[]
while True:
    texto = input("Escreve sua mensagem:")

    if texto =="sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot:", resposta["content"])

#print(enviar_mensagem("Em que ano Einstein publicou a teoria geral da relatividade ?"))