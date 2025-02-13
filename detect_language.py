from langdetect import detect

# Função para detectar o idioma de um tweet
def detect_language(tweet_text):
    try:
        # Detecta o idioma do texto
        language = detect(tweet_text)
        return language
    except Exception as e:
        print(f"Erro na detecção do idioma: {e}")
        return None
