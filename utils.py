"""
Utilitaires pour Smart Shopper Swarm
"""
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def get_openai_api_key():
    """Récupère la clé API OpenAI"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY non trouvée dans le fichier .env")
    return api_key

def get_serper_api_key():
    """Récupère la clé API Serper pour la recherche web"""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY non trouvée dans le fichier .env")
    return api_key
