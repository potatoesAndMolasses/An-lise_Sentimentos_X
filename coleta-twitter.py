import tweepy
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Autenticação com a API do X (Twitter)
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Termo de busca: "clima"
search_term = "clima"

# Coleta os últimos 25 tweets relacionados ao clima
try:
    tweets = api.search_tweets(q=search_term, count=25, lang="pt", tweet_mode="extended")
    
    # Exibe os
