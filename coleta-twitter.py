import tweepy
import csv
from dotenv import load_dotenv
import os
from detect_language import detect_language
from analise_sentimentos import analisar_sentimento

# Carrega as variáveis de ambiente
load_dotenv()

# Autenticação com a API V2 do X (Twitter) usando o bearer token
bearer_token = os.getenv('BEARER_TOKEN')

# Autenticação com o Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
client = tweepy.Client(auth=auth)

# Inicializa o cliente da API V2
client = tweepy.Client(bearer_token=bearer_token)

# Termo de busca: "clima"
search_term = "clima"

# Abre o arquivo CSV para escrita (se não existir, ele será criado)
with open('tweets_sentimentos.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escreve o cabeçalho no CSV (apenas na primeira execução)
    if file.tell() == 0:
        writer.writerow(["Tweet", "Sentimento", "Data", "Idioma"])

    # Realiza a busca em todos os idiomas definidos
    response = client.search_recent_tweets(query=search_term, max_results=25, tweet_fields=["created_at"], lang="pt")

    if response.data:
        for tweet in response.data:
            sentimento = analisar_sentimento(tweet.text)
            writer.writerow([tweet.text, sentimento, tweet.created_at, "pt"])
            
            #Exibir o sentimento do tweet
            print(f"Tweet: {tweet.text}")
            print(f"Sentimento: {sentimento}")
            print("-" * 50)