import tweepy
from dotenv import load_dotenv
import os
from detect_language import detect_language
from analise_sentimentos import analisar_sentimento

# Carrega as variáveis de ambiente
load_dotenv()

# Autenticação com a API V2 do X (Twitter) usando o bearer token
bearer_token = os.getenv('BEARER_TOKEN')

# Inicializa o cliente da API V2
client = tweepy.Client(bearer_token=bearer_token)

# Termo de busca: "clima"
search_term = clima

# Abre o arquivo CSV para escrita (se não existir, ele será criado)
with open('tweets_sentimentos.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escreve o cabeçalho no CSV (apenas na primeira execução)
    if file.tell() == 0:
        writer.writerow(["Tweet", "Sentimento", "Data", "Idioma"])

    # Realiza a busca em todos os idiomas definidos
    for idioma, termo in termos_busca.items():
        # Busca os tweets mais recentes sobre o termo de busca no idioma correspondente
        response = client.search_recent_tweets(query=termo, max_results=25, tweet_fields=["created_at"], lang="pt")

        # Exibe os tweets encontrados e escreve no arquivo CSV
        if response.data:
            for tweet in response.data:
                sentimento = analisar_sentimento(tweet.text)
                writer.writerow([tweet.text, sentimento, tweet.created_at, "pt"])

                # Exibe o tweet e o sentimento no console
                print(f"Idioma: {idioma}")
                print(f"Tweet: {tweet.text}")
                print(f"Sentimento: {sentimento}")
                print("-" * 50)