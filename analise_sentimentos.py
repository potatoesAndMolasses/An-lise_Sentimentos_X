from textblob import TextBlob

# Função para analisar o sentimento de um texto
def analisar_sentimento(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment.polarity
    if sentimento > 0:
        return "Positivo"
    elif sentimento < 0:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    tweet_exemplo = "Amei o novo recurso do Twitter!"
    sentimento = analisar_sentimento(tweet_exemplo)
    print(f"Sentimento: {sentimento}")