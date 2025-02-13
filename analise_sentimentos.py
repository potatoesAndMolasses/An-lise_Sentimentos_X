from textblob import TextBlob

# Função para analisar o sentimento de um texto
def analisar_sentimento(texto):
    blob = TextBlob(texto)
    sentiment   o = blob.sentiment.polarity
    if sentimento > 0:
        return "Positivo"
    elif sentimento < 0:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":