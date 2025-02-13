import tweepy
from dotenv import load_dotenv
import os
from detect_language import detect_language
from analisar_sentimento import analisar_sentimento

# Carrega as variáveis de ambiente
load_dotenv()

# Autenticação com a API V2 do X (Twitter) usando o bearer token
bearer_token = os.getenv('BEARER_TOKEN')

# Inicializa o cliente da API V2
client = tweepy.Client(bearer_token=bearer_token)

# Termo de busca: "clima"
search_term = "clima"

# Busca os tweets mais recentes sobre o termo 'clima'
response = client.search_recent_tweets(query=search_term, max_results=25, tweet_fields=["created_at"])

# Exibe os tweets encontrados com análise de sentimento
for tweet in response.data:
    # Verifica o idioma do tweet usando a função detect_language
    language = detect_language(tweet.text)
    
    # Realiza a análise de sentimento para todos os tweets usando a função importar
    sentiment = analisar_sentimento(tweet.text)
    
    # Exibe o tweet, o sentimento e o idioma detectado
    print(f"Tweet: {tweet.text}")
    print(f"Sentimento: {sentiment}")
    print(f"Idioma detectado: {language}")
    print("-" * 50)
